from dataclasses import dataclass
from datetime import datetime


@dataclass
class TripData:
   duration: int
   start_date: datetime
   end_date: datetime
   start_st_number: int
   start_station: str
   end_station_number: int
   end_station: str
   bike_number: str
   member_type: str