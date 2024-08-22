import random

def handle_unfeasibility( target_week_dict, weeks,   counter_unfeasibility, counter_unfeasibility_max,
                         mainteinace_flexibility_down, task_flexibility_up,
                         adjustments_tracker= None, target_week_dict_unfeasible=None,
                           dict_pairs_unfeasible=None, target_week_base_unfeasible=None,
                           adjustments_tracker_base=None):
    """
        Handles the case when scheduling is unfeasible by attempting various adjustments.
        This function is the main one to be called when unfeasibility is detected.
        Specifics of the adjustments are defined in the functions called within this function.
        
        :param unfeasible: Boolean indicating if the current scheduling is unfeasible.
        :type unfeasible: bool
        :param target_week_dict: The current target week dictionary.
        :type target_week_dict: dict
        :param weeks: Total number of weeks.
        :type weeks: int
        :param dict_pairs: Current dictionary pairs.
        :type dict_pairs: dict
        :param adjustments_tracker: Tracker for adjustments made.
        :type adjustments_tracker: dict
        :param counter_unfeasibility: Counter for the number of unfeasibility attempts.
        :type counter_unfeasibility: int
        :return: Updated target_week_dict, adjustments_tracker, and dict_pairs.
        :rtype: tuple[dict, dict, dict]
    """
    dict_pairs = {(i, j): 0 for i in target_week_dict.keys() for j in target_week_dict.keys() if i != j}
    if target_week_dict_unfeasible is not None and dict_pairs_unfeasible is not None:
        target_week_dict = target_week_dict_unfeasible
        dict_pairs = dict_pairs_unfeasible

    if counter_unfeasibility < 20:
        target_week_dict_unfeasible, adjustments_tracker, dict_pairs_unfeasible = adjust_values_to_reduce_crowding(target_week_dict, weeks, dict_pairs, adjustments_tracker)
        target_week_base_unfeasible = target_week_dict_unfeasible.copy()
        adjustments_tracker_base = adjustments_tracker.copy()
    elif counter_unfeasibility == 20 and (mainteinace_flexibility_down == 2 or task_flexibility_up ==2):
        target_week_dict_unfeasible, adjustments_tracker, dict_pairs_unfeasible = adjust_values_to_reduce_crowding(target_week_dict, weeks, dict_pairs, adjustments_tracker)
        target_week_base_unfeasible = target_week_dict_unfeasible.copy()
        adjustments_tracker_base = adjustments_tracker.copy()
        counter_unfeasibility = counter_unfeasibility_max        
    elif 20 <= counter_unfeasibility <= 25:
        print('\033[92m' + 'desperate attempt one.' + '\033[0m')
        target_week_dict_unfeasible, adjustments_tracker = desperate_adjust_target_week(target_week_base_unfeasible, adjustments_tracker_base, weeks, 3, 2, 8, 0, 0)
    elif 25 < counter_unfeasibility <= 30:
        print('\033[92m' + 'desperate attempt two.' + '\033[0m')
        target_week_dict_unfeasible, adjustments_tracker = desperate_adjust_target_week(target_week_base_unfeasible,adjustments_tracker_base, weeks, 3, 2, 6, 2, 0)
    elif 30 < counter_unfeasibility <= 35:
        print('\033[92m' + 'desperate attempt three.' + '\033[0m')
        target_week_dict_unfeasible, adjustments_tracker = desperate_adjust_target_week(target_week_base_unfeasible,adjustments_tracker_base, weeks, 3, 2, 4, 4, 0)
    elif 35 < counter_unfeasibility <= counter_unfeasibility_max:
        print('\033[92m' + 'desperate attempt four.' + '\033[0m')
        target_week_dict_unfeasible, adjustments_tracker = desperate_adjust_target_week(target_week_base_unfeasible,adjustments_tracker_base, weeks, 3, 2, 2, 2, 2)

    return target_week_dict_unfeasible, adjustments_tracker, dict_pairs_unfeasible, target_week_base_unfeasible, adjustments_tracker_base, counter_unfeasibility


