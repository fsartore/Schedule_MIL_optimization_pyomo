import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import Directories as dir
import matplotlib.patches as mpatches
from time_handling import TimeHandling
from Parameters import  task_flexibility_down, task_flexibility_up, units_partition
from read_previous_task import ReadLasttask
from Parameters import unit_names, today,  end_year
from elaborate_and_save_data import load_data_plot

'''Define directories and classes instances'''
current_year_list = [str(today.year + i) for i in range(end_year - today.year + 1)] 
print('current_year_list:', current_year_list)
last_task_path = dir.last_task_path
file_path_input =  dir.folder_path_input
current_year_list = current_year_list
time_handling_instance = TimeHandling(current_year_list, file_path_input,today)
previous_year_list = time_handling_instance.uniterate_previous_year_list()
start_date_list, end_date_list = time_handling_instance.uniterate_start_end_dates()
holidays_days_list = time_handling_instance.uniterate_holidays_days_list()
last_task_instance = ReadLasttask(unit_names, last_task_path, today)
folder_path_base =  dir.folder_path_base
folder_path = os.path.join(folder_path_base, "task_schedule_iterate")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_path_input =  dir.folder_path_input

# Initialize
year_counter_max = len(previous_year_list)
year_flag = True
year_counter = 0
n_units_history = []
unit_list_name = unit_names    

while year_flag == True:

    '''Actualize time_depending variables'''
    previous_year = previous_year_list[year_counter]
    current_year = current_year_list[year_counter]
    start_date = start_date_list[year_counter]
    end_date = end_date_list[year_counter]   
  
    print(f'\n\n\n Year: {current_year} \n\n\n')

    loaded_data = load_data_plot(folder_path, current_year)  # function to load all the usefull solutions
    dict_unit_todo_task = loaded_data['dict_unit_todo_task']
    unit_list_name = loaded_data['unit_list_name']
    time_horizon_tot = loaded_data['time_horizon_tot']
    df = loaded_data['result_path']
    # Ensure unit_list_name is a set
    unit_list_name_set = set(unit_list_name)   
    # Convert dict_unit_todo_task.keys() to a set
    dict_unit_todo_task_keys_set = set(dict_unit_todo_task.keys())   
    # Perform the set difference operation
    unit_not_to_do_task = unit_list_name_set.difference(dict_unit_todo_task_keys_set)    
    # If you need the result as a list (for further operations that require list instead of set)
    unit_not_to_do_task_list = list(unit_not_to_do_task)



    # add to df also the units that are not in the last task list and order them sequentially
    for unit in unit_list_name:
        if unit not in df.index:
            df.loc[unit] = 0   
    df = df.reindex(unit_list_name)  # order it correctly

    # dictonary with the days of difference with regards to the target solution
    with open(f'{folder_path}/dict_diff_folder/dict_diff_{current_year}.pkl', 'rb') as file:
        dict_diff = pickle.load(file)
    for unit in unit_list_name:
        if unit  not in dict_diff.keys():
            dict_diff[unit] = 0
    dict_diff = {key: dict_diff[key] for key in unit_list_name if key in dict_diff}
    print(dict_diff)     
              
              
    '''PLOT'''

    # Create the heatmap
    plt.figure(figsize=(100, 50 ))
    # Draw the heatmap first
    sns.heatmap(df, cmap='YlOrBr', cbar=False, linewidths=0.05, linecolor='gray')  
    # Define a custom colormap from green to rose


    # Assuming dict_unit_to_be_tasktained is your dictionary
    dict_unit_to_be_task_keys = dict_unit_todo_task.keys()

    # Get current axis
    ax = plt.gca()

    # Retrieve current y-axis tick labels
    current_labels = [label.get_text() for label in ax.get_yticklabels()]

    # Set y-axis labels (this step might be redundant if labels are already set by seaborn)
    ax.set_yticklabels(current_labels)

    # Now, iterate over the labels and set the color conditionally
    for label in ax.get_yticklabels():
        if label.get_text() in dict_unit_to_be_task_keys:
            label.set_color('green')


    # Define a set for holidays
    holidays_list = time_handling_instance.holidays_in_time_horizon(start_date, end_date, year_counter) 
    weekends = time_handling_instance.weekend_set(start_date,time_horizon_tot)
    # Draw the colored spans for holidays and weekends
    for i in range(len(unit_list_name)):
        for j in range(time_horizon_tot):                   
            if  j in holidays_list:
                plt.axhspan(0, len(unit_list_name), xmin=(j-0.9)/time_horizon_tot, xmax=(j-0.1)/time_horizon_tot, 
                            facecolor=(0.804, 0.361, 0.361), alpha=1)
            if j in weekends:
                plt.axhspan(0, len(unit_list_name), xmin=(j-0.9)/time_horizon_tot, 
                            xmax=(j-0.1)/time_horizon_tot, facecolor=(0, 0, 0, 0.6))   
    # Create patches for the leunitd
    red_patch = mpatches.Patch(color='indianred', label='Holidays')
    black_patch = mpatches.Patch(color='black', label='Weekends')

    # Add the leunitd to the plot
    plt.leunitd(handles=[red_patch, black_patch],
                loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=50)
    plt.xlabel('Time', fontsize=100, labelpad=70)
    plt.ylabel('units', fontsize=100, labelpad=150)
    plt.title(f'task Schedule {current_year}', fontsize=100, pad=150, fontweight='bold')
    # Make the y-ticks larger
    plt.yticks(fontsize=42)
    # Create a secondary y-axis
    sec_ax = plt.gca().twinx()
    # Map dict_diff values to the y-ticks positions
    dict_diff_values = [dict_diff[key] for key in reversed(unit_list_name)]  # Assuming df.index and dict_diff keys match
    # uniterate evenly spaced numbers over the y-axis interval
    tick_positions = np.linspace(start=0, stop=len(df.index)-1, num=len(df.index))
    # Set the secondary y-axis tick positions and labels
    sec_ax.set_yticks(tick_positions)
    sec_ax.set_yticklabels(dict_diff_values, fontsize=60)  # Adjust fontsize as needed
    # Align the secondary y-axis limit with the primary y-axis
    sec_ax.set_ylim(-0.5, len(df.index)-0.5)
    # Move the secondary y-axis to the right
    sec_ax.yaxis.tick_right()
    sec_ax.yaxis.set_label_position('right')

    sec_ax.set_ylabel('Target difference',fontsize=100, labelpad=150)


    # Color the y-tick labels based on their values
    for label, value, key in zip(sec_ax.get_yticklabels(), dict_diff_values, reversed(unit_list_name)):
        if key in unit_not_to_do_task_list:
            label.set_color('black')
        elif abs(value) <= 14:
            label.set_color('green')
        elif 14 < abs(value) <= 35:
            label.set_color('orange')
        else:
            label.set_color('red')

    '''Save the figure'''
    figure_path = dir.figures_path
    down= str(task_flexibility_up)
    up = str(task_flexibility_down)
    dir_path = os.path.join(figure_path, str(today.date()) + '---' + str(end_year)+'-unit_part--'+ str(units_partition))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, f'task_schedule_{current_year}.png')
    plt.savefig(file_path)

    '''Update the year'''
    year_counter = year_counter + 1
    if year_counter == year_counter_max:
        year_flag = False




