# Handling Unfeasibility

This section describes a series of functions used to handle unfeasibility in the optimization model.
Sometimes, due to the overlap of the search space of different unit's task, the solution might be infeasible. In this case, the optimization model will return an error. To handle this, the optimization model can be slightly modified to have the most valuable sub-optimal and feasible solution. In particular, this modifications regard small adjustments of the task range, perfromed in the smartest way possible, namely with the smallest possible number of changes.

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Handle Unfeasibility</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>handle_unfeasibility</code> function is designed as the main function to handle unfeasibility in the optimization model.</p>
  <p>To see the function, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/handling_unfeasibility.py#L3-L49" target="_blank" style="color: #4CAF50;">handling_unfeasibility.handle_unfeasibility</a></p>

```{eval-rst}
.. autofunction:: handling_unfeasibility.handle_unfeasibility
```

</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Adjust Task Range</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>adjust_values_to_reduce_crowding</code> function is designed to change the task range in the smartest way to make the model both feasible and close to the original optimization problem.</p>
  <p>To see the function, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/handling_unfeasibility.py#L52-L193" target="_blank" style="color: #4CAF50;">handling_unfeasibility.adjust_values_to_reduce_crowding</a></p>

```{eval-rst}
.. autofunction:: handling_unfeasibility.adjust_values_to_reduce_crowding
```

</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Desperate Adjust</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>desperate_adjust_target_week</code> function is designed to randomly change the task range. This function is used as the last hope to find a feasible solution. Its use is reccomended only in case a feasible solution must be found at any cost</p>
  <p>To see the function, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/handling_unfeasibility.py#L195-L244" target="_blank" style="color: #4CAF50;">handling_unfeasibility.desperate_adjust_target_week</a></p>

```{eval-rst}
.. autofunction:: handling_unfeasibility.desperate_adjust_target_week
```

</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Adjust Bounds</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>adjusted_bound_dict_init</code> function is designed to reconstruct the bounds in case they have been modified during an adjustment due to unfeasibility</p>
  <p>To see the function, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/handling_unfeasibility.py#L47-L268" target="_blank" style="color: #4CAF50;">handling_unfeasibility.adjusted_bound_dict_init</a></p>

```{eval-rst}
.. autofunction:: handling_unfeasibility.adjusted_bound_dict_init
```