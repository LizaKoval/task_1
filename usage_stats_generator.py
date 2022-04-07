from typing import List
from abstractstatsservice import StatsGenerator
from usage_stats_storage import UsageStats
from usage_stats_storage import UsageStat


class UsageStatsCreator(StatsGenerator):
    def __init__(self):
        pass

    def get_stats(self, trips, _unprocessed_data_amount=0) -> List[UsageStats]:
        months = {trip.dates.start_date.month for trip in trips}
        processed_stats = []
        for month in months:
            month_trips = list(filter(lambda trip: trip.dates.start_date.month == month, trips))  # extracting all trips made for the month
            total_amount_of_trips_in_month = self.get_general_trips_amount(month_trips) #super().get_general_trips_amount
            month_stats = UsageStat(month, total_amount_of_trips_in_month)
            processed_stats.append(month_stats)
        usage_stats = UsageStats(processed_stats)
        print("usage_stats is generated")
        return usage_stats