def adjust_values_to_reduce_crowding(target_week_dict, weeks, dict_pairs, adjustments_tracker=None ):
    '''
        It is used in case of unfeasibility to change a bit the target week dictionary to make the task feasible.
        LOGIC:
        1. If the difference between the two closest values is less than weeks/2, 
        adjust the value with the smaller adjustment_tracker value 
        by increasing it by 1 if the value is the bigger one and by decreasing it by 1 if the value is the smaller one
        and if the destination is free, otherwise increase the bigger by one.
        2. If the difference between the two closest values is more than weeks/2,
        adjust the value with the smaller adjustment_tracker value
        by decreasing it by 1 if the value is the smaller one and by increasing it by 1 if the value is the bigger one
        and if the destination is free, otherwise decrease the smaller by one.

        :param target_week_dict: The current target week dictionary, when the task should be scheduled.
        :type target_week_dict: dict[str, int]
        :param weeks: Total number of weeks.
        :type weeks: int
        :param dict_pairs: Current dictionary pairs, made of all the possible combinations of two units.
        :type dict_pairs: dict[str, tuple[str, str]]
        :param adjustments_tracker: Tracker for adjustments made.
        :type adjustments_tracker: dict[str, int]
        :return: Updated target_week_dict, adjustments_tracker, and dict_pairs.
        :rtype: tuple[dict[str, int], dict[str, int], dict[str, tuple[str, str]]]
    '''

    if not target_week_dict:
        return target_week_dict, {}

    if adjustments_tracker is None:
        adjustments_tracker = {key: 0 for key in target_week_dict.keys()}  # Initialize tracking dictionary

    def adjust_value(val, direction, key):
        return min(max(1, val + (1 if direction == "up" else -1)), weeks)

    def find_closest_pair(values, dict_pairs, sorted_values):
        min_distance = weeks
        pair_indices = (0, 1)     
        pair_indices_equal = [] 
        for i in range(len(values) - 1):
            distance = values[i + 1] - values[i]
            if distance <= min_distance:
                min_distance = distance
        for i in range(len(values) - 1):
            distance = values[i + 1] - values[i]
            if distance == min_distance:
                pair_indices = (i, i + 1)
                pair_indices_equal.append(pair_indices)

        pair_indices = min(pair_indices_equal, key=lambda x: dict_pairs[(sorted_values[x[0]][1], sorted_values[x[1]][1])]) 
        return pair_indices

    sorted_values = sorted((value, key) for key, value in target_week_dict.items())
    adjustments_needed = True

    counter = 0
    i = None
    j = None
    while adjustments_needed:
        adjustments_needed = False
        counter += 1
        if counter > 10:
            break
        values_only = [value for value, key in sorted_values]
        if i is not None and j is not None:
            dict_pairs[(sorted_values[i][1], sorted_values[j][1])] += 1
        i,j = find_closest_pair(values_only, dict_pairs, sorted_values)

        if values_only[j] < weeks / 2:
            if abs(adjustments_tracker[sorted_values[j][1]]) <= abs(adjustments_tracker[sorted_values[i][1]]):
                key_for_j = sorted_values[j][1]
                new_value_up = adjust_value(values_only[j], "up", key_for_j)
                new_value_down = adjust_value(values_only[j], "down", key_for_j)
                if new_value_up not in values_only[j+1:] and new_value_down not in values_only[:j]:
                    sorted_values = [(new_value_up if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] += 1
                elif new_value_up in values_only[j+1:] and new_value_down not in values_only[:j]:
                    sorted_values = [(new_value_down if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] -= 1
                elif new_value_up not in values_only[j+1:] and new_value_down in values_only[:j]:
                    sorted_values = [(new_value_up if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] += 1
                else:
                    sorted_values = [(new_value_up if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] += 1
                    adjustments_needed = True
            else: 
                kew_for_i = sorted_values[i][1]
                new_value_up = adjust_value(values_only[i], "up", kew_for_i)
                new_value_down = adjust_value(values_only[i], "down", kew_for_i)
                if new_value_up not in values_only[i+1:] and new_value_down not in values_only[:i]:
                    sorted_values = [(new_value_up if key == kew_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[kew_for_i] -= 1
                elif new_value_up in values_only[i+1:] and new_value_down not in values_only[:i]:
                    sorted_values = [(new_value_down if key == kew_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[kew_for_i] -= 1
                elif new_value_up not in values_only[i+1:] and new_value_down in values_only[:i]:
                    sorted_values = [(new_value_up if key == kew_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[kew_for_i] += 1
                else:
                    sorted_values = [(new_value_up if key == kew_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[kew_for_i] -= 1
                    adjustments_needed = True   
        else:
            if abs(adjustments_tracker[sorted_values[i][1]]) <= abs(adjustments_tracker[sorted_values[j][1]]):
                key_for_i = sorted_values[i][1]
                new_value_up = adjust_value(values_only[i], "up", key_for_i)
                new_value_down = adjust_value(values_only[i], "down", key_for_i)
                if new_value_up not in values_only[i+1:] and new_value_down not in values_only[:i]:
                    sorted_values = [(new_value_down if key == key_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_i] -= 1
                elif new_value_up in values_only[i+1:] and new_value_down not in values_only[:i]:
                    sorted_values = [(new_value_down if key == key_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_i] -= 1
                elif new_value_up not in values_only[i+1:] and new_value_down in values_only[:i]:
                    sorted_values = [(new_value_up if key == key_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_i] += 1
                else:
                    sorted_values = [(new_value_down if key == key_for_i else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_i] -= 1
                    adjustments_needed = True
            else:
                key_for_j = sorted_values[j][1]
                new_value_up = adjust_value(values_only[j], "up", key_for_j)
                new_value_down = adjust_value(values_only[j], "down", key_for_j)
                if new_value_up not in values_only[j+1:] and new_value_down not in values_only[:j]:
                    sorted_values = [(new_value_up if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] += 1
                elif new_value_up in values_only[j+1:] and new_value_down not in values_only[:j]:
                    sorted_values = [(new_value_down if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] -= 1
                elif new_value_up not in values_only[j+1:] and new_value_down in values_only[:j]:
                    sorted_values = [(new_value_up if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] += 1
                else:
                    sorted_values = [(new_value_up if key == key_for_j else value, key) for value, key in sorted_values]
                    adjustments_tracker[key_for_j] += 1
                    adjustments_needed = True

        # Reconstruct sorted_values with updated values
        sorted_values.sort(key=lambda x: x[0])  # Sort by value after adjustment

    # Reconstruct target_week_dict from sorted_values
    for value, key in sorted_values:
        target_week_dict[key] = value

    return target_week_dict, adjustments_tracker, dict_pairs

def desperate_adjust_target_week(target_week_dict_original, adjustments_tracker_base, week, flex_adjust,
                                 zero_weight, one_weight, two_weight, three_weight,
                                   adjustments_tracker=None, target_week_dict=None):
    """
        Adjusts the values of target_week_dict randomly within a range of +-flex_adjust,
        ensuring the final values are between 1 and `week`. Tracks the adjustments made
        in adjustments_tracker. Gives more probability to a change of +-(numb) weight
        depending on the weight given to the number.
    
        :param target_week_dict_original: The original target week dictionary.
        :type target_week_dict_original: dict[str, int]
        :param adjustments_tracker_base: The original adjustments tracker.
        :type adjustments_tracker_base: dict[str, int]
        :param week: The total number of weeks.
        :type week: int
        :param flex_adjust: The maximum adjustment value in weeks.
        :type flex_adjust: int
        :param zero_weight: The weight for 0 weeks adjustments.
        :type zero_weight: float
        :param one_weight: The weight for 1 week adjustments.
        :type one_weight: float
        :param two_weight: The weight for 2 weeks adjustments.
        :type two_weight: float
        :param three_weight: The weight for 3 weeks adjustments.
        :type three_weight: float
        :param adjustments_tracker: The current adjustments tracker.
        :type adjustments_tracker: dict[str, int]
        :param target_week_dict: The current target week dictionary.
        :type target_week_dict: dict[str, int]
        :return: Updated target_week_dict and adjustments_tracker.
        :rtype: tuple[dict[str, int], dict[str, int]]
    """
    if adjustments_tracker is None:
        adjustments_tracker = {}
    if target_week_dict is None:
        target_week_dict = target_week_dict_original.copy()

    for key, value in target_week_dict_original.items():
        # Generate a weighted list of possible adjustments
        adjustments = list(range(-flex_adjust, flex_adjust + 1))
        # Increase the weight for -1 and +1 adjustments
        adjustments += [-1, 1] * one_weight  # Adjust the multiplier to tweak the weighting
        adjustments += [0] * zero_weight  # Add a few 0s to the list
        adjustments += [-2, 2]* two_weight # Add a few -2s and 2s to the list
        adjustments += [-3, 3]* three_weight  # Add a few -3s and 3s to the list

        # Select a random adjustment, ensuring it's within the valid range
        while True:
            adjustment = random.choice(adjustments)
            new_value = value + adjustment
            if 1 <= new_value <= week:
                break

        # Update the target_week_dict with the new value
        target_week_dict[key] = new_value

        # Track the difference between the new and original value
        adjustments_tracker[key] = adjustments_tracker_base[key] + adjustment 

    return target_week_dict, adjustments_tracker


def adjusted_bound_dict_init(target_week_dict, weeks, task_flexibility_up, task_felxibility_down):
    '''
        This function is used to adjust the bound_dict_init in case of unfeasibility.
        
        :param target_week_dict: The current target week dictionary, when the task should be scheduled.
        :type target_week_dict: dict[str, int]
        :param weeks: Total number of weeks.
        :type weeks: int
        :param task_flexibility_up: The maximum number of weeks the task can be scheduled after the target week.
        :type task_flexibility_up: int
        :param task_flexibility_down: The maximum number of weeks the task can be scheduled before the target week.
        :type task_flexibility_down: int
        :return: Updated bound_dict_init.
        :rtype: dict[str, tuple[int, int]]
    '''
    bound_dict_init = {i: (1, weeks) for i in target_week_dict.keys()}
    for i in target_week_dict.keys():
        if target_week_dict[i]-task_felxibility_down >= 1 and target_week_dict[i]+task_flexibility_up <= weeks:
            bound_dict_init[i] = (target_week_dict[i]-task_felxibility_down, target_week_dict[i]+task_flexibility_up)
        elif target_week_dict[i]-task_felxibility_down < 1 and target_week_dict[i]+task_flexibility_up <= weeks:
            bound_dict_init[i] = (1, target_week_dict[i]+task_flexibility_up)
        elif target_week_dict[i]-task_felxibility_down >= 1 and target_week_dict[i]+task_flexibility_up > weeks:
            bound_dict_init[i] = (target_week_dict[i]-task_felxibility_down, weeks)
        else:
            bound_dict_init[i] = (1, weeks)
    return bound_dict_init






