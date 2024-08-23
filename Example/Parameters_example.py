import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
###########Parameters#############

standard_interval = 15              # standard interval between task in months
task_days = 15                      # number of days needed for a unit to perform a task
today =  datetime(2024,1,1)         # First day of the analysis
end_year = 2028                     # End year of the analysis
task_flexibility_down = 5           # range of weeks for the solution to explore down
task_flexibility_up = 5             # range of weeks for the solution to explore up
units_partition = 4                 # number of subproblems we want to have
check_overlap = False               # True: if we want to change the solution if there are overlaps, False otherwise
counter_unfeasibility_max = 40      # Max number of unfeasibility tricks to change the solution
counter_overlap_max = 2             # Max time of overlaps
check_time = None                   # True: if we want to stop the code if we reach the max time
max_time = 10*60                    # Max time for the code to find a solution
T = 7                               # days in a week
best_task_delta_days =  20          # best task delta days
best_task_delta_weeks = 3           # best task delta weeks
unit_names = [
    'Worker 01', 
    'Worker 02', 
    'Worker 03', 
    'Worker 04', 
    'Worker 05', 
    'Worker 06', 
    'Worker 07', 
    'Worker 08', 
    'Worker 09', 
    'Worker 10', 
    'Worker 11', 
    'Worker 12', 
    'Worker 13', 
    'Worker 14', 
    'Worker 15'
]                     # names the units as they appear in the input file