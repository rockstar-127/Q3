from abc import ABC, abstractmethod

class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data, order="ascending"):
        pass
