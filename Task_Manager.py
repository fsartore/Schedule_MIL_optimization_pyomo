######## Objective: give back a dictonary of couples ##########
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import itertools

def unit_todo_task(unit_list_name, last_task_data, weeks,  dict_delta):

    '''
    Check if the task will be held in the time horizon under analysis, 
    return the number of units to undergo the task and a dictionary with the units to undergo the task.

    :param unit_list_name: list of units to undergo the task
    :type unit_list_name: list[str]
    :param last_task_data: list of the last time the task was held for each unit
    :type last_task_data: list[int]
    :param weeks: number of weeks in the time horizon
    :type weeks: int
    :param dict_delta: dictionary with the delta time between tasks for each unit
    :type dict_delta: dict[str, int]
    :returns: 
        - n_units: number of units to undergo the task
        - unit_todo_task_dict: dictionary with the units to undergo the task and their last task time
        - dict_interval_to_do_task: dictionary with the interval between tasks for each unit which will undergo the task
    :rtype: tuple[int, dict[str, int], dict[str, int]]
    '''
    n_units = 0
    unit_todo_task_dict = {}  # Initialize as an empty dictionary
    dict_last_task = {i: 0 for i in unit_list_name}  
    dict_interval_all = dict_delta
    for i in range(len(last_task_data)):
        dict_last_task[unit_list_name[i]] = last_task_data[i]    
    for i in dict_last_task.keys():
        if 0<= dict_last_task[i] + round(dict_interval_all[i]) <= weeks:
            n_units += 1
            unit_todo_task_dict[i] = dict_last_task[i]  # Update the dictionary here
    # order the dictonary by the number of weeks since the last task
    unit_todo_task_dict = dict(sorted(unit_todo_task_dict.items(), key=lambda item: item[1]))
    # order dict_interval_to_do_task with the same sequence of keys as unit_todo_task_dict
    dict_interval_to_do_task = {i: dict_interval_all[i] for i in unit_todo_task_dict.keys()}

    return n_units, unit_todo_task_dict, dict_interval_to_do_task



def target_time(dict_last_task, dict_unit_todo_task, dict_interval_to_do_task):
    '''
    Calculate the target week for the next task for each unit in the dictionary dict_unit_todo_task.

    :param dict_last_task: dictionary with the last task time in weeks for each unit
    :type dict_last_task: dict[str, int]
    :param dict_unit_todo_task: dictionary with the units to undergo the task and their last task time week
    :type dict_unit_todo_task: dict[str, int]
    :param dict_interval_to_do_task: dictionary with the interval between tasks for each unit which will undergo the task
    :type dict_interval_to_do_task: dict[str, int]
    :returns:
        - dict_target: dictionary with the target week for the next task for each unit in dict_unit_todo_task
    :rtype: dict[str, int]
    '''
    dict_target = {}
    for unit in dict_unit_todo_task.keys():
        last_task = dict_last_task[unit]
        # Calculate initial target time
        target_time = last_task + relativedelta(days=dict_interval_to_do_task[unit]*7+3)  # +3 because the task is held on Mondays and finishes on Fridays
        # Adjust target time to the closest Monday
        weekday = target_time.weekday()
        if weekday != 0:  # If not Monday
            if weekday <= 3:  # From Tuesday to Thursday, go back to the previous Monday
                days_to_subtract = weekday
                target_time -= timedelta(days=days_to_subtract)
            else:  # From Friday to Sunday, go forward to the next Monday
                days_to_add = 7 - weekday
                target_time += timedelta(days=days_to_add)        
        dict_target[unit] = target_time
    return dict_target    


