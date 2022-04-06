import datetime
from stats_class import Stats
from typing import List
from dataclasses import dataclass

@dataclass
class UsageStat:
    month: datetime
    bikes_amount: int

@dataclass()
class UsageStats(Stats):
    stats: List[UsageStat]