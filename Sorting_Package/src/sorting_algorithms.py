"""
sorting_algorithms.py
Contains abstract base class for sorting algorithms.
"""

from abc import ABC, abstractmethod

class SortAlgorithm(ABC):
    """
    Parent abstract class for sorting algorithms.
    Forces all child classes to implement 'sort()'.
    """

    @abstractmethod
    def sort(self, data, order="ascending"):
        """
        Sort the given list of integers.
        Should return a NEW sorted list.
        """
        pass
