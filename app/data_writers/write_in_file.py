from abc import ABC, abstractmethod
import csv


class Writer(ABC):
    @abstractmethod
    def write(self, obj):
        pass

class GeneralStatsWriter(Writer):
    def __init__(self, filename):
        self.filename = filename

    def write(self, obj):
        titles = ['Total Trip Count', 'Max Trip Time', 'Total Bike Count', 'Unprocessed Rows Count']

        with open(self.filename,'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(titles)
            writer.writerow([obj.trips_amount, obj.max_trip_time, obj.bikes_amount, obj.unprocessed_count])

class UsageStatsWriter(Writer):
    def __init__(self, filename):
        self.filename = filename

    def write(self, obj):
        titles = ['Month', 'Trips amount']

        with open(self.filename, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(titles)
            items = obj.stats
            for item in items:
                writer.writerow([item.month, item.bikes_amount])

class BikeStatsWriter(Writer):
    def __init__(self, filename):
        self.filename = filename

    def write(self, obj):
        titles = ['Total of trips', 'Term of use', 'Bike number']

        with open(self.filename, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(titles)
            items = obj.stats
            for item in items:
                writer.writerow([item.bikes_trips_amount, item.term_of_use, item.bike_number])