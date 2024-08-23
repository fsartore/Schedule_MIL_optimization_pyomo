import pyomo.environ as pyomo


class Constraints_task:
    def __init__(self,model,time_tot, task_days,T,days_to_monday):
        self.m = model
        self.time_tot = time_tot
        self.task_days = task_days
        self.T = T
        self.days_to_monday = days_to_monday
       

    def end_after_start_rule(self, m, i):
        """
        This function defines a rule that ensures the end time (tend) 
        is greater than the start time (tstart) 
        for a given index i in the model m.
    
        :param self: Reference to the current instance of the class.
        :param m: The model containing the time variables.
        :param i: The index for which the rule is being applied.
        :returns: True if tend[i] is greater than or equal to tstart[i] + 0.1, False otherwise.
        :rtype: bool
        """
        return m.tend[i] >= m.tstart[i] + 0.1
    
    
    def m_init_rule(self, m, i, j):
        """
        This function defines a rule that ensures that the decision variable x[i,j]
        is set to 0 for days before the initial time for a given index pair t(i, j)
        and can assume boolean value 1 for days after the initial time. 
        The time variable t[i][j] must be greater than or equal to the initial time,
        decided by the the decision variable start time tstart[i] at the week j.
    
        :param self: Reference to the current instance of the class.
        :param m: The model containing the time variables and activity variables.
        :param i: The first index for the time variable.
        :param j: The second index representing the day.
        :returns: True if the initial time is set correctly, False otherwise.
        :rtype: bool
        """
        return m.t[i][j - m.t[i][1] + 1] >= (((m.tstart[i] - 1) * self.T + (1 + self.days_to_monday)) - (self.time_tot + 1) * (1 - m.x[i, j]))
         
    def m_end_rule(self, m, i, j):
        """
        This function defines a rule that ensures that the decision variable x[i,j]
        is set to 0 for days after the end time for a given index pair t(i, j)
        and can assume boolean value 1 for days before the end time.
        The time variable t[i][j] must be less than or equal to the end time,
        decided by the decision variable end time tend[i] at the week j.
    
        :param self: Reference to the current instance of the class.
        :param m: The model containing the time variables and activity variables.
        :param i: The first index for the time variable.
        :param j: The second index representing the day.
        :returns: True if the end time is set correctly, False otherwise.
        :rtype: bool
        """
        return m.t[i][j - m.t[i][1] + 1] <= (m.tend[i] * self.T + self.days_to_monday) + (self.time_tot + 1) * (1 - m.x[i, j])
       
    def m_weekend_rule(self, m, i, j):
        """
        This function defines a rule that ensures no activity (x[i,j]) 
        is scheduled on weekends for a given index pair (i, j) in the model m.
    
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables and weekends.
        :param i: The first index for the activity variable.
        :param j: The second index representing the day.
        :returns: 
            - True if j is in m.weekends and m.x[i,j] is set to 0.
            - pyomo.Constraint.Skip if j is not in m.weekends.
        :rtype: bool or pyomo.Constraint.Skip
        """
        return m.x[i, j] == 0 if j in m.weekends else pyomo.Constraint.Skip
        
    def holidays_rule(self, m, i, j):
        """
        This function defines a rule that ensures no activity (x[i,j]) 
        is scheduled on holidays for a given index pair (i, j) in the model m.
    
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables and holidays.
        :param i: The first index for the activity variable.
        :param j: The second index representing the day.
        :returns: 
            - True if j is in m.holidays_day and m.x[i,j] is set to 0.
            - pyomo.Constraint.Skip if j is not in m.holidays_day.
        :rtype: bool or pyomo.Constraint.Skip
        """
        return m.x[i, j] == 0 if j in m.holidays_day else pyomo.Constraint.Skip
        
    def zero_init_rule(self, m, i, j):
        """
        This function defines a rule that ensures the activity variable (x[i,j]) 
        is set to 0 for days before the initial time for a given index pair (i, j) 
        in the model m.
    
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables and initial times.
        :param i: The first index for the activity variable.
        :param j: The second index representing the day.
        :returns: 
            - True if j is less than or equal to the calculated initial time, setting m.x[i,j] to 0.
            - pyomo.Constraint.Skip if j is greater than the calculated initial time.
        :rtype: bool or pyomo.Constraint.Skip
        """
        return m.x[i, j] == 0 if j <= ((m.init_times[i] - 1) * self.T + self.days_to_monday) else pyomo.Constraint.Skip
    
    def zero_end_rule(self, m, i, j):
        """
        This function defines a rule that ensures the activity variable (x[i,j]) 
        is set to 0 for days beyond the end time for a given index pair (i, j) 
        in the model m.
        
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables and end times.
        :param i: The first index for the activity variable.
        :param j: The second index representing the day.
        :returns: 
            - True if j is greater than or equal to the calculated end time, setting m.x[i,j] to 0.
            - pyomo.Constraint.Skip if j is less than the calculated end time.
        :rtype: bool or pyomo.Constraint.Skip
        """
        return m.x[i, j] == 0 if j >= (m.end_times[i] * self.T + 1 + self.days_to_monday) else pyomo.Constraint.Skip
        
    def task(self, m, i):
        """
        This function defines a rule that ensures a task is scheduled 
        for the exact number of days specified by self.task_days for 
        a given index i in the model m.
        
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables.
        :param i: The index for the task.
        :returns: True if the sum of days scheduled for task i equals self.task_days, False otherwise.
        :rtype: bool
        
        The return equation is:
        \[
        \sum_{j} m.x[i, j] == self.task_days
        \]
        """
        return sum(m.x[i, :]) == self.task_days
    
    def no_overlap(self, m, j):
        """
        This function defines a rule that ensures no overlapping activities 
        for a given index (day) j in the model m. It ensures that at most one 
        activity can be scheduled at the same time.
        
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables.
        :param j: The index representing the time slot.
        :returns: True if the sum of activities scheduled at time slot j is less than or equal to 1, False otherwise.
        :rtype: bool
        """
        return sum(m.x[:, j]) <= 1
    
    def busy_days(self, m, i, j):
        """
        This function defines a rule that ensures no activity (x[i,j]) 
        is scheduled on busy days for a given index pair (i, j) in the model m.
        
        :param self: Reference to the current instance of the class.
        :param m: The model containing the activity variables and busy days.
        :param i: The first index referred to the particular unit.
        :param j: The second index for the activity variable, representing the day.
        :returns: 
            - True if j is in m.busy_days and m.x[i,j] is set to 0.
            - pyomo.Constraint.Skip if j is not in m.busy_days.
        :rtype: bool or pyomo.Constraint.Skip
        """
        return m.x[i, j] == 0 if j in m.busy_days else pyomo.Constraint.Skip
    

    



    
    

