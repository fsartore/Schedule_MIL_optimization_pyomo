# Time Bounds 

This section describes a series of functions used to mamange the task, in particular, which units will perfrom the task in the current time step, which wil be the taget time to perform the task, and which will be the task range flexibility within wich the task can be performed.



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Partition Dict</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Time_Bounds.partition_dict</code> function is designed to divide the original optimization problem into multiple subproblems. In each subproblem, only a fraction of the total number of units' tasks will be optimized. After the first optimization, the subsequent ones will take into account the previous solutions to avoid overlaps. 
  This function is a key part of this optimization framework, as it allows reaching a solution using commercial solvers. Clearly, the final solution cannot be as good as the one obtained by considering the whole problem.</p>
  <p>To create the partitions, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Time_Bounds.py#L6-L33" target="_blank" style="color: #4CAF50;">Time_Bounds.partition_dict</a></p>

```{eval-rst}
.. autofunction:: Time_Bounds.partition_dict
```
</div>


<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">n_units_tuple</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Time_Bounds.n_units_tuple</code> function is designed to define a list of possible units-times couples.</p>
  <p>To create the partitions, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Time_Bounds.py#L35-L45" target="_blank" style="color: #4CAF50;">Time_Bounds.n_units_tuple</a></p>

```{eval-rst}
.. autofunction:: Time_Bounds.n_units_tuple
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">bound_dict_end</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Time_Bounds.bound_dict_end</code> function is designed to define a dictionary of tuples for the Time_Bounds of the end variables where every tuple is shifted by a given number of weeks.</p>
  <p>To create the partitions, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Time_Bounds.py#L47-L61" target="_blank" style="color: #4CAF50;">Time_Bounds.bound_dict_end</a></p>

```{eval-rst}
.. autofunction:: Time_Bounds.bound_dict_end
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">bound_dict_t</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Time_Bounds.bound_dict_t</code> function is designed to define a dictionary of tuples for the Time_Bounds of the m.t variables, representing the start and end dates.</p>
  <p>To create the partitions, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Time_Bounds.py#L63-L84" target="_blank" style="color: #4CAF50;">Time_Bounds.bound_dict_t</a></p>

```{eval-rst}
.. autofunction:: Time_Bounds.bound_dict_t
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">possible_unit_times</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Time_Bounds.possible_unit_times</code> function is designed to define a a list of possible units-times couples.</p>
  <p>To create the partitions, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Time_Bounds.py#L63-L84" target="_blank" style="color: #4CAF50;">Time_Bounds.possible_unit_times</a></p>

```{eval-rst}
.. autofunction:: Time_Bounds.possible_unit_times
```

