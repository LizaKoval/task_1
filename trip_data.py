from dataclasses import dataclass
from datetime import datetime
from date import Date

@dataclass() # class for storing data, and it has unseen default methods btw i can use __slots__ for storing fields and when executing it will let us use less store and give faster access to the fields
class TripData:
   duration: int
   dates: Date
   start_st_number: int
   start_station: str
   end_station_number: int
   end_station: str
   bike_number: str
   member_type: str



