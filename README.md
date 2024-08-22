# Welcome to  MIL Schedule Optimization with Pyomo's documentation!

This is a guide to the MIL Schedule Optimization with Pyomo package. This package is designed to help you optimize your task schedule using a mix-integer linear optimization model with Pyomo for Python.  It best suits problems where the tasks are repetitive, one task is performed at a time, and the tasks have a fixed duration.This optimization model is primarily designed for maintenance scheduling, but it can be adapted to other scheduling problems. The optimiziation is against a set of calendar constraints, such as working hours, weekends, and holidays, which are defined by the user. The key feature of the model is its ability to split the whole optimization into smaller optimization problems, which are solved sequentially. This allows the model to be used for large-scale optimization problems, for real-time optimization, and for optimization with limited computational resources. The package is designed to be user-friendly with the possibility to customize the optimization model. Another important feature of the model is it's ability to handle unfeasible solutions, slightly modifying the optimization model to have the most valuable sub-optimal and feasible solution. The package is open-source and can be used for free. The package is designed to be used by engineers, researchers, and students who want to optimize their task schedule using a mix-integer linear optimization model with Pyomo. In the model we will refer to the task as "task" and to the component performing the task as "unit". 
This guide was written by Federico Sartore, an ETH student in Energy Science and Technology Master. For more information, please contact @fsartore on GitHub or by mail fsartore@student.ethz.ch.






