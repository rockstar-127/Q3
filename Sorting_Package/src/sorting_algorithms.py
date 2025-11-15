"""
sorting_algorithms.py

Implements an abstract base class for sorting algorithms and concrete
implementations of Bubble Sort, Selection Sort, Quick Sort, Merge Sort,
and Shell Sort. Also provides a SortingSelector factory class.
"""

from abc import ABC, abstractmethod
from typing import List


# ----------------------------- VALIDATION HELPERS ----------------------------- #

def validate_input_list(data: List[int]) -> None:
    """
    Validates input list for sorting algorithms.

    Rules:
    1. Must be a Python list.
    2. Must contain ONLY integers.
    3. Length must be less than 2 × 10^5.

    Raises
    ------
    TypeError
        If data is not a list or contains non-integers.
    ValueError
        If list exceeds maximum allowed size.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list of integers.")

    if len(data) >= 2 * 10**5:
        raise ValueError("List size must be < 2 × 10^5 elements.")

    for item in data:
        if not isinstance(item, int):
            raise TypeError("Sorting supports ONLY integer lists.")


# --------------------------- ABSTRACT BASE CLASS ------------------------------ #

class SortAlgorithm(ABC):
    """
    Abstract base class defining the interface for all sorting algorithms.
    """

    @abstractmethod
    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        """
        Sort the given list of integers.

        Parameters
        ----------
        data : list[int]
            The list of integers to be sorted.
        order : str, optional
            Sorting order, by default "ascending".

        Returns
        -------
        list[int]
            A sorted list of integers.
        """


    def validate(self, data: List[int]) -> None:
        """
        Validates input before sorting.

        Parameters
        ----------
        data : list[int]
            List to validate.
        """
        validate_input_list(data)


# ----------------------------- BUBBLE SORT ----------------------------------- #

class BubbleSort(SortAlgorithm):
    """Bubble Sort algorithm implementation."""

    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        self.validate(data)
        arr = data.copy()
        n = len(arr)
        reverse = order == "descending"

        for i in range(n):
            for j in range(0, n - i - 1):
                if (not reverse and arr[j] > arr[j + 1]) or \
                   (reverse and arr[j] < arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


# ----------------------------- SELECTION SORT -------------------------------- #

class SelectionSort(SortAlgorithm):
    """Selection Sort algorithm implementation."""

    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        self.validate(data)
        arr = data.copy()
        n = len(arr)
        reverse = order == "descending"

        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if (not reverse and arr[j] < arr[idx]) or \
                   (reverse and arr[j] > arr[idx]):
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]

        return arr


# ------------------------------ QUICK SORT ----------------------------------- #

class QuickSort(SortAlgorithm):
    """Quick Sort implementation using divide-and-conquer."""

    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        self.validate(data)

        if len(data) <= 1:
            return data.copy()

        reverse = order == "descending"
        pivot = data[len(data) // 2]

        left = [x for x in data if (x < pivot and not reverse) or (x > pivot and reverse)]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if (x > pivot and not reverse) or (x < pivot and reverse)]

        return self.sort(left, order) + mid + self.sort(right, order)


# ------------------------------ MERGE SORT ----------------------------------- #

class MergeSort(SortAlgorithm):
    """Merge Sort implementation."""

    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        self.validate(data)

        if len(data) <= 1:
            return data.copy()

        mid = len(data) // 2
        left = self.sort(data[:mid], order)
        right = self.sort(data[mid:], order)

        return self._merge(left, right, order)

    def _merge(self, left: List[int], right: List[int], order: str) -> List[int]:
        reverse = order == "descending"
        merged = []
        i = j = 0

        # Efficient merge using pointers instead of pop(0)
        while i < len(left) and j < len(right):
            if (not reverse and left[i] < right[j]) or \
               (reverse and left[i] > right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


# ------------------------------- SHELL SORT ---------------------------------- #

class ShellSort(SortAlgorithm):
    """Shell Sort algorithm using gap sequence."""

    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        self.validate(data)
        arr = data.copy()
        n = len(arr)
        gap = n // 2
        reverse = order == "descending"

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i

                while j >= gap and (
                    (not reverse and arr[j - gap] > temp)
                    or (reverse and arr[j - gap] < temp)
                ):
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp

            gap //= 2

        return arr


# ---------------------------- SORTING SELECTOR ------------------------------- #

class SortingSelector:
    """Factory class to select and execute a sorting algorithm."""

    def __init__(self, algorithm_name: str):
        self.algorithm_name = algorithm_name.lower()

    def get_algorithm(self) -> SortAlgorithm:
        """Returns an instance of the requested sorting algorithm."""
        algorithms = {
            "bubble": BubbleSort,
            "selection": SelectionSort,
            "quick": QuickSort,
            "merge": MergeSort,
            "shell": ShellSort,
        }

        if self.algorithm_name not in algorithms:
            raise ValueError("Invalid algorithm name.")

        return algorithms[self.algorithm_name]()

    def sort(self, data: List[int], order: str = "ascending") -> List[int]:
        """Runs the requested algorithm."""
        algorithm = self.get_algorithm()
        return algorithm.sort(data, order)
