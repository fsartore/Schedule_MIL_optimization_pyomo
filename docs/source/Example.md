# Example
This code serves to illustrate the use of the `pyomo` library to solve a simple optimization problem. The problem is to optimize the schedule of 15 workers in a factory. The workers work 15 days to complete a task. Each task must be completed by a single worker. Each task must be completed in 15consecutive working days. One single task can be completed at the same time. The first day of the analysisi is 01/01/2024. We aim to optimize the schedule till the end of 2028. Every worker has a flexibility window of 10 weeks to perform the task. The last time each workers perdormed the task can be read in the C:..Schedule_MIL_optimization_pyomo\Historic_data\Data\last_task_data.xlsx. The workers cannot operate at weekend and during holidays, which are stored in the file C:..\Schedule_MIL_optimization_pyomo\Optimization_tests\Input\holidays.xlsx.
The goal is to produce a schedule that minimizes the overall time of the task completion. The optimiziation is against the calendar constraints, like weekend and hlidays. 
To run this example, the files in the Example folder must be copied to the root directory of the project, and their name must be changed to the same name as the original files.

Once the files are copied, the code can be run by executing the following command from the root directory of the project:

```python
python Scheduling_task_multiyear.py
```