# Pyomo Optimization Model

This section describes the optimization model used in the package using Pyomo language.

Given the model:
```python
m = pyo.ConcreteModel()
```

## Sets
Sets are used indexed sets of objects, used to constrain the range of variables and parameters. 
The model uses the following sets:
| Variable                                                                                                      | Description                                                                                     |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L138" target="_blank" style="color: #4CAF50;">m.n_unit_element</a> | used to define a set of units names                                                             |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L139" target="_blank" style="color: #4CAF50;">m.t</a> | used to define a set of time steps, namely the time steps of the optimization                   |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L142" target="_blank" style="color: #4CAF50;">m.NN</a> | used to define a set for possible units-times couples                                           |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L143" target="_blank" style="color: #4CAF50;">m.weekends</a> | used to define a set for weekends                                                              |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L144" target="_blank" style="color: #4CAF50;">m.holiday_day</a> | used to define a set for holidays or days the tasks cannot be performed                         |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L145" target="_blank" style="color: #4CAF50;">m.time_horizon_tot</a> | used to define a set for the total time horizon of the optimization                             |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L151" target="_blank" style="color: #4CAF50;">m.init_times</a> | used to define a set for the initial time of different tasks                                    |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L154" target="_blank" style="color: #4CAF50;">m.end_times</a> | used to define a set for the end time of different tasks                                        |

## Variables
Variables are used to define the decision variables of the optimization problem.
The model uses the following variables:
| Variable                                                                                                      | Description                                                                                     |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L157" target="_blank" style="color: #4CAF50;">m.x</a> | used as a binary variable for the optimization problem, where 1 means the task is performed that day and 0 means the task is not performed that day. It searches for in the whole time horizon. |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L158" target="_blank" style="color: #4CAF50;">m.tstart</a> | used as a NonNegative Integer variable for the optimization problem, where it defines the start week of the task. This is restricted by a bound defined by the user, to limit the search space. |
| <a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L159" target="_blank" style="color: #4CAF50;">m.tend</a> | used as a NonNegative Integer variable for the optimization problem, where it defines the end week of the task. This is restricted by a bound defined by the user, to limit the search space. |

## Model Constraints
Please refer to the {doc}`Constraints` section for more information.



## Objective Function
The objective function is used to define the optimization goal.
The model uses the following objective function:

<div style="background-color: #e6ffe6; padding: 10px;">
<a href="https://github.com/fsartore/Schedule_MIL_optimization_pyomo/blob/main/Scheduling_maintenance_multiyear.py#L185" target="_blank" style="color: #4CAF50;">obj_expr</a> = 

```{math}
\sum_{i \in m.n\_units} \left( m.tend[i] \cdot T - \left( (m.tstart[i] - 1) \cdot T + 1 \right) \right)
```
</div>


The objective function is to minimize the difference between the end time and the start time of the task, for all the tasks, given the constraints.
To define the objective function, you can use the following code:



```python
m.objective = pyomo.Objective(expr = obj_expr, sense=pyomo.minimize)
```

## Solving the Model
To solve the model, you first have to define the solver you want to use:



Then, you can solve the model using the following code:

```python
result = solver.solve(m)
```
To retrive the objective function value, you can use the following code:


```python
objective = += pyomo.value(m.objective)
```

