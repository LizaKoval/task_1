from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Date:
    def __init__(self, in_start_date, in_end_date):
        self.start_date = self.to_date(in_start_date)
        self.end_date = self.to_date(in_end_date)

    def to_date(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
