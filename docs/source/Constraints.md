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
  <p>The <code>Constraints.Constraints_maintenace.end_after_start_rule</code> function is designed to set the end time after the start time.</p>
  <p>To read the end_after_start_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L13-L25" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.end_after_start_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.end_after_start_rule
```
</div>

<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">m_init_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the m_init_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L28-L43" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.m_init_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.m_init_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">m_end_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the m_end_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L45-L60" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.m_end_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.m_end_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">m_weekend_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the m_weekend_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L62-L76" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.m_weekend_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.m_weekend_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">holidays_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the holidays_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L78-L92" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.holidays_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.holidays_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">zero_init_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the zero_init_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L94-L109" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.zero_init_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.zero_init_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">zero_end_rule</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the zero_end_rule constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L111-L126" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.zero_end_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.zero_end_rule
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">task</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the task constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L128-L145" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.task</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.task
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">no_overlap</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the no_overlap constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L147-L159" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.no_overlap</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.no_overlap
```
</div>



<div style="border: 2px solid #4CAF50; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
  <h2 style="color: #4CAF50;">busy_days</h2>
  <p><strong>Overview:</strong></p>
  <p>To read the busy_days constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L161-L175" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.busy_days</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.busy_days
```
</div>