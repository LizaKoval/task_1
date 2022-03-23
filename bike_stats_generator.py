from functools import reduce
from services import DataServices

class BikeStatsCreator(DataServices):
    tittles = ['Total of trips', 'Term of use', 'Bike number']
    stats = [] # processed bike statistics

    def __init__(self, obj):
        self.all_trips = obj.all_trips
        bikes_stats = self.gather_bike_stats() # not sorted processed bike statistics
        self.stats = self.sort_data(bikes_stats)

    def gather_bike_stats(self):
        bikes = {trip.bike_number for trip in self.all_trips}  # made the set of unique bikes
        bike_stats = []
        for bike in bikes:
            bike_trips = list(filter(lambda trip: trip.bike_number == bike, self.all_trips)) # all trips list made by 1 particular bike
            total_bike_trips_amount = self.get_general_trips_amount(bike_trips)
            bike_term_of_use = self.get_time_of_all_bike_trips(bike_trips)
            bike_stats.append([total_bike_trips_amount,bike_term_of_use, bike])
        return bike_stats

    def get_time_of_all_bike_trips(self, bike_trips): # returns term of use of particular bike
        model_trip = bike_trips[0]
        term_of_use = reduce(lambda x, trip: x + (trip.end_date-trip.start_date), bike_trips[:1], model_trip.end_date - model_trip.start_date)
        return term_of_use

    def sort_data(self, processed_bikes_list):
        sorted_bike_stats = sorted(processed_bikes_list, key=lambda x: x[0], reverse=True)
        return sorted_bike_stats