import csv
import datetime # used for dates
import services # users module with all necessary
                # instruments(methods)

class TripData: # main class with data read from csv file

   duration = ''
   start_date = ''
   end_date = ''
   start_st_number = ''
   start_station = ''
   end_station_number = ''
   end_station = ''
   bike_number = ''
   member_type = ''

   trips = [] # special list for Trip's objects
   bikes=0 # bikes counter

   def __init__(self): # builder
      pass


class FileReader:

   def __init__(self, filename):
      self.filename = filename

   def file_read(self):
      with open(self.filename, "r", newline="") as csvfile:
         reader = csv.DictReader(csvfile, delimiter=',')
         for row in reader:  # reading data from file into Trip's objects
            t = TripData()
            t.duration = int(row.get('Duration'))
            start_date_str = row.get('Start date')
            t.start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
            t.end_date = datetime.datetime.strptime(row.get('End date'), "%Y-%m-%d %H:%M:%S")
            t.start_st_number = int(row.get('Start station number'))
            t.start_station = row.get('Start station')
            t.end_station_number = int(row.get('End station number'))
            t.end_station = row.get('End station')
            t.bike_number = row.get('Bike number')
            t.member_type = row.get('Member type')
            t.trip_duration = t.end_date - t.start_date
            print(t)  # DELETE LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            TripData.trips.append(t)

class ResultSaver: # class for saving processed data in final files

   def __init__(self, filename, statement, result):
      self.filename = filename
      self.statement = statement
      self.result = result

   def file_write(self):
      with open(self.filename, "a", newline="") as csvfile:
         writer = csv.writer(csvfile, delimiter=' ')
         writer.writerow([self.statement, self.result])

class MonthlyFileReader:
   pass