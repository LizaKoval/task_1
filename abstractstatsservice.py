from abc import ABC, abstractmethod, abstractproperty
from typing import List

class StatsGenerator(ABC):
    @abstractmethod
    def get_stats(self, trips):
        pass

    def get_general_trips_amount(self, trips):  # used by daughter classes
        return len(trips)






