from functools import reduce
from abstractstatsservice import StatsGenerator
from services import DataService

class GeneralStatsCreator(DataService, StatsGenerator):
    titles = ['Total Trip Count', 'Max Trip Time', 'Total Bike Count',
              'Unprocessed Rows Count']# for output file header
    stats = []

    def __init__(self, obj):
        self.all_trips = obj.all_trips
        self.unprocessed_count = obj.unprocessed_count
        self.gather_stats()

    def gather_stats(self):
        trips_amount = self.get_general_trips_amount(self.all_trips)
        max_trip_time = self.get_max_trip_time(self.all_trips)
        bikes_amount = self.get_bikes_amount(self.all_trips)

        self.stats.append([trips_amount, max_trip_time, bikes_amount, self.unprocessed_count])

    def get_max_trip_time(self, trips):
        model_trip = trips[0]
        trip_time = reduce(lambda x, trip: max(x, trip.end_date - trip.start_date), trips[1:],
                           model_trip.end_date - model_trip.start_date)  # finding max value of trip duration
        return str(
            trip_time)  # between x & trip.end - trip.start в trips, where х = model_trip.end_date - model_trip.start_date
        # and found maximal value accumulates

    def get_bikes_amount(self, trips):
        bikes_set = set()
        for trip in trips:
            bikes_set.add(trip.bike_number)
        return len(bikes_set)
