
# Parameters

<div style="border: 1px solid green; padding: 10px; background-color: #d4edda; color: #155724;">
  <strong>Note:</strong> Define the parameters according to your own setup in <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Parameters.py#L6-L22" target="_blank">`Parameters`</a> .py doc.
</div>


| Parameter                | Description                                                                 | Type                |
|--------------------------|-----------------------------------------------------------------------------|---------------------|
| **standard_interval**    | Standard interval between tasks in months.                                  | `int`               |
| **task_days**            | Number of days needed for a unit to perform a task.                         | `int`               |
| **today**                | First day of the analysis.                                                  | `str` or `datetime-like` |
| **end_year**             | End year of the analysis.                                                   | `int`               |
| **task_flexibility_down**| Range of weeks for the solution to explore down.                            | `int`               |
| **task_flexibility_up**  | Range of weeks for the solution to explore up.                              | `int`               |
| **units_partition**      | Number of subproblems we want to have.                                      | `int`               |
| **check_overlap**        | `True`: If we want to change the solution if there are overlaps. `False`: Otherwise. | `bool`              |
| **counter_unfeasibility_max** | Max number of unfeasibility tricks to change the solution.             | `int`               |
| **counter_overlap_max**  | Max times of overlaps, before forcing the exit.                             | `int`               |
| **check_time**           | `True`: If we want to stop the code if we reach the max time. `False`: Otherwise. | `bool`              |
| **max_time**             | Max time for the code to find a solution (in seconds).                      | `int`               |
| **T**                    | Days in a week, 7. In case of a different value, the code will not work, and need to be modified accordingly. | `int`               |
| **best_task_delta_days** | Minimum number of days to perform a task.                                   | `int`               |
| **best_task_delta_weeks**| Minimum number of weeks to perform a task.                                  | `int`               |
| **unit_names**           | Names of the units as they appear in the input file, provide a list.        | `list of str`       |

## Define Folder Paths

<div style="border: 1px solid green; padding: 10px; background-color: #d4edda; color: #155724;">
  <strong>Note:</strong> Change the folder paths according to your own setup in <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Directories.py#L4-L7" target="_blank">`Directories`</a> .py doc.
</div>


| Parameter              | Description                                          | Example                                      |
|------------------------|------------------------------------------------------|----------------------------------------------|
| **folder_path_results**| Folder path to save results.                         | `C:\...\Optimization_tests_results`          |
| **folder_path_input**  | Folder path to read input data.                      | `C:\...\Optimization_tests\Input`            |
| **figures_path**       | Folder path to save figures.                         | `C:\...\Optimization_tests_results\Figures`  |
| **last_task_path**     | Folder path to read last task data in consecutive runs. | `C:\...\Historic_data\Dados`                |

