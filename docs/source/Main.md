# Main

This is the main file that runs the MIL optimization.
It is the file that is called by the user to run the optimization. 

<p>To access the main function, you can follow this link:</p>
<p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_task_multiyear.py" target="_blank" style="color: #4CAF50;">Scheduling_task_multiyear</a></p>

![Optimization Process Description](../../Code_scheme.png)
*Figure 1: Optimization Process Description*

<div style="border: 1px solid green; padding: 10px; background-color: #fff3cd; color: #856404;">
  <strong>Note:</strong> The main function will not run until the <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Parameters.py#L6-L22" target="_blank">`Parameters.py`</a> doc and <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Directories.py#L4-L7" target="_blank">`Directories.py`</a> code are not properly set up according to the user's needs.
</div></p>


The specific functions are described in the specific Contents section: 


1. {doc}`Pyomo Optimization Model`: This section describes the optimization model used in the package.
2. {doc}`Constraints`: This section describes the constraints used in the optimization model.
3. {doc}`Parameters`: This section describes the parameters used in the optimization model.
4. {doc}`Time Bounds`: This section describes the bounds used in the optimization model.
5. {doc}`Read Previous Tasks`: This section describes how to read the previous task, to further optimize the schedule.
6. {doc}`Task Manager`: This section describes a series of functions used to manage the task.
7. {doc}`Time Handling`: This section describes a series of functions used to handle the time in the optimization model.

When the <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py" target="_blank" style="color: #4CAF50;">main</a> runs, an unfeasible solution can be produced, therefore we have a specific section to handle this issue:

9. {doc}`Handling Unfeasibility`: This section describes how to handle unfeasibility in the optimization model.

Once obtained a solution, we can save the results in a specific file: 

10. Please, note that at line  <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.pyL167" target="_blank" style="color: #4CAF50;">267</a>
there is a function that saves the different results. You can find further datails in :<p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/elaborate_and_save_data.py" target="_blank" style="color: #4CAF50;">Elaborate and Save results</a></p>The code is very easy and self-explanatory. It can be costumized according to the user's needs. 

Eventually, a plot can be produced to visualize the results:

11. {doc}`Plot Results`: This section describes how to plot the results of the optimization model.

To run an example code, you can follow this link:

12. {doc}`Example`: This section describes an example code that can be run to test the optimization model.





