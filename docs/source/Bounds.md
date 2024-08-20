# Bounds

In this section, we will discuss the functions that are used to define the bounds of the optimization problem. The bounds are used to define the minimum and maximum values that the decision variables can take. The bounds are defined in the <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Bounds.py" target="_blank" style="color: #4CAF50;">`Bounds`</a> .py doc.



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Partition Dict</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>read_previous_task.iterate_start_end_dates</code> function is designed to create a list of tuples with the start and end dates of the tasks for every year in the time horizon.</p>
  <p>To create the start and end times tuples, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Bounds.py" target="_blank" style="color: #4CAF50;">Bounds.partition_dict</a></p>

```{eval-rst}
.. autofunction:: read_previous_task.iterate_start_end_dates
```