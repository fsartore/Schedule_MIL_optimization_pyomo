import pyomo.environ as pyomo
from Parameters import T,  task_days, standard_interval,units_partition
from Parameters import task_flexibility_up, task_flexibility_down, units_partition, check_overlap
from Parameters import counter_unfeasibility_max, counter_overlap_max, max_time, check_time
from Constraints import Constraints_task
from Bounds import Bounds_class
from Bounds import bound_dict_t, possible_unit_times,  partition_dict
from Bounds import   bound_dict_end, n_units_tuple 
from datetime import datetime
import time
from pyomo.contrib.appsi.solvers import Highs
import numpy as np
import pandas as pd
from elaborate_and_save_data import save_data_results, fill_dataframe, process_task_data
from time_handling import TimeHandling
from Task_Manager import unit_todo_task, task_range, target_time
from handling_unfeasibility import handle_unfeasibility, adjusted_bound_dict_init
from read_previous_task import ReadLasttask
from Parameters import unit_names, today,  end_year, best_task_delta_weeks, best_task_delta_days
import Directories as dir

start_time = time.time()
current_year_list = [str(today.year + i) for i in range(end_year - today.year + 1)] 
print('current_year_list:', current_year_list)

'''Define directories and classes instances'''
file_path_input =  dir.folder_path_input                                        # were we store the resulkts that will serve as input for the next iteration
previous_tasktenance_path = dir.last_task_path                              # path to the last task data
time_handling_instance = TimeHandling(current_year_list, file_path_input,today)
previous_year_list = time_handling_instance.generate_previous_year_list()
start_date_list, end_date_list = time_handling_instance.generate_start_end_dates()
holidays_days_list = time_handling_instance.generate_holidays_days_list()
previous_task_instance = ReadLasttask(unit_names, previous_tasktenance_path, today)

# Create a dictionary and a dataframe that will store the availability of each year for result analysis
availability_max_dict = {i: 0 for i in current_year_list}
availability_dict = {i: 0 for i in current_year_list}
objective_data = pd.DataFrame(columns=['Task Flexibility', 'Unit Partitions', 'Objective'])


# initialize
year_flag = True
year_counter = 0
objective = 0
year_counter_max = len(previous_year_list)
n_unit_history = []
unit_list_name = unit_names
dict_delta_current = None
unfeasible = False
adjustments_tracker = None
target_week_dict_unfeasible = None
dict_pairs_unfeasible = None
target_week_base_unfeasible = None
adjustments_tracker_base = None
counter_unfeasibility = 0
counter_overlap = 0
task_flexibility_down_base = task_flexibility_down
task_flexibility_up_base = task_flexibility_up
dict_delta = {unit: round(standard_interval*4.345) for unit in unit_names}       # dict_delta with the number of delta weeks per each unit


