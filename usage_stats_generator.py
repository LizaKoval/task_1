from functools import reduce
from services import DataServices

class UsageStatsCreator(DataServices):
    tittles = ['Month', 'Trips amount']
    stats = []

    def __init__(self, obj):
        self.all_trips = obj.all_trips
        self.gather_usage_stats()

    def gather_usage_stats(self):
        months = {trip.start_date.month for trip in self.all_trips}

        for month in months:
            month_trips = list(filter(lambda trip: trip.start_date.month == month, self.all_trips))  # extracting all trips made for the month
            total_amount_of_trips_in_month = self.get_general_trips_amount(month_trips)
            self.stats.append([month, total_amount_of_trips_in_month])
