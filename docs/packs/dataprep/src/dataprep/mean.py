"""
dataprep.mean
~~~~~~~~~~~~~

This module implements dataprep mean.
"""

import sys

from dataprep.cymean import mean


def main():
    """Calculates the mean value.

    :param numbers: Numbers from which the mean value is to be calculated.
    :return: :class:`float <float>` object
    :rtype: float
    """

    result = 0.0

    try:
        nums = [float(num) for num in sys.argv[1:]]
    except ValueError:
        nums = []

    try:
        result = mean(nums)
    except ZeroDivisionError:
        pass

    print(result)


if __name__ == "__main__":
    main()
