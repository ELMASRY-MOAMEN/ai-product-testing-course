from abc import ABC, abstractmethod
class BaseAdapter(ABC):
    @abstractmethod
    def invoke(self, case: dict) -> dict: raise NotImplementedError
