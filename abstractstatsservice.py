from abc import ABC, abstractmethod, abstractproperty
from typing import List

class StatsGenerator(ABC):

    titles = []
    stats = []

    stats_objects = []

    @abstractmethod
    def gather_stats(self):
        pass

    def get_general_trips_amount(self, trips):  # used by daughter classes
        return len(trips)






