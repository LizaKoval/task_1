from abc import ABC, abstractmethod, abstractproperty

class StatsGenerator(ABC):

    titles = []
    stats = []

    @abstractmethod
    def gather_stats(self):
        pass

    @staticmethod # TODO: think about its decorater
    def get_general_trips_amount(self, trips):  # used by daughter classes
        return len(trips)






