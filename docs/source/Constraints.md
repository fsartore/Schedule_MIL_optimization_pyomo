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
  <p>To create the constraint, you can use the following function:</p>
  <p><a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Constraints.py#L13-L25" target="_blank" style="color: #4CAF50;">Constraints.Constraints_maintenace.end_after_rule</a></p>

```{eval-rst}
.. autofunction:: Constraints.Constraints_maintenace.end_after_rule
```
</div>