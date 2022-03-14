import csv
from typing import List

from trip_data import TripData
from trip_data import FileReader


class DataServices:
    all_trips: List[TripData]# for processing several files i use one big list for FileReader objects
    unprocessed_lines = 0

    def __init__(self, data_reader: List[FileReader]):
        self.all_trips = []
        self.read_data(data_reader)

    def read_data(self, data_reader: List[FileReader]):
        self.all_trips, self.unprocessed_lines = data_reader.file_read()

    def generate_general_stats(self):
        general_stats = []

        trips_amount = self.get_general_trips_amount(self.all_trips)
        max_trip_time = self.get_max_trip_time(self.all_trips)
        bikes_amount = self.get_bikes_amount(self.all_trips)

        general_stats.append([trips_amount, max_trip_time, bikes_amount,])

        self.save_to_csv('general-stats.cvs',
                         ['Total Trip Count', 'Max Trip Time', 'Total Bike Count', 'Unprocessed Rows Count'],
                         general_stats,
                         )


    def get_general_trips_amount(self, trips):
        return len(trips)

    def get_max_trip_time(self, trips):
        max = trips[0].duration
        for i in trips: # range(len(trips) - 1):
          if trips[i].trip_duration > max:
             max = trips[i].trip_duration
        print(f'Самая продолжительная поездка: {max}')
        return max

    def get_bikes_amount(self, trips):
        bikes_set = set()
        for trip in trips:
            bikes_set.add(trip.bike_number)
        return len(bikes_set)

    def save_to_csv(self, filename, tittles, rows: List[str]):
        with open(filename,'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=" ", fieldnames=tittles)
            writer.writeheader()
            writer.writerow(rows)
