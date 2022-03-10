# main.py - is the main interface file
# main.py - главный управляющий файл

import services # module with all calculations and sortings
from trip_data import FileName

# FILENAME = "202003-capitalbikeshare-tripdata.csv"

f1 = FileName('202003-capitalbikeshare-tripdata.csv')

#class Trip:

#   duration = ''
#   start_date = ''
#   end_date = ''
#   start_st_number = ''
#   start_station = ''
#   end_station_number = ''
#   end_station = ''
#   bike_number = ''
#   member_type = ''

#   trips = [] # special list for Trip's objects
#   bikes=0 # bikes counter

#   def __init__(self): # builder
#      pass
  # @staticmethod
  # def trips_number():
    #  trips_number = len(Trip.trips)
    #  return trips_number

   # @staticmethod
   #def bikes_number():
   #   for i in range(len(Trip.trips) - 1):
      #   if (Trip.trips[i].bike_number != Trip.trips[i + 1].bike_number):
        #    Trip.bikes += 1
     # return Trip.bikes

#with open(FILENAME, "r", newline="") as csvfile:
#   reader = csv.DictReader(csvfile, delimiter=',')
#   for row in reader: # reading data from file into Trip's objects
#      t = Trip()
#     t.duration = int(row.get('Duration'))
#      start_date_str = row.get('Start date')
#      t.start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
#      t.end_date = datetime.datetime.strptime(row.get('End date'), "%Y-%m-%d %H:%M:%S")
#      t.start_st_number = int(row.get('Start station number'))
#      t.start_station = row.get('Start station')
#      t.end_station_number = int(row.get('End station number'))
#      t.end_station = row.get('End station')
#      t.bike_number = row.get('Bike number')
#      t.member_type = row.get('Member type')
#      t.trip_duration = t.end_date - t.start_date
#      print(t)                                     # DELETE LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!
#      Trip.trips.append(t)

#trips_number = len(Trip.trips) # total amount of trips: this function
                              # has been already realised as staticmethod for class Trip in line 32
                              # but if i understood clear my task was to clean Trip class from any calculations ...so I did it

# for i in range(len(Trip.trips) - 1): # total amount of bikes used
#   if (Trip.trips[i].bike_number != Trip.trips[i + 1].bike_number):
#      Trip.bikes += 1

# longest_trip=max_time_of_trip(Trip.trips)

#with open('general-stats.csv', "a", newline="") as csvfile:
#    writer = csv.writer(csvfile, delimiter=' ')
#    writer.writerow(['Количество поездок = ', trips_number]) #  3 task part a
#   writer.writerow(["Время самой продолжительной поездки = ", longest_trip])#  3 task part b
#    writer.writerow(['Количество велосипедов за первый квартал = ', Trip.bikes]) #  3 task part c















