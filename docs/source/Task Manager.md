# Task Manager
This section describes a series of functions used to mamange the task, in particular, which units will perfrom the task in the current time step, which wil be the taget time to perform the task, and which will be the task range flexibility within wich the task can be performed.

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Units to perfrom the task</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>unit_todo_task</code> function is designed to return a series of elements which deals with the actual units that will perform the task in the currrent time horizon under analysis.</p>
  <p>To see the function, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Task_Manager.py#L5-L40" target="_blank" style="color: #4CAF50;">Task_Manager.unit_todo_task</a></p>

```{eval-rst}
.. autofunction:: Task_Manager.unit_todo_task
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Target Time</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>target_time</code> function is designed to return the target time to perform the task for each unit.</p>
  <p>To see the function, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Task_Manager.py#L44-L73" target="_blank" style="color: #4CAF50;">Task_Manager.target_time</a></p>

```{eval-rst}
.. autofunction:: Task_Manager.target_time
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Target Range</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>task_range</code> function is designed to return range each solution has to explore:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Task_Manager.py#L76-L135" target="_blank" style="color: #4CAF50;">Task_Manager.task_range</a></p>

```{eval-rst}
.. autofunction:: Task_Manager.task_range
```
</div>