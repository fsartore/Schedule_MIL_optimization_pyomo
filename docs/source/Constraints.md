# Constraints


<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Constraints</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints</code> code is the key code for this optimization framework.
  It provides all the equations used to contrain the optimization setup. In particular, m_init_rule and m_end rule are highly performance equations designed to limit the search space within the flexibility range provided by the user. All the equations deal with mix integer linear variables. :</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints" target="_blank" style="color: #4CAF50;">Constraints</a></p>


</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">end_after_start_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>read_previous_task.iterate_start_end_dates</code> function is designed to create a list of tuples with the start and end dates of the tasks for every year in the time horizon.</p>
  <p>To create the start and end times tuples, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/read_previous_task.py#L25-L40" target="_blank" style="color: #4CAF50;">read_previous_task.iterate_start_end_dates</a></p>

```{eval-rst}
.. autofunction:: read_previous_task.iterate_start_end_dates
```
</div>