import os
import pickle
import pandas as pd

'''Save the data in the folder'''
def save_data_results(folder_path_base, df, final_x, start_end_time_dict, 
                      active_unit_keys_list, current_year, df_difference, dict_diff,
                      dict_unit_todotask, unit_list_name, time_horizon_tot,
                       adjusyment_tracker,
                      ):
    folder_path = os.path.join(folder_path_base, "taske_schedule_iterate")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    dir_path = f'{folder_path}/excel_schedule'    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    df.to_excel(f'{dir_path}/taske_schedule_iterate_{current_year}.xlsx')

    dir_path = f'{folder_path}/difference_target_folder'    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    df_difference.to_excel(f'{dir_path}/target_difference_{current_year}.xlsx', sheet_name=str(current_year))  

    dir_path = f'{folder_path}/dict_diff_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/dict_diff_{current_year}.pkl', 'wb') as file:
        pickle.dump(dict_diff, file) 

    dir_path = f'{folder_path}/final_x_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/final_x_{current_year}.pkl', 'wb') as file:
        pickle.dump(final_x, file)

    dir_path = f'{folder_path}/start_end_time_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/start_end_time_{current_year}.pkl', 'wb') as file:
        pickle.dump(start_end_time_dict, file) 

    dir_path = f'{folder_path}/active_unit_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/active_unit_{current_year}.pkl', 'wb') as file:
        pickle.dump(active_unit_keys_list, file)

    dir_path = f'{folder_path}/dict_unit_todotask_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/dict_unit_todotask_{current_year}.pkl', 'wb') as file:
        pickle.dump(dict_unit_todotask, file)

    dir_path = f'{folder_path}/unit_list_name_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/unit_list_name_{current_year}.pkl', 'wb') as file:
        pickle.dump(unit_list_name, file)

    dir_path = f'{folder_path}/time_horizon_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/time_horizon_{current_year}.pkl', 'wb') as file:
        pickle.dump(time_horizon_tot, file)

    dir_path = f'{folder_path}/adjusyment_tracker_folder'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'{dir_path}/adjusyment_tracker_{current_year}.pkl', 'wb') as file:
        pickle.dump(adjusyment_tracker, file)

        
'''Create the dataframe with the results'''
def fill_dataframe(df, current_x, active_unit_keys_list, days_time_hoz_list):
    # Create a mapping from numeric indices to string indices
    index_mapping_unit = {i+1: unit_key for i, unit_key in enumerate(active_unit_keys_list)}
    index_maping_time = {i+1: time for i, time in enumerate(days_time_hoz_list)}
    # Fill in the DataFrame based on the model's solution
    for i in range(1, len(current_x)+1):
        for j in range(1, len(current_x[0])+1):
            if current_x[i-1][j-1] == 1.:
                df.loc[index_mapping_unit[i], index_maping_time[j]] = 1
            elif current_x[i-1][j-1] == -0.:
                df.loc[index_mapping_unit[i], index_maping_time[j]] = 0
    return df


'''Function to load the data for the plot'''
def load_data_plot(folder_path, current_year):
    # Initialize paths for each file
    paths = {
        'dict_unit_todo_task': f'{folder_path}/dict_unit_todotask_folder/dict_unit_todotask_{current_year}.pkl',
        'unit_list_name': f'{folder_path}/unit_list_name_folder/unit_list_name_{current_year}.pkl',
        'time_horizon_tot': f'{folder_path}/time_horizon_folder/time_horizon_{current_year}.pkl',
        'result_path': f'{folder_path}/excel_schedule/taskenance_schedule_iterate_{current_year}.xlsx'
    }
    
    # Initialize a dictionary to hold the loaded data
    data = {}
    
    # Iterate over each item in paths to load the data if the file exists
    for key, path in paths.items():
        if key != 'result_path':
            if os.path.exists(path):
                with open(path, 'rb') as file:
                    data[key] = pickle.load(file)
            else:
                print(f'File {path} does not exist.')
                data[key] = None  # Or handle missing file as needed
        else:
            if os.path.exists(path):
                df = pd.read_excel(path)  # Corrected variable from result_path to path
                df.set_index(df.columns[0], inplace=True)
                data[key] = df
            else:
                print(f'File {path} does not exist.')
                data[key] = None
    
    return data