import pyomo.environ as pyomo
import itertools

class Bounds_class:
    def __init__(self,model, bound_dict):
        self.m = model
        self.bound_dict = bound_dict

    def bounds_rule(self,m,i):
        return self.bound_dict[i] 

    def bounds_rule_t(self,m,i):
        return self.bound_dict[i]  
    
    def bounds_rule_zeroinit(self,m,i):
        return self.bound_dict[i][0]
    
    def bounds_rule_zeroend(self,m,i):
        return self.bound_dict[i][1]
    
'''Function to partition the units according to the number of subproblems'''
def partition_dict(bound_dict_init, units_partition, n_units, n_units_tot, remainder):
    items = iter(bound_dict_init.items())
    dict_partitions = []
    if units_partition <= n_units_tot:
        if remainder == 0:
            dict_partitions = [dict(itertools.islice(items, n_units)) for _ in range(units_partition)]
        else:
            dict_partitions = [dict(itertools.islice(items, n_units+1)) if i < remainder else dict(itertools.islice(items, n_units)) for i in range(units_partition)]
    else:
        # If units_partition is greater than n_units_tot, split into groups of one element
        dict_partitions = [dict([next(items)]) for _ in range(n_units_tot)]
    return dict_partitions

def n_units_tuple(dict_partitions_current): # Define a list of possible units-times couples
    all_keys = list(dict_partitions_current.keys())
    return all_keys

# Define a dictornary of touples for the bounds of the tend variables where every touple is shifted by 1
def bound_dict_end(bound_dict_init, weeks, best_task_delta_weeks):
    bound_dict_end = {k: (v[0]+best_task_delta_weeks, v[1]+best_task_delta_weeks if weeks-v[1]>=1 else v[1]) for k, v in bound_dict_init.items()}
    return bound_dict_end

# Define a dictornary of touples for the bounds of the m.t, so the start an the end date
def bound_dict_t(bound_dict_init, weeks, T,days_to_monday, time_horizon_tot, best_task_delta_weeks):
    bound_dict_t = {k: ((v[0]-1)*T+(1+days_to_monday), (v[1]+best_task_delta_weeks)*T+days_to_monday) if ((v[1]+1)*T+days_to_monday)<=time_horizon_tot else ((v[0]-1)*T+(1+days_to_monday), time_horizon_tot) for k, v in bound_dict_init.items()}
    bound_dict_t= {k: list(range(v[0], v[1]+1)) for k, v in bound_dict_t.items()}
    return bound_dict_t

# Define a list of possible units-times couples
def possible_unit_times(bound_dict_t):
    possible_unit_times = [(s,t) for s in bound_dict_t.keys() for t in bound_dict_t[s]]
    return possible_unit_times
    
