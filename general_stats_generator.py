from functools import reduce
from abstractstatsservice import StatsGenerator
from general_stats_storage import GeneralStats

class GeneralStatsCreator(StatsGenerator):
    def __init__(self):
        pass

    def get_stats(self, trips, unprocessed_data_amount) -> GeneralStats:
        trips_amount = self.get_general_trips_amount(trips)
        max_trip_time = self.get_max_trip_time(trips)
        bikes_amount = self.get_bikes_amount(trips)

        general_stats_obj = GeneralStats(trips_amount, max_trip_time, bikes_amount, unprocessed_data_amount)
        print("gen_stats is generated")
        return general_stats_obj

    def get_max_trip_time(self, trips):
        model_trip = trips[0]
        max_trip_time = reduce(lambda x, trip: max(x, trip.dates.end_date - trip.dates.start_date), trips[1:], # x accumulates the reault of
                           model_trip.dates.end_date - model_trip.dates.start_date)  # finding max value of trip duration
        return max_trip_time  # between x & trip.end - trip.start в trips, where х = model_trip.end_date - model_trip.start_date
        # and found maximal value accumulates

    def get_bikes_amount(self, trips):
        bikes_set = set()
        for trip in trips:
            bikes_set.add(trip.bike_number)
        return len(bikes_set)
