from abc import ABC, abstractmethod

class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data, order="ascending"):
        pass


class BubbleSort(SortAlgorithm):

    def sort(self, data, order="ascending"):
        data = data.copy()
        n = len(data)

        for i in range(n):
            for j in range(0, n - i - 1):
                if (order == "ascending" and data[j] > data[j+1]) or \
                   (order == "descending" and data[j] < data[j+1]):
                    data[j], data[j+1] = data[j+1], data[j]

        return data


class SelectionSort(SortAlgorithm):
    def sort(self, data, order="ascending"):
        data = data.copy()
        n = len(data)

        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if (order == "ascending" and data[j] < data[idx]) or \
                   (order == "descending" and data[j] > data[idx]):
                    idx = j

            data[i], data[idx] = data[idx], data[i]

        return data
    
    
class QuickSort(SortAlgorithm):
    def sort(self, data, order="ascending"):
        if len(data) <= 1:
            return data.copy()

        pivot = data[len(data) // 2]

        left = [x for x in data if (x < pivot and order == "ascending") or
                                   (x > pivot and order == "descending")]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if (x > pivot and order == "ascending") or
                                    (x < pivot and order == "descending")]

        return self.sort(left, order) + mid + self.sort(right, order)


class MergeSort(SortAlgorithm):
    def sort(self, data, order="ascending"):
        if len(data) <= 1:
            return data.copy()

        mid = len(data) // 2
        left = self.sort(data[:mid], order)
        right = self.sort(data[mid:], order)

        return self._merge(left, right, order)

    def _merge(self, left, right, order):
        result = []
        while left and right:
            if (order == "ascending" and left[0] < right[0]) or \
               (order == "descending" and left[0] > right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        result.extend(left)
        result.extend(right)
        return result
    
class SortingSelector:
    def __init__(self, algorithm_name):
        self.algorithm_name = algorithm_name.lower()

    def get_algorithm(self):
        if self.algorithm_name == "bubble":
            return BubbleSort()
        elif self.algorithm_name == "selection":
            return SelectionSort()
        elif self.algorithm_name == "quick":
            return QuickSort()
        elif self.algorithm_name == "merge":
            return MergeSort()
        else:
            raise ValueError("Invalid algorithm name.")

    def sort(self, data, order="ascending"):
        algo = self.get_algorithm()
        return algo.sort(data, order)
