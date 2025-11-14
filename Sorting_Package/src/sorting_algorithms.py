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