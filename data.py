"""
## Recreating the toy sine example from https://arxiv.org/pdf/1506.09024.pdf

Get data from sine_data.npy or line_data.npy.
"""
import os
from pathlib import Path
import numpy as np


def get_data(line_or_sine, x_errors):
    """Returns tuple xs, ys for either "line" or "sine"."""
    location = Path(__file__).parent
    if x_errors:
        filename = location.joinpath("data_{}_x_errors.npy".format(line_or_sine))
    else:
        filename = location.joinpath("data_{}.npy".format(line_or_sine))
    data = np.load(filename)
    return data[0], data[1]
