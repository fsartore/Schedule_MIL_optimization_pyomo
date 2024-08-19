import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
###########Parameters#############

# TODO: not include this file but comment it in a specific file

standard_interval = 18             # standard interval between task in months
task_days = 10                     # number of days needed for a unit to perform a task
today = datetime(2024,1,1)         # First day of the analysis
end_year = 2027                    # End year of the analysis
task_flexibility_down = 2          # range of weeks for the solution to explore down
task_flexibility_up = 2            # range of weeks for the solution to explore up
units_partition = 1                # number of subproblems we want to have
check_overlap = False              # True: if we want to change the solution if there are overlaps, False otherwise
counter_unfeasibility_max = 60     # Max number of unfeasibility tricks to change the solution
counter_overlap_max = 4            # Max time of overlaps
standard_analysis = True           # If True, perfrom standard analysis with standard interval
check_time = False                 # True: if we want to stop the code if we reach the max time
max_time = 3*60                    # Max time for the code to find a solution
T = 7                              # days in a week
best_task_delta_days =12           # best task delta days
best_task_delta_weeks = 1          # best task delta weeks
unit_names = ['Unit 1', 'Unit 2']  # names the units as they appear in the input file