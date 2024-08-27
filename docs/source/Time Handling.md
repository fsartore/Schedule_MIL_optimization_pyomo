# Time Handling

This section describes a series of functions used to handle the time in the optimization model. In particular, it describes how to create diferent time elements. Most of them are very basic function, whose name is self-explanatory. You can fine them in the <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/time_handling.py" target="_blank" style="color: #4CAF50;">time_handling</a> file. We will focus on two functions, which are more complex and are used to define the holidays list, which is an important user input in the optimization model to be defined according to the user's needs. The second funtion is meant to handle the model in case of wrong solutions, so that it can return a correct solution.



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Holidays list</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>time_handling.TimeHandling.generate_holidays_days_list</code> function is designed to define a customized list of days where the task cannot be performed.</p>
  <p>To see the function, you can use the following link:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/time_handling.py#L25-L43" target="_blank" style="color: #4CAF50;">time_handling.TimeHandling.generate_holidays_days_list</a></p>

```{eval-rst}
.. autofunction:: time_handling.TimeHandling.generate_holidays_days_list
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Handle Wrong Solution</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>time_handling.TimeHandling.modify_task_schedule</code> function is designed to handle wrong solutions.</p>
  <p>To see the function, you can use the following link:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/time_handling.py#L79-L247" target="_blank" style="color: #4CAF50;">time_handling.TimeHandling.modify_task_schedule</a></p>

```{eval-rst}
.. autofunction:: time_handling.TimeHandling.modify_task_schedule
```