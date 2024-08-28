# Constraints


<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">Constraints</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints</code> code is the key code for this optimization framework.
  It provides all the equations used to contrain the optimization setup. In particular, m_init_rule and m_end rule are highly performance equations designed to limit the search space within the flexibility range provided by the user. All the equations deal with mix integer linear variables. :</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints" target="_blank" style="color: #4CAF50;">Constraints</a></p>


<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">End After Rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.end_after_start_rule</code> function is designed to set the end time after the start time.</p>
  <p>To read the end_after_start_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L13-L25" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.end_after_start_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.end_after_start_rule
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">m_init_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.m_init_rule</code> function defines a rule that ensures the decision variable <code>x[i,j]</code>
     is set to 0 for days before the initial time for a given index pair <code>t(i, j)</code>
     and can assume the boolean value 1 for days after the initial time.
     The time variable <code>t[i][j]</code> must be greater than or equal to the initial time,
     decided by the decision variable start time <code>tstart[i]</code> at week <code>j</code>.</p>
  <p>To read the <code>m_init_rule</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L28-L43" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.m_init_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.m_init_rule
```
</div>


<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">m_end_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.m_end_rule</code> function defines a rule that ensures the decision variable <code>x[i,j]</code>
     is set to 0 for days after the end time for a given index pair <code>t(i, j)</code>
     and can assume the boolean value 1 for days before the end time.
     The time variable <code>t[i][j]</code> must be less than or equal to the end time,
     decided by the decision variable end time <code>tend[i]</code> at week <code>j</code>.</p>
  <p>To read the <code>m_end_rule</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L45-L60" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.m_end_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.m_end_rule
```
</div>


<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">m_weekend_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.m_weekend_rule</code> function defines a rule that ensures no activity <code>x[i,j]</code>
     is scheduled on weekends for a given index pair <code>(i, j)</code> in the model <code>m</code>.</p>
  <p>To read the <code>m_weekend_rule</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L62-L76" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.m_weekend_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.m_weekend_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">holidays_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.holidays_rule</code> function defines a rule that ensures no activity <code>x[i,j]</code>
     is scheduled on holidays for a given index pair <code>(i, j)</code> in the model <code>m</code>.</p>
  <p>To read the <code>holidays_rule</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L78-L92" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.holidays_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.holidays_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">zero_init_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.zero_init_rule</code> function is designed to set the initial value of the decision variable to zero.</p>
  <p>To read the <code>zero_init_rule</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L94-L109" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.zero_init_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.zero_init_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">zero_end_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.zero_end_rule</code> function defines a rule that ensures the activity variable <code>x[i,j]</code>
     is set to 0 for days before the initial time for a given index pair <code>(i, j)</code>
     in the model <code>m</code>.</p>
  <p>To read the <code>zero_end_rule</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L111-L126" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.zero_end_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.zero_end_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">task</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.task</code> function defines a rule that ensures the activity variable <code>x[i,j]</code>
     is set to 0 for days beyond the end time for a given index pair <code>(i, j)</code> in the model <code>m</code>.</p>
  <p>To read the <code>task</code> constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L128-L145" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.task</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.task
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">no_overlap</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.no_overlap</code>         This function defines a rule that ensures no overlapping activities 
        for a given index (day) j in the model m. It ensures that at most one 
        activity can be scheduled at the same time.</p>
  <p>To read the <code>no_overlap constraint</code>, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L147-L159" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.no_overlap</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.no_overlap
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">busy_days</h2>
  <p><strong>Overview:</strong></p>
  <p>The <code>Constraints.Constraints_task.busy_days</code>         This function defines a rule that ensures no activity (x[i,j]) 
        is scheduled on busy days for a given index pair (i, j) in the model m.</p>
  <p>To read the <code>busy_days constraint</code>, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L161-L175" target="_blank" style="color: #4CAF50;">Constraints.Constraints_task.busy_days</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_task.busy_days
```
</div>