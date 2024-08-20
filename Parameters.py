import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
###########Parameters#############

standard_interval = None              # standard interval between task in months
task_days = None                      # number of days needed for a unit to perform a task
today = None                          # First day of the analysis
end_year = None                       # End year of the analysis
task_flexibility_down = None          # range of weeks for the solution to explore down
task_flexibility_up = None            # range of weeks for the solution to explore up
units_partition = None                # number of subproblems we want to have
check_overlap = None                  # True: if we want to change the solution if there are overlaps, False otherwise
counter_unfeasibility_max = None      # Max number of unfeasibility tricks to change the solution
counter_overlap_max = None            # Max time of overlaps
standard_analysis = None              # If True, perform standard analysis with standard interval
check_time = None                     # True: if we want to stop the code if we reach the max time
max_time = None                       # Max time for the code to find a solution
T = None                              # days in a week
best_task_delta_days = None           # best task delta days
best_task_delta_weeks = None          # best task delta weeks
unit_names = None                     # names the units as they appear in the input file