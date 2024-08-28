# Read Previous Tasks

This section describes a series of functions used to read the previous task data.

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Iterate Start and End Dates</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Read_previous_tasks.iterate_start_end_dates</code> function iterates over the start and end dates for the time horizon under analysis.
     It returns a list of start dates and a list of end dates.
     Specifically, the start date is the current date and the end date is the first day of the next year.
     From the second year onwards, the start date is the first day of the year and the end date is the first day of the next year.</p>
  <p>To create the start and end times tuples, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Read_previous_tasks.py#L25-L40" target="_blank" style="color: #4CAF50;">Read_previous_tasks.iterate_start_end_dates</a></p>

```{eval-rst}
.. autofunction:: Read_previous_tasks.iterate_start_end_dates
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Read Last Task</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Read_previous_tasks.ReadLasttask.read_last_task</code> function is designed to read the last task data for each unit.</p>
  <p>To read the last task data, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Read_previous_tasks.py#L19-L20" target="_blank" style="color: #4CAF50;">Read_previous_tasks.ReadLasttask.read_last_task</a></p>

```{eval-rst}
.. autofunction:: Read_previous_tasks.ReadLasttask.read_last_task
```
