import datetime
from app.stats_storages.stats_class import Stats
from typing import List
from dataclasses import dataclass

@dataclass
class BikeStat:
    bikes_trips_amount: int
    term_of_use: datetime
    bike_number: str

@dataclass()
class BikeStats(Stats):
    stats: List[BikeStat]