def task_range(dict_intervall_to_do_task, weeks,  task_flexibility_up, task_flexibility_down, dict_unit_todo_task):

    '''
    This function returns a dictionary of tuples with the bounds for the task times in weeks for each unit to undergo the task
    given the task flexibility from Parameters. It also returns a dictionary with the target week for the next task for each unit,
    ordered according to the bounds.

    :param dict_interval_to_do_task: dictionary with the interval between tasks for each unit which will undergo the task
    :type dict_interval_to_do_task: dict[str, int]
    :param weeks: number of weeks in the time horizon
    :type weeks: int
    :param task_flexibility_up: maximum number of weeks the task can be delayed
    :type task_flexibility_up: int
    :param task_flexibility_down: maximum number of weeks the task can be anticipated
    :type task_flexibility_down: int
    :param dict_unit_todo_task: dictionary with the units to undergo the task and their last task time week
    :type dict_unit_todo_task: dict[str, int]
    :returns:
        - bound_dict_init: dictionary with the bounds for the task times in weeks for each unit to undergo the task
        - target_week_dict: dictionary with the target week for the next task for each unit, ordered according to the bounds
    :rtype: dict[str, int]
    '''
    bound_dict_init = {i: (1, weeks) for i in dict_unit_todo_task.keys()}
    target_week_dict ={i: 0 for i in dict_unit_todo_task.keys()}

    for i in dict_unit_todo_task.keys():
        delta_week_base = round(dict_intervall_to_do_task[i])

        if delta_week_base+dict_unit_todo_task[i] <= 1:
            target_week_dict[i] = 1
            if target_week_dict[i]+task_flexibility_up <= weeks:
                bound_dict_init[i] = (1, target_week_dict[i]+task_flexibility_up)
            else:
                bound_dict_init[i] = (1, weeks)
        elif delta_week_base+dict_unit_todo_task[i] >= weeks:
            target_week_dict[i] = weeks
            if target_week_dict[i]-task_flexibility_down >= 1:
                bound_dict_init[i] = (target_week_dict[i]-task_flexibility_down, weeks)
            else:
                bound_dict_init[i] = (1, weeks)
        elif delta_week_base+dict_unit_todo_task[i] > 1 and delta_week_base+dict_unit_todo_task[i] < weeks:
            target_week_dict[i] = delta_week_base+dict_unit_todo_task[i]  
            if target_week_dict[i]-task_flexibility_down >= 1 and target_week_dict[i]+task_flexibility_up <= weeks:
                bound_dict_init[i] = (target_week_dict[i]-task_flexibility_down, target_week_dict[i]+task_flexibility_up)
            elif target_week_dict[i]-task_flexibility_down < 1 and target_week_dict[i]+task_flexibility_up <= weeks:
                bound_dict_init[i] = (1, target_week_dict[i]+task_flexibility_up)
            elif target_week_dict[i]-task_flexibility_down >= 1 and target_week_dict[i]+task_flexibility_up > weeks:
                bound_dict_init[i] = (target_week_dict[i]-task_flexibility_down, weeks)
            else:
                bound_dict_init[i] = (1, weeks)

    # Order bound_dict_init by the first value of the tuples
    bound_dict_init = dict(sorted(bound_dict_init.items(), key=lambda item: item[1][0]))

    # Order target_week_dict to match the order of bound_dict_init
    target_week_dict = {k: target_week_dict[k] for k in bound_dict_init.keys()}

    
    return bound_dict_init, target_week_dict


def partition_dict(bound_dict_init, units_partition, n_units, n_units_tot, remainder):
    """
    Partitions the units according to the number of subproblems.
    This function divides the original optimization problem into multiple subproblems, each containing a fraction of the total number of units' tasks.

    :param bound_dict_init: The initial bound dictionary.
    :type bound_dict_init: dict
    :param units_partition: The number of partitions.
    :type units_partition: int
    :param n_units: The number of units per partition.
    :type n_units: int
    :param n_units_tot: The total number of units.
    :type n_units_tot: int
    :param remainder: The remainder when dividing the total number of units by the number of partitions.
    :type remainder: int
    :returns: A list of dictionaries, each containing a partition of the units.
    :rtype: list[dict]
    """
    items = iter(bound_dict_init.items())
    dict_partitions = []
    if units_partition <= n_units_tot:
        if remainder == 0:
            dict_partitions = [dict(itertools.islice(items, n_units)) for _ in range(units_partition)]
        else:
            dict_partitions = [dict(itertools.islice(items, n_units+1)) if i < remainder else dict(itertools.islice(items, n_units)) for i in range(units_partition)]
    else:
        # If units_partition is greater than n_units_tot, split into groups of one element
        dict_partitions = [dict([next(items)]) for _ in range(n_units_tot)]
    return dict_partitions



