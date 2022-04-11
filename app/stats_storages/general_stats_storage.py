import datetime
from app.stats_storages.stats_class import Stats
from dataclasses import dataclass

@dataclass()
class GeneralStats(Stats):
    trips_amount: int
    max_trip_time: datetime
    bikes_amount: int
    unprocessed_count: int
