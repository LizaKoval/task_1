import csv
import datetime # used for dates
from typing import List

class TripData: # main class with data read from csv file

   duration: int
   start_date: datetime
   end_date: datetime
   start_st_number: int
   start_station: str
   end_station_number: int
   end_station: str
   bike_number: str
   member_type: str

   def __init__(self): # builder
      pass

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
               print(t)  # DELETE LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!
               rows.append(t)

            except(TypeError, ValueError, KeyError): # if some errors happen, we will count them
               unprocessed_counter += 1
               print(f'Ошибка чтения в файле {self.filename}')

      return rows, unprocessed_counter


class ResultSaver: # class for saving processed data in final files

   def __init__(self, filename):
      self.filename = filename

   def file_write(self):
      with open(self.filename, "a", newline="") as csvfile:
         writer = csv.writer(csvfile, delimiter=' ')
         writer.writerow([self.statement, self.result])

class MonthlyFileReader:
   pass