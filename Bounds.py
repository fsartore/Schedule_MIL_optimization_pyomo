import pyomo.environ as pyomo
import itertools



def partition_dict(bound_dict_init, units_partition, n_units, n_units_tot, remainder):
    """
        Partitions the units according to the number of subproblems.

        :param bound_dict_init: The initial bound dictionary.
        :type bound_dict_init: dict
        :param units_partition: The number of partitions.
        :type units_partition: int
        :param n_units: The number of units per partition.
        :type n_units: int
        :param n_units_tot: The total number of units.
        :type n_units_tot: int
        :param remainder: The remainder when dividing the total number of units by the number of partitions.
        :type remainder: int
        :returns: dict_partitions: A list of dictionaries, each containing a partition of the units.
        :rtype: list of dict
    """
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

def n_units_tuple(dict_partitions_current):
    """
    Defines a list of possible units-times couples.

    :param dict_partitions_current: The current partition dictionary.
    :type dict_partitions_current: dict
    :returns: A list of keys from the partition dictionary.
    :rtype: list
    """
    all_keys = list(dict_partitions_current.keys())
    return all_keys

def bound_dict_end(bound_dict_init, weeks, best_task_delta_weeks):
    """
    Defines a dictionary of tuples for the bounds of the end variables where every tuple is shifted by a given number of weeks.

    :param bound_dict_init: The initial bound dictionary.
    :type bound_dict_init: dict
    :param weeks: The number of weeks in the time horizon.
    :type weeks: int
    :param best_task_delta_weeks: The number of weeks to shift the bounds.
    :type best_task_delta_weeks: int
    :returns: A dictionary with the updated bounds.
    :rtype: dict
    """
    bound_dict_end = {k: (v[0]+best_task_delta_weeks, v[1]+best_task_delta_weeks if weeks-v[1]>=1 else v[1]) for k, v in bound_dict_init.items()}
    return bound_dict_end

def bound_dict_t(bound_dict_init, weeks, T, days_to_monday, time_horizon_tot, best_task_delta_weeks):
    """
    Defines a dictionary of tuples for the bounds of the m.t variables, representing the start and end dates.

    :param bound_dict_init: The initial bound dictionary.
    :type bound_dict_init: dict
    :param weeks: The number of weeks in the time horizon.
    :type weeks: int
    :param T: The number of days in a week.
    :type T: int
    :param days_to_monday: The number of days to the next Monday.
    :type days_to_monday: int
    :param time_horizon_tot: The total time horizon.
    :type time_horizon_tot: int
    :param best_task_delta_weeks: The number of weeks to shift the bounds.
    :type best_task_delta_weeks: int
    :returns: A dictionary with the updated bounds.
    :rtype: dict
    """
    bound_dict_t = {k: ((v[0]-1)*T+(1+days_to_monday), (v[1]+best_task_delta_weeks)*T+days_to_monday) if ((v[1]+1)*T+days_to_monday)<=time_horizon_tot else ((v[0]-1)*T+(1+days_to_monday), time_horizon_tot) for k, v in bound_dict_init.items()}
    bound_dict_t = {k: list(range(v[0], v[1]+1)) for k, v in bound_dict_t.items()}
    return bound_dict_t

def possible_unit_times(bound_dict_t):
    """
    Defines a list of possible units-times couples.

    :param bound_dict_t: The dictionary containing the bounds for the m.t variables.
    :type bound_dict_t: dict
    :returns: A list of tuples representing possible units-times couples.
    :rtype: list of tuple
    """
    possible_unit_times = [(s, t) for s in bound_dict_t.keys() for t in bound_dict_t[s]]
    return possible_unit_times
    
class Bounds_class:
    """
    A class to handle bounds for a given model and bound dictionary.

    Attributes:
    m : model
        The model to which the bounds are applied.
    bound_dict : dict
        A dictionary containing the bounds for each unit.
    """

    def __init__(self, model, bound_dict):
        """
        Initializes the Bounds_class with a model and a bound dictionary.

        :param model: The model to which the bounds are applied.
        :type model: model
        :param bound_dict: A dictionary containing the bounds for each unit.
        :type bound_dict: dict
        """
        self.m = model
        self.bound_dict = bound_dict

    def bounds_rule(self, m, i):
        """
        Returns the bounds for a given unit.

        :param m: The model to which the bounds are applied.
        :type m: model
        :param i: The unit for which the bounds are returned.
        :type i: int
        :returns: The bounds for the given unit.
        :rtype: tuple
        """
        return self.bound_dict[i]


    def bounds_rule_zeroinit(self, m, i):
        """
        Returns the initial bound for a given unit.

        :param m: The model to which the bounds are applied.
        :type m: model
        :param i: The unit for which the initial bound is returned.
        :type i: int
        :returns: The initial bound for the given unit.
        :rtype: int
        """
        return self.bound_dict[i][0]

    def bounds_rule_zeroend(self, m, i):
        """
        Returns the end bound for a given unit.

        :param m: The model to which the bounds are applied.
        :type m: model
        :param i: The unit for which the end bound is returned.
        :type i: int
        :returns: The end bound for the given unit.
        :rtype: int
        """
        return self.bound_dict[i][1]