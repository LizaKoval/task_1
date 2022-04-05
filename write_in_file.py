from abc import ABC, abstractmethod
import csv
from typing import List

from bike_stats_storage import BikeStats
from usage_stats_storage import UsageStats


class Writer(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def write(self, obj):
        pass

class GeneralStatsWriter(Writer):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, obj):
        titles = ['Total Trip Count', 'Max Trip Time', 'Total Bike Count', 'Unprocessed Rows Count']

        with open(self.filename,'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(titles)
            writer.writerow(list[obj.trips_amount, obj.max_trip_time, obj.bikes_amount, obj.unprocessed_count])

class UsageStatsWriter(Writer):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, objects: List[UsageStats]):
        titles = ['Month', 'Trips amount']

        with open(self.filename, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(titles)
            for obj in objects:
                writer.writerow(list[obj.month, obj.bikes_amount])

class BikeStatsWriter(Writer):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, objects: List[BikeStats]):
        titles = ['Total of trips', 'Term of use', 'Bike number']

        with open(self.filename, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(titles)
            for obj in objects:
                writer.writerow(list[obj.bikes_trips_amount, obj.term_of_use, obj.bike_number])