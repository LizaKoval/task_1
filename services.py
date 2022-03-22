import csv
from functools import reduce
# from functools import filter
from typing import List

from trip_data import TripData
from trip_data_reader import FileReader


class DataServices:
    all_trips: List[TripData]# for processing several files i use one big list of FileReader objects
    unprocessed_count: int = 0

    def __init__(self, data_readers: List[FileReader]) -> None:
        self.all_trips = []
        self.get_data_from_readers(data_readers)

    def get_data_from_readers(self, data_readers: List[FileReader]): # List[FileReader] is the list of FileReader objects for reading more then 1 file
        for reader in data_readers:
            all_trips, unprocessed_count = reader.file_read() # list of strings read from a particular file(aka list of TripData objects)
            self.all_trips.extend(all_trips)

            self.unprocessed_count += unprocessed_count
        return self.all_trips, self.unprocessed_count


        #self.save_to_csv('output/general-stats.csv',
        #                 tittles,
        #                 general_stats,
        #                 )

    def get_general_trips_amount(self, trips): # used by daughter classes
        return len(trips)


    def save_to_csv(self, filename, header: List[str], rows: List[str]):
        with open(filename,'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(header)
            writer.writerows(rows)

    def generate_usage_stats(self):
        months = {trip.start_date.month for trip in self.all_trips}
        monthly_stats = []
        tittles = ['Month', 'Trips amount']

        for month in months:
            month_trips = list(filter(lambda trip: trip.start_date.month == month, self.all_trips)) # extracting all trips made for the month
            total_amount_of_trips_in_month = self.get_general_trips_amount(month_trips)
            monthly_stats.append([month, total_amount_of_trips_in_month])

        self.save_to_csv("output/usage-stats.csv", tittles, monthly_stats)

    def generate_bike_stats(self):
        bikes = {trip.bike_number for trip in self.all_trips} # made the set of unique bikes
        bikes_stats = []
        tittles = ['Total of trips', 'Term of use', 'Bike number']

        for bike in bikes:
            bike_trips = list(filter(lambda trip: trip.bike_number == bike, self.all_trips)) # all trips list made by 1 particular bike
            total_bike_trips_amount = self.get_general_trips_amount(bike_trips)
            bike_term_of_use = self.get_time_of_all_bike_trips(bike_trips)
            bikes_stats.append([total_bike_trips_amount,bike_term_of_use, bike])

        sorted_bike_stats = sorted(bikes_stats, key=lambda x: x[0], reverse=True)

        self.save_to_csv('output/bike-stats.csv', tittles, sorted_bike_stats)

    def get_time_of_all_bike_trips(self, bike_trips): # returns term of use of particular bike
        model_trip = bike_trips[0]
        term_of_use = reduce(lambda x, trip: x + (trip.end_date-trip.start_date), bike_trips[:1], model_trip.end_date - model_trip.start_date)
        return term_of_use