'''Iterate over the years'''
while year_flag == True:

    #Optional time escape to set
    end_time = time.time()
    if check_time == True:
        if end_time - start_time > max_time:  #seconds
            raise TimeoutError(f'Time taken is more than {max_time} seconds')

    #Actualize time_depending variables
    previous_year = previous_year_list[year_counter]
    current_year = current_year_list[year_counter]
    start_date = start_date_list[year_counter]
    end_date = end_date_list[year_counter]

    print(f'\n\n\n Current year = {current_year }\n\n\n')

    " For specifics, dirict the the specific folder"
    days_to_monday, time_horizon_tot = time_handling_instance.calculate_time_horizon(start_date, end_date)             # if the year does not start on monday
    weeks = time_handling_instance.weeks_in_time_horizon(start_date, end_date,days_to_monday)                          # n of weeks
    if previous_year == previous_year_list[0] or (year_counter != 0 and n_unit_history[year_counter-1] == 0):          # the first time we read the data from the last task file
        dict_previous_task, previous_task_dict_year = previous_task_instance.read_last_task()
    else:
        df_lmy = pd.read_excel(f'{file_path_input}/input_{previous_year}.xlsx', sheet_name='last_task')                                                               # then from the  result file that we have just created
        dict_previous_task = dict(zip(df_lmy['Unit'], df_lmy['Last task']))
    dict_weeks_previous_task = {unit: (start_date - pd.to_datetime(date)).days//7 for unit, date in dict_previous_task.items()} # weeks ago of previous task
    previous_task_data = [int(-value) for value in dict_weeks_previous_task.values()]
    n_units_tot, dict_unit_todo_task, dict_interval_to_do_task = unit_todo_task(unit_list_name, previous_task_data, weeks, dict_delta) # specific dict that will be involved in the current_year analysis
    target_dict = target_time(dict_previous_task,dict_unit_todo_task,  dict_interval_to_do_task) # to evaluate the godness of the solution with respect to the target task week 
    n_unit = n_units_tot // units_partition                                                      # in case we had to partition for solver limits
    n_unit_history.append(n_units_tot)                                                           # to handle the problem of having no unit in the first year
    if n_units_tot == 0:                                                                         # if there are no units to do the task we skip to the next year
        year_counter = year_counter + 1
        if year_counter == year_counter_max:
            year_flag = False           
        continue
    remainder = n_units_tot % units_partition 
    bound_dict_init, target_week_dict = task_range(dict_interval_to_do_task, weeks, task_flexibility_up, task_flexibility_down, dict_unit_todo_task) # interval of flexibility for the task
    dict_pairs = {(i, j): 0 for i in target_week_dict.keys() for j in target_week_dict.keys() if i != j} 
    
    '''HANDLE UNFEASIBILITY'''
    if unfeasible == True:
        print(f'\n\n\n Counter_unfeasibility: {counter_unfeasibility} \n\n\n')
        target_week_dict_unfeasible, adjustments_tracker, dict_pairs_unfeasible, target_week_base_unfeasible, adjustments_tracker_base, counter_unfeasibility = handle_unfeasibility( target_week_dict, weeks, counter_unfeasibility, counter_unfeasibility_max, task_flexibility_down,task_flexibility_up,adjustments_tracker, target_week_dict_unfeasible, dict_pairs_unfeasible, target_week_base_unfeasible, adjustments_tracker_base)
        bound_dict_init = adjusted_bound_dict_init(target_week_dict_unfeasible, weeks, task_flexibility_up, task_flexibility_down)
    try:
        # Partition the units in subgroups for solver efficiency 
        dict_partitions = partition_dict(bound_dict_init, units_partition, n_unit, n_units_tot, remainder)
        # Create a Flag that is True untill we have solved all of the subproblems
        flag = True
        # Start a counter that will be used to count the number of iterations
        counter = 0
        counter_max = units_partition if units_partition <= n_units_tot else n_units_tot
        # Create an empty list current_x where we will store the values of x
        current_x = []
        # Initialize 
        sum_columns = []
        busy_days = []
        active_unit_keys_list = n_units_tuple(dict_unit_todo_task)
        # initialize a dict of tuples to later store the start and end time of tasks for each units
        start_end_time_dict = {i: (0,0) for i in active_unit_keys_list}
        # To switch back to standard interval after a task
        dict_delta_current = {}

        '''Enter a while loop that will run until the flag is False'''
        while flag == True:

            
            m = pyomo.ConcreteModel()
            #############Sets##################
            dict_partitions_current = dict_partitions[counter]          
            active_unit_keys_list_current = [i for i in dict_partitions_current.keys()] # list of the keys of the current partition
            start_end_time_dict_current = {i: (0,0) for i in active_unit_keys_list_current}

            bound_obj_t = Bounds_class(m, bound_dict_t(dict_partitions_current, weeks, T,days_to_monday, time_horizon_tot, best_task_delta_weeks))
            n_unit_element = n_units_tuple(dict_partitions_current)
            m.n_units = pyomo.Set(initialize = n_unit_element)                   # Define a set for units
            m.t = pyomo.Set(m.n_units, initialize = bound_obj_t.bounds_rule)   # Define a set for time steps
            bound_dict_t_current = bound_dict_t(dict_partitions_current, weeks, T,days_to_monday,time_horizon_tot, best_task_delta_weeks)
          
            m.NN = pyomo.Set(initialize = possible_unit_times(bound_dict_t_current)) # Define a set for possible units-times couples
            m.weekends = pyomo.Set(initialize=time_handling_instance.weekend_set(start_date,time_horizon_tot)) # Define a set for weekends
            m.holidays_day = pyomo.Set(initialize = time_handling_instance.holidays_in_time_horizon(start_date, end_date,year_counter)) # Define a set for holidays
            m.time_horizon_tot = pyomo.RangeSet(1, time_horizon_tot) # Define a range set for time horizon

            bound_obj_init = Bounds_class(m, dict_partitions_current)
            bound_obj_end = Bounds_class(m, bound_dict_end(dict_partitions_current, weeks, best_task_delta_weeks))

            ############Sets to init times##########
            m.init_times = pyomo.Param(m.n_units, initialize= bound_obj_init.bounds_rule_zeroinit)
            m.end_times = pyomo.Param(m.n_units, initialize= bound_obj_end.bounds_rule_zeroend)

            #############Variables##############
            '''Define a binary variable x,...
            x==1 if the task is performed at time t, x==0 otherwise'''
            m.x = pyomo.Var(m.n_units, m.time_horizon_tot, domain= pyomo.Binary, initialize = 0)
            m.tstart = pyomo.Var(m.n_units, domain=pyomo.NonNegativeIntegers, name="t_start" ,bounds = bound_obj_init.bounds_rule)  # start task
            m.tstart.pprint()
            m.tend = pyomo.Var(m.n_units, domain=pyomo.NonNegativeIntegers, name="t_end", bounds = bound_obj_end.bounds_rule)  # end task
                
            #############Constraints##############
            constr_obj = Constraints_task(m, time_horizon_tot, task_days, T,days_to_monday)
            '''Add constraints to ensure that end time is after start time'''
            m.after_start = pyomo.Constraint(m.n_units, rule = constr_obj.end_after_start_rule)
            '''Constraint to ensure x = 0 when before the start of the task'''
            m.InitConstr = pyomo.Constraint(m.NN, rule=constr_obj.m_init_rule)
            '''Constraint to ensure x = 0 when before the start of the task'''
            m.EndConstr = pyomo.Constraint(m.NN, rule=constr_obj.m_end_rule)
            '''Constraint to ensure x = 0 when it is a weekend'''
            m.WeekendConstr = pyomo.Constraint(m.n_units, m.time_horizon_tot, rule=constr_obj.m_weekend_rule)
            '''Constraint to ensure x = 0 when it is a holiday'''
            m.HolidaysConstr = pyomo.Constraint(m.n_units, m.time_horizon_tot, rule=constr_obj.holidays_rule)
            '''Constraint to ensure x = 0 when it is before the start of the task'''
            m.ZeroInitConstr = pyomo.Constraint(m.n_units, m.time_horizon_tot, rule=constr_obj.zero_init_rule)
            '''Constraint to ensure x = 0 when it is after the end of the task'''
            m.ZeroEndConstr = pyomo.Constraint(m.n_units, m.time_horizon_tot, rule=constr_obj.zero_end_rule)
            '''Constraint to ensure the sum of x is equal to the number of task days'''
            m.sumConstr = pyomo.Constraint(m.n_units, rule=constr_obj.task)
            '''Constraint to ensure that only one task is performed at a time'''
            m.overlapConstr = pyomo.Constraint(m.time_horizon_tot, rule=constr_obj.no_overlap)

            #############Objective##############
            '''Objective function to minimize the number of task days taking holidays into account'''
            obj_expr = sum((m.tend[i]*T) - ((m.tstart[i]-1)*T+1) for i in m.n_units)
            m.objective = pyomo.Objective(expr = obj_expr, sense=pyomo.minimize)

            "in case of partition add the previous results as forbidden days"
            if busy_days != []:
                m.busy_days = pyomo.Set(initialize=busy_days)
            if busy_days != []:
                m.BusyConstr = pyomo.Constraint(m.n_units, m.time_horizon_tot, rule=constr_obj.busy_days)    

            #############Solve#################
            solver = pyomo.SolverFactory('gurobi')
            #solver = pyomo.SolverFactory('glpk')
            #solver = pyomo.SolverFactory('cbc')
            # solver = pyomo.SolverFactory('ipopt')
            #solver  = Highs()
            #solver = HiGHS(time_limit=10, mip_heuristic_effort=0.2, mip_detect_symmetry="on")

            '''Print solution'''
            result = solver.solve(m)
            print("Objective: ", pyomo.value(m.objective))       
            objective += pyomo.value(m.objective)
            print("Start End Time: ")
            for i in m.n_units:
                print(f"unit {i}: Start Time = {pyomo.value(m.tstart[i])}, End Time = {pyomo.value(m.tend[i])}")

            # retrieve the values  of x after being modified in case the starting date of task is not the first day of the time horizon 
            specific_x, start_end_time_dict_current = time_handling_instance.modify_task_schedule(check_overlap, m,days_to_monday,counter, current_x, start_end_time_dict_current,active_unit_keys_list_current, counter_overlap, counter_overlap_max, task_days)           
            # update the start_end_time_dict with the values of start_end_time_dict_current
            start_end_time_dict.update(start_end_time_dict_current)
            #  Define x as a (n-unit, time_horizon_tot) matrix
            current_x = current_x + specific_x
            # Define sum_columns as the sum of the columns of x
            sum_columns = [sum([current_x[i][j] for i in range(len(current_x))]) for j in range(len(current_x[0]))]
            # retrieve the busy_days that are equal to 1
            busy_days = [i+1 for i in range(len(sum_columns)) if sum_columns[i] == 1] 
            # Add 1 to the counter
            counter = counter + 1
            # Update the delta dictionary with the standard interval after having gone trough the first changement          
            dict_delta_current.update({i: round(standard_interval*4.345) for i in dict_partitions_current.keys()})

            # if counter is equal to the number of counter max then set the flag to False
            if counter == counter_max:
                    flag = False

    except ValueError:
        '''HANDLE UNFEASIBILITY OR OVERLAP ERRORS'''
        if counter_unfeasibility <= counter_unfeasibility_max:
            print('\033[91m' + 'solution not found, Model was proven to be infeasible or in overlap.' + '\033[0m')
            unfeasible = True
            counter_unfeasibility += 1
        else: 
            #in case nothing worked, increase flexibility
            if counter_overlap <= counter_overlap_max:
                print('\033[91m' + 'Overlap, relax the flexibility.' + '\033[0m')
                unfeasible = False
                task_flexibility_up += 1
                task_flexibility_down += 1
                counter_unfeasibility = 0
                counter_overlap += 1
            else:
                # raise a termination error
                raise Exception('Overlap and unfeasibility, we tried everything.')

    else:
        # analyze the actual availability with comparison to the maximum availability
        days_time_hoz_list = time_handling_instance.days_in_time_horizon(start_date, end_date) # associate to the elements of start_end_time_dict the corrispondig dates
        m.names_time_horizon_tot = pyomo.Set(initialize= days_time_hoz_list)
        for i in start_end_time_dict:
            start_end_time_dict[i] = (days_time_hoz_list[start_end_time_dict[i][0]-1], days_time_hoz_list[start_end_time_dict[i][1]-1]) # for every unit, the start end date of the task


        # create a dict to calculate the difference between the target date and the start date of task   
        dict_diff = {i: (datetime.strptime(start_end_time_dict[i][0], "%Y-%m-%d") - target_dict[i]).days for i in active_unit_keys_list}
        df_difference = pd.DataFrame(dict_diff.values(), index=dict_diff.keys(), columns=['Days Difference'])

        #Create a DataFrame to hold the data
        m.n_unit_tot = pyomo.Set(initialize = active_unit_keys_list)
        df = pd.DataFrame(0, index=m.n_unit_tot, columns=m.names_time_horizon_tot)     
        df = fill_dataframe(df, current_x, active_unit_keys_list, days_time_hoz_list) 
        # Final result to store
        final_x = np.round(np.array(current_x), 1)

        # this function does not modify the datas
        file_path_input =  dir.folder_path_input
        if previous_year == previous_year_list[0] or (year_counter != 0 and n_unit_history[year_counter-1] == 0): # if first year
            process_task_data(dict_previous_task,  
                                    start_end_time_dict, file_path_input, current_year, previous_year, previous_year_list)
        else:  # if following years
            df_lm = pd.read_excel(f'{file_path_input}/input_{previous_year}.xlsx', sheet_name='last_task')
            process_task_data(dict_previous_task,  
                                    start_end_time_dict, file_path_input, current_year, previous_year, previous_year_list, df_lm)
        # Save the results to future use       
        # Save the results to future use
        save_data_results(dir.folder_path_results, df,  final_x, start_end_time_dict, active_unit_keys_list, 
                          current_year,df_difference, dict_diff,dict_unit_todo_task, unit_list_name, time_horizon_tot,
                           adjustments_tracker)
     
        # update dict_delta with standard interval
        dict_delta.update(dict_delta_current)
        # Reinitialize
        unfeasible = False
        dict_delta_current = None
        adjustments_tracker = None
        target_week_dict_unfeasible = None
        dict_pairs_unfeasible = None
        target_week_base_unfeasible = None
        adjustments_tracker_base = None
        counter_unfeasibility = 0
        counter_overlap = 0
        task_flexibility_down = task_flexibility_down_base
        task_flexibility_up = task_flexibility_up_base

        # Update the year
        year_counter = year_counter + 1
        if year_counter == year_counter_max:
            year_flag = False


'''Calculate the time taken'''
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

