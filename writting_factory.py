from typing import List

from bike_stats_storage import BikeStats
from general_stats_storage import GeneralStats
from usage_stats_storage import UsageStats
from write_in_file import GeneralStatsWriter, UsageStatsWriter, BikeStatsWriter


class Factory:
    writers = {
        GeneralStats: GeneralStatsWriter('output/general-stats.csv'),
        UsageStats: UsageStatsWriter("output/usage-stats.csv"),
        BikeStats: BikeStatsWriter("output/bike-stats.csv")
    }

    def get_writer(self, obj) -> GeneralStatsWriter:
        return self.writers[type(obj)]