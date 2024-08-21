import pandas as pd
import os
import pyomo.environ as pyomo

#:caption: 'Contents:'
#:maxdepth: 2
class TimeHandling:
    def __init__(self, current_year_list, file_path_input,today):
        self.current_year_list = current_year_list
        self.file_path_input = file_path_input
        self.today = today
        self.start_date_list, self.end_date_list = self.generate_start_end_dates()
        self.holidays_days_list = self.generate_holidays_days_list()
        
    def generate_previous_year_list(self):  
        previous_year_list = []
        for i in range(len(self.current_year_list)):
            previous_year_list.append(str(int(self.current_year_list[i])-1))
        return previous_year_list

    def generate_start_end_dates(self):
        today_timestamp = pd.to_datetime(self.today)
        start_date_list = [today_timestamp] + [pd.to_datetime(f'{year}-01-01') for year in self.current_year_list[1:]]
        end_date_list = [pd.to_datetime(f'{self.today.year + 1}-01-01')] + [pd.to_datetime(f'{int(year) + 1}-01-01') for year in self.current_year_list[1:]]
        return start_date_list, end_date_list

    def generate_holidays_days_list(self):
        '''
        Generate a list of holidays for each year in the time horizon under analysis.
        To perform this task, the function reads the holidays from an Excel file.
        The Excel file must have a sheet named 'Feriados' with the following columns:
        - year 2020, year 2021, year 2022, ...
        Each row represents a holiday.
        If a holiday is not present in a year, the cell must be empty.
        :returns: holidays_days_list: list of holidays for each year in the time horizon
        '''
        holidays_days_list = []
        for year in self.current_year_list:
            file_path = os.path.join(self.file_path_input, f"feriados.xlsx")
            df_hol = pd.read_excel(file_path, sheet_name='Feriados')
            df_hol_year = df_hol[f'year {year}']
            holidays_days_list.append([date.strftime('%Y-%m-%d') for date in df_hol_year if pd.notna(date)])
        return holidays_days_list

    def calculate_time_horizon(self, start_date, end_date):
        weekday_of_start_date = start_date.weekday()
        days_to_monday = (7 - weekday_of_start_date) % 7
        time_horizon_tot = (end_date - start_date).days + 1
        return days_to_monday, time_horizon_tot

    def holidays_in_time_horizon(self, start_date, end_date, year_counter):
        holidays = []
        for holiday in self.holidays_days_list[year_counter]:
            holiday_date = pd.to_datetime(holiday)
            if start_date <= holiday_date <= end_date:
                holidays.append((holiday_date - start_date).days+1)
        return holidays

    def weeks_in_time_horizon(self, start_date, end_date, days_to_monday):
        first_monday_date = start_date + pd.Timedelta(days=days_to_monday)
        delta_weeks = (end_date+pd.Timedelta(days=2) - first_monday_date).days // 7 # 2 because if it was friday
        if first_monday_date + pd.Timedelta(days=delta_weeks*7) > end_date+pd.Timedelta(days=2):
            delta_weeks -= 1
        return delta_weeks

    def days_in_time_horizon(self, start_date, end_date):  
        date_range = pd.date_range(start_date, end_date)
        return [date.strftime('%Y-%m-%d') for date in date_range]

    def weekend_set(self, start_date, time_horizon_tot):   
        weekday_of_start_date = start_date.weekday()
        return [i for i in range(1, time_horizon_tot + 1) if (i + weekday_of_start_date) % 7 == 6 or (i + weekday_of_start_date) % 7 == 0]

    def weekends_in_time_horizon(self, start_date, end_date):  # datetype
        date_range = pd.date_range(start_date, end_date)
        weekends = date_range[date_range.to_series().dt.dayofweek >= 5]
        return [date.strftime('%Y-%m-%d') for date in weekends]

    def modify_task_schedule(self,check_overlap,  m, days_to_monday, counter,storage_x,  start_end_time_dict, active_unit_keys_list, counter_overlap,counter_overlap_max, task_days):
        '''
        This function modifies the task schedule to make it feasible.
        This is a complex function that adjusts the solution to be feasible, to avoid overlaps, to make the first day Monday
        and to ensure that the task days are consecutive.

        Three checks:
        1) first day is not monday
        2) the task days are not consecutive
        3) the solution overlaps with other solutions

        Update specific_x, the current solution, depending on the quality of the modified solutions
        CRITERIAS:
        1) favour the solution with less task days to improve the availability
        2) avoid overlaps
        ACTIONS:
        1) If all good update specific_x
        2) Raise a value error to activate unfeasible tricks to distribute better the target times
        3) If close to the last unfeasible tricks, accept an overlap solution

        :param check_overlap: True if we want the solver to restart in case of overlap
        :param m: model
        :param days_to_monday: days to the first monday from the first day
        :param counter: counter of the number of times the function was called
        :param storage_x: where previous solution of the same year are stored
        :param start_end_time_dict: start end of task for each units
        :param active_unit_key_list: unit in this partition to be possibly changed
        :param counter_overlap: counter of various unfiseability for overlap
        :param counter_overlap_max: maximum number of unfeasibility for overlap
        :param task_days: number of task days
        :returns: specific_x: the modified solution
        :returns: start_end_time_dict: the start end time of the modified solution
        
        '''


        # Import current solution of current partition
        specific_x = [[pyomo.value(m.x[i,j]) for j in m.time_horizon_tot] for i in m.n_units]
        specific_x_prev =  [[pyomo.value(m.x[i,j]) for j in m.time_horizon_tot] for i in m.n_units]
        specific_x_next = [[pyomo.value(m.x[i,j]) for j in m.time_horizon_tot] for i in m.n_units]

        # To get a unique list of all indices where any element of specific_x is 1, considering specific_x is a list of lists
        all_busy_days_prev = list(set(j for i in range(len(storage_x)) for j, value in enumerate(storage_x[i]) if value == 1))

        #Initiate
        first_day_prev = [0 for _ in range(len(active_unit_keys_list))]
        last_day_prev = [0 for _ in range(len(active_unit_keys_list))]
        task_per_prev_monday_prev = [0 for _ in range(len(active_unit_keys_list))]
        first_day_next = [0 for _ in range(len(active_unit_keys_list))]
        last_day_next = [0 for _ in range(len(active_unit_keys_list))]
        task_per_next_monday_next = [0 for _ in range(len(active_unit_keys_list))]


        for index, i in enumerate(active_unit_keys_list):
            first_day = [j for j in m.time_horizon_tot if pyomo.value(m.x[i,j]) == 1][0]
            last_day = [j for j in reversed(m.time_horizon_tot) if pyomo.value(m.x[i,j]) == 1][0]
            num_weekends = sum(1 for j in range(first_day, last_day+1) if j in m.weekends)
            num_holidays = sum(1 for j in range(first_day, last_day+1) if j in m.holidays_day)
            total = num_weekends + num_holidays
            zero_days = int((last_day+1 - first_day)-(total + sum(pyomo.value(m.x[i,j]) for j in range(first_day, last_day+1) if j not in m.weekends and j not in m.holidays_day)))
            days_to_previous_monday = (first_day - (days_to_monday+1)) % 7
            days_to_next_monday = (7-days_to_previous_monday) % 7 if days_to_previous_monday != 0 else 7
            hol_between_prev_mon_and_first_day = sum(1 for j in range(first_day - days_to_previous_monday, first_day+1) if j in m.holidays_day)
            # Initiate
            first_day_prev[index] = first_day
            first_day_next[index] = first_day
            last_day_prev[index] = last_day
            last_day_next[index] = last_day
            task_per_prev_monday_prev[index]= (last_day_prev[index]+1 - first_day_prev[index])
            task_per_next_monday_next[index] = (last_day_prev[index]+1 - first_day_prev[index])
            specific_x_original = specific_x[index]
            non_zero_indices_origin = [i for i, x in enumerate(specific_x_original) if x == 1.0]
            # Exlude the busy days relative to the index under analysis
            all_busy_days_menus_index = list(set(j for i in range(len(specific_x)) for j, value in enumerate(specific_x[i]) if value == 1 and i != index))
            all_busy_days_index = list(set(all_busy_days_menus_index + all_busy_days_prev))
            

            if first_day % 7 != days_to_monday + 1 or sum(pyomo.value(m.x[i,j]) for j in range(first_day, last_day + 1) if j not in m.weekends and j not in m.holidays_day) <= (last_day + 1 - first_day - total - 0.1) or any(index in all_busy_days_prev for index in non_zero_indices_origin):          
               
                # Prev = if we collpased the solution starting from the previous monday
                # Next = if we collpased the solution startting from the next monday
                specific_x_prev[index] = [1.0 if j in range(first_day - days_to_previous_monday, ((last_day+1) +hol_between_prev_mon_and_first_day) - (zero_days+days_to_previous_monday)) and j not in m.weekends and j not in m.holidays_day else 0.0 for j in range(1,len(specific_x_prev[index])+1)]
                if last_day + days_to_next_monday + 1 <= m.time_horizon_tot[-1]:
                    specific_x_next[index] = [1.0 if j in range(first_day + days_to_next_monday, last_day + days_to_next_monday + 1) and j not in m.weekends and j not in m.holidays_day else 0.0 for j in range(1,len(specific_x_prev[index])+1)]
                else :
                    specific_x_next[index] = specific_x_prev[index]

                # ensure the solution has n_task solution days for prev solution
                non_zero_indices_prev = [i for i, x in enumerate(specific_x_prev[index]) if x == 1.0]
                if len(non_zero_indices_prev) > task_days:
                    for it in range(task_days, len(non_zero_indices_prev)):
                        specific_x_prev[index][non_zero_indices_prev[it]] = 0.0
                    non_zero_indices_prev = [i for i, x in enumerate(specific_x_prev[index]) if x == 1.0]    

                # ensure the solution has n_task solution days for next solution
                non_zero_indices_next = [iti for iti, x in enumerate(specific_x_next[index]) if x == 1.0]
                if len(non_zero_indices_next) > task_days:
                    for itit in range(task_days, len(non_zero_indices_next)):
                        specific_x_next[index][non_zero_indices_next[itit]] = 0.0
                    non_zero_indices_next = [iti for iti, x in enumerate(specific_x_next[index]) if x == 1.0]        
                elif len(non_zero_indices_next)<task_days:
                    specific_x_next[index] = specific_x_prev[index]
                    non_zero_indices_next = [iti for iti, x in enumerate(specific_x_next[index]) if x == 1.0]

                # Prev
                first_day_prev[index] = [j for j in m.time_horizon_tot if specific_x_prev[index][j-1] == 1][0]
                last_day_prev[index] = [j for j in reversed(m.time_horizon_tot) if specific_x_prev[index][j-1] == 1][0]
                task_per_prev_monday_prev[index] = (last_day_prev[index]+1 - first_day_prev[index])

                # Next
                first_day_next[index] = [j for j in m.time_horizon_tot if specific_x_next[index][j-1] == 1][0]
                last_day_next[index] = [j for j in reversed(m.time_horizon_tot) if specific_x_next[index][j-1] == 1][0]
                task_per_next_monday_next[index] = (last_day_next[index]+1 - first_day_next[index])

                if index == 0 and counter == 0:
                    specific_x[index] = specific_x_prev[index] if task_per_prev_monday_prev[index]<=task_per_next_monday_next[index] else specific_x_next[index]
                else:
                    if task_per_prev_monday_prev[index] <= task_per_next_monday_next[index] :                        
                        if not any(index in all_busy_days_index for index in non_zero_indices_prev):
                            specific_x[index] = specific_x_prev[index]
                        elif not any(index in all_busy_days_index for index in non_zero_indices_next):
                            specific_x[index] = specific_x_next[index]
                        else:
                            if counter_overlap<=counter_overlap_max-1 and check_overlap == True:
                                print(f"\033[94mNo overlap could be solved for unit {i}\033[0m")
                                raise ValueError(f"No averlap could be solved for unit {i}")
                            else:
                                specific_x[index] = specific_x_prev[index]                         
                    else:
                        if not any(index in all_busy_days_index for index in non_zero_indices_next):
                            specific_x[index] = specific_x_next[index]
                        elif not any(index in all_busy_days_index for index in non_zero_indices_prev):
                            specific_x[index] = specific_x_prev[index]
                        else:
                            if counter_overlap<=counter_overlap_max-1 and check_overlap == True:
                                print(f"\033[94mNo overlap could be solved for unit {i}\033[0m")
                                raise ValueError(f"No averlap could be solved for unit {i}")
                            else:
                                specific_x[index] = specific_x_prev[index]

                # Update busy days
                non_zero_indices = [i for i, x in enumerate(specific_x[index]) if x == 1.0]
                all_busy_days_prev = list(set(all_busy_days_prev) | set(non_zero_indices))
            
            start_time = 0
            end_time = 0
            for j in range(len(specific_x[index])):
                if specific_x[index][j] == 1:
                    start_time = j+1
                    break
            for j in reversed(range(len(specific_x[index]))):
                if specific_x[index][j] == 1:
                    end_time = j+1
                    break
            start_end_time_dict[i] = (start_time, end_time)
            

        return specific_x, start_end_time_dict

    


