import datetime
from stats_class import Stats
from dataclasses import dataclass

@dataclass()
class UsageStats(Stats):
    month: datetime
    bikes_amount: int