# Example
This code serves to illustrate the use of the `pyomo` library to solve a simple optimization problem. The problem is to optimize the schedule of 15 workers in a factory. The workers work 15 days to complete a task. Each task must be completed by a single worker. Each task must be completed in 15 consecutive working days. After one task is completed, each worker will perform another task after 16 months. Only one task can be completed at the same time. The first day of the analysis is 01/01/2024. We aim to optimize the schedule until the end of 2026. Every worker has a flexibility window of 6 weeks to perform the task. The last time each worker performed the task can be read in the `C:..\Schedule_MIL_optimization_pyomo\Historic_data\Data\last_task_data.xlsx`. The workers cannot operate on weekends and during holidays, which are stored in the file `C:..\Schedule_MIL_optimization_pyomo\Optimization_tests\Input\holidays.xlsx`.
The goal is to produce a schedule that minimizes the overall time of task completion. The optimization is against the calendar constraints, like weekends and holidays.
To run this example, the files in the `Example` folder : `C:\Users\Asus\Desktop\ITAIPU\Schedule_MIL_optimization_pyomo\Example`  
must be copied to the root directory of the project, and their names must be changed to the same name as the original files.

Once the files are copied, the code can be run by executing the following command from the root directory of the project:

```python
python Scheduling_task_multiyear.py
```