import datetime
from stats_class import Stats
from dataclasses import dataclass

@dataclass()
class BikeStats(Stats):
    bikes_trips_amount: int
    term_of_use: datetime
    bike_number: str