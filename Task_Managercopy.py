######## Objective: give back a dictonary of couples ##########
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import itertools



def partition_dict(bound_dict_init, units_partition, n_units, n_units_tot, remainder):
    """
    Partitions the units according to the number of subproblems.
    This function divides the original optimization problem into multiple subproblems, each containing a fraction of the total number of units' tasks.

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
    :returns: A list of dictionaries, each containing a partition of the units.
    :rtype: list[dict]
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



