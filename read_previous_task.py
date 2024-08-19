import pandas as pd


class ReadLasttask:
    def __init__(self, units_names, last_task_path,  today):
        self.unit_names = units_names
        self.data_path = last_task_path
        self.today = today
        self.last_task_time = self.read_last_task()[0]
        self.last_task_type = self.read_last_task()[1]

    def read_last_task(self):
        '''Implement according to your data
        
        :returns:
            - last_task_dict_time: dictionary with the last time the task was held for each unit
            - last_task_dict_year: dictionary with the last year the task was held for each unit
        '''
        last_task_dict_time = {}
        last_task_dict_year = {}
        
        return last_task_dict_time,  last_task_dict_year
    

def iterate_start_end_dates(today, current_year_list):
    '''
    Iterate over the start and end dates for the time horizon under analysis.
    It returns a list of start dates and a list of end dates.
    Specifically, the start date is the current date and the end date is the first day of the next year.
    From the second year onwards, the start date is the first day of the year and the end date is the first day of the next year.
    :param today: current date
    :param current_year_list: list of years in the time horizon under analysis
    :returns:
        - start_date_list: list of start dates
        - end_date_list: list of end dates
    '''
    today_timestamp = pd.to_datetime(today)
    start_date_list = [today_timestamp] + [pd.to_datetime(f'{year}-01-01') for year in current_year_list[1:]]
    end_date_list = [pd.to_datetime(f'{today.year + 1}-01-01')] + [pd.to_datetime(f'{int(year) + 1}-01-01') for year in current_year_list[1:]]
    return start_date_list, end_date_list


   
