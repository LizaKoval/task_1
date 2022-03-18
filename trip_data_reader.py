import csv
import datetime
from typing import List
from trip_data import TripData

class FileReader:

   filename = ''

   def __init__(self, filename):
      self.filename = filename

   def file_read(self) -> List[TripData]: # returns the list of TripData objects read from data
      rows = []                           # and number of errors while reading a file
      unprocessed_counter = 0

      with open(self.filename, "r") as csvfile:
         reader = csv.DictReader(csvfile, delimiter=',')
         for row in reader:  # reading data from file into Trip's objects
            try:
               t = TripData()
               t.duration = int(row.get('Duration'))
               t.start_date = datetime.datetime.strptime(row.get('Start date'), "%Y-%m-%d %H:%M:%S") # !!!!!!!!!!!!!!!!! WRITE METHOD FOR FORMATTING TYPES
               t.end_date = datetime.datetime.strptime(row.get('End date'), "%Y-%m-%d %H:%M:%S")
               t.start_st_number = int(row.get('Start station number'))
               t.start_station = row.get('Start station')
               t.end_station_number = int(row.get('End station number'))
               t.end_station = row.get('End station')
               t.bike_number = row.get('Bike number')
               t.member_type = row.get('Member type')
               t.trip_duration = t.end_date - t.start_date
               print(t)  # TODO: DELETE LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!
               rows.append(t)

            except(TypeError, ValueError, KeyError): # if some errors happen, we will count them in unprocessed_counter
               unprocessed_counter += 1
               print(f'Ошибка чтения в файле {self.filename}')

      return rows, unprocessed_counter

