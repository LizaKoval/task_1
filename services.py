import csv
from functools import reduce
from typing import List

from trip_data import TripData
from trip_data_reader import FileReader


class DataService:
    all_trips: List[TripData]# for processing several files i use one big list of FileReader objects
    unprocessed_count: int = 0

    def __init__(self, data_readers: List[FileReader]) -> None:
        self.all_trips = []
        self.get_data_from_readers(data_readers)

    def get_data_from_readers(self, data_readers: List[FileReader]): # List[FileReader] is the list of FileReader objects for reading more then 1 file
        for reader in data_readers:
            all_trips, unprocessed_count = reader.read() # list of strings read from a particular file(aka list of TripData objects)
            self.all_trips.extend(all_trips)

            self.unprocessed_count += unprocessed_count
        return self.all_trips, self.unprocessed_count



