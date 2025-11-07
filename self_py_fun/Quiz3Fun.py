import numpy as np


# This function is merely for BIOS 584 debugging purposes
def compute_D_partial(input_signal):
    r"""
    :param input_signal:
    """
    T_len = len(input_signal)
    signal_diff_one = input_signal[-1] - input_signal[1:]
    D_val = np.sum(np.sqrt(1+signal_diff_one**2)) / (T_len - 1)
    return D_val


def compute_D_correct(input_signal):
    r"""
    :param input_signal:
    """
    D_val = None
    return D_val


import numpy as np


# Task 1: Original function with typos identified
def compute_D_partial_for_task_1_only(input_signal):
    """
    Original function with typos for debugging purposes
    """
    T = len(input_signal)
    D_val = 0

    for i in range(T):  # TYPO 1: Should be range(T-1) to avoid index out of bounds and match formula
        # TYPO 2: Should be subtraction (x[i] - x[i+1]) not addition
        diff = input_signal[i] + input_signal[i + 1]
        D_val += np.sqrt(1 + diff ** 2)

    return D_val


def compute_D_correct(input_signal):
    T = len(input_signal)
    D_val = 0

    for i in range(T - 1):
        diff = input_signal[i] - input_signal[i + 1]
        D_val += np.sqrt(1 + diff ** 2)

    return D_val  # ← Make sure this line is there!