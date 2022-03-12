# main.py - is the main interface file
# main.py - главный управляющий файл

import services # module with all calculations and sortings
from trip_data import FileReader
from services import DataServices
file1 = FileReader('202003-capitalbikeshare-tripdata.csv')
file1.file_read()


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















