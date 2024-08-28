# Time Handling

This section describes a series of functions used to handle the time in the optimization model. In particular, it describes how to create diferent time elements. Most of them are very basic function, whose name is self-explanatory. You can fine them in the <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/time_handling.py" target="_blank" style="color: #4CAF50;">time_handling</a> file. We will focus on two functions, which are more complex and are used to define the holidays list, which is an important user input in the optimization model to be defined according to the user's needs. The second funtion is meant to handle the model in case of wrong solutions, so that it can return a correct solution.



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Holidays List</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>time_handling.TimeHandling.generate_holidays_days_list</code> function generates a list of holidays for each year in the time horizon under analysis.
     To perform this task, the function reads the holidays from an Excel file.
     The Excel file must have a sheet named 'Feriados' with the following columns:
     - year 2020, year 2021, year 2022, ...
     Each row represents a holiday.
     If a holiday is not present in a year, the cell must be empty.</p>
  <p>To see the function, you can use the following link:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/time_handling.py#L25-L43" target="_blank" style="color: #4CAF50;">time_handling.TimeHandling.generate_holidays_days_list</a></p>

```{eval-rst}
.. autofunction:: time_handling.TimeHandling.generate_holidays_days_list
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Handle Wrong Solution</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>time_handling.TimeHandling.modify_task_schedule</code> function modifies the task schedule to make it feasible.
     This is a complex function that adjusts the solution to be feasible, avoids overlaps, makes the first day Monday,
     and ensures that the task days are consecutive.</p>
  <p>Three checks:</p>
  <ol>
    <li>First day is not Monday</li>
    <li>The task days are not consecutive</li>
    <li>The solution overlaps with other solutions</li>
  </ol>
  <p>Update <code>specific_x</code>, the current solution, depending on the quality of the modified solutions.</p>
  <p><strong>Criteria:</strong></p>
  <ol>
    <li>Favor the solution with fewer task days to improve availability</li>
    <li>Avoid overlaps</li>
  </ol>
  <p><strong>Actions:</strong></p>
  <ol>
    <li>If all good, update <code>specific_x</code></li>
    <li>Raise a value error to activate unfeasible tricks to better distribute the target times</li>
    <li>If close to the last unfeasible tricks, accept an overlap solution</li>
  </ol>
  <p>To see the function, you can use the following link:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/time_handling.py#L79-L247" target="_blank" style="color: #4CAF50;">time_handling.TimeHandling.modify_task_schedule</a></p>

```{eval-rst}
.. autofunction:: time_handling.TimeHandling.modify_task_schedule
```