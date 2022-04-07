from app.stats_storages.bike_stats_storage import BikeStats
from app.stats_storages.general_stats_storage import GeneralStats
from app.stats_storages.usage_stats_storage import UsageStats
from app.data_writers.write_in_file import GeneralStatsWriter, UsageStatsWriter, BikeStatsWriter

class Factory:
    writers = {
        GeneralStats: GeneralStatsWriter('app/data/output/general-stats.csv'),
        UsageStats: UsageStatsWriter("app/data/output/usage-stats.csv"),
        BikeStats: BikeStatsWriter("app/data/output/bike-stats.csv")
    }

    def get_writer(self, obj) -> GeneralStatsWriter:
        return self.writers[type(obj)]