import datetime # used for dates
from dataclasses import dataclass

@dataclass #class with data structure
class TripData: # main class with data read from csv file

   duration: int
   start_date: datetime # special format for dates and time
   end_date: datetime
   start_st_number: int
   start_station: str
   end_station_number: int
   end_station: str
   bike_number: str
   member_type: str

   def __init__(self): # builder
      pass
