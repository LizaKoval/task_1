import csv
from functools import reduce
# from functools import filter
from typing import List

from trip_data import TripData
from trip_data import FileReader


class DataServices:
    all_trips: List[TripData]# for processing several files i use one big list for FileReader objects
    unprocessed_count: int = 0

    def __init__(self, data_readers: List[FileReader]) -> None:
        self.all_trips = []
        self.get_data_from_readers(data_readers)

    def get_data_from_readers(self, data_readers: List[FileReader]):
        for reader in data_readers:
            all_trips, unprocessed_count = reader.file_read()
            self.all_trips.extend(all_trips)
            self.unprocessed_count += unprocessed_count

    def generate_general_stats(self):
        general_stats = []

        trips_amount = self.get_general_trips_amount(self.all_trips)
        max_trip_time = self.get_max_trip_time(self.all_trips)
        bikes_amount = self.get_bikes_amount(self.all_trips)

        general_stats.append([trips_amount, max_trip_time, bikes_amount, self.unprocessed_count])

        tittles = ['Total Trip Count', 'Max Trip Time', 'Total Bike Count', 'Unprocessed Rows Count']

        self.save_to_csv('general-stats.csv',
                         tittles,
                         general_stats,
                         )

    def get_general_trips_amount(self, trips):
        return len(trips)

    def get_max_trip_time(self, trips):
        model_trip = trips[0]
        trip_time = reduce(lambda x, trip: max(x, trip.end_date - trip.start_date), trips[1:], model_trip.end_date - model_trip.start_date) # finding max value of trip duration
        return str(trip_time) # between x & trip.end - trip.start в trips, where х = model_trip.end_date - model_trip.start_date
                         # and found maximal value accumulates

    def get_bikes_amount(self, trips):
        bikes_set = set()
        for trip in trips:
            bikes_set.add(trip.bike_number)
        return len(bikes_set)

    def save_to_csv(self, filename, header: List[str], rows: List[str]):
        with open(filename,'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=" ")
            writer.writerow(header)
            writer.writerows(rows)

    def generate_usage_stats(self):
        months = {trip.start_date.month for trip in self.all_trips}
        monthly_stats = []
        tittles = ['Month', 'Trips amount']

        for month in months:
            month_trips = list(self.get_trips_per_month(self.all_trips, month)) # extracting all trips made for the month
            total_amount_of_trips_in_month = self.get_general_trips_amount(month_trips)
            monthly_stats.append([month, total_amount_of_trips_in_month])

        self.save_to_csv("usage-stats.csv", tittles, monthly_stats)

    def get_trips_per_month(self, all_trips, month):
        required_trips = []
        for trip in all_trips:
            if trip.start_date.month == month:
                required_trips.append(trip)
    # TODO: try to do THIS METHOD BY using filter() and lambda()
        # required_trips = list(filter(lambda trip, month: trip.start_date.month == month, all_trips, month)
        return required_trips
