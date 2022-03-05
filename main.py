import csv
# import datetime # буду использовать для считывания формата даты

FILENAME = "202003-capitalbikeshare-tripdata.csv"

class Trip:

   duration = ''
   start_date = ''
   end_date = ''
   start_st_number = ''
   start_station = ''
   end_station_number = ''
   end_station = ''
   bike_number = ''
   member_type = ''

   trips = [] # массив объектов
   bikes=0 # счётчик байков

   def __init__(self): # конструктор
     pass

   @staticmethod
   def trips_number():
      trips_number = len(Trip.trips)
      return trips_number

   @staticmethod
   def bikes_number():
      for i in range(len(Trip.trips) - 1):
         if (Trip.trips[i].bike_number != Trip.trips[i + 1].bike_number):
            Trip.bikes += 1
      return Trip.bikes

with open(FILENAME, "r", newline="") as csvfile:
   reader = csv.DictReader(csvfile, delimiter=',')
   for row in reader: # пытаюсь прочитать данные из файла в объект класса Trip
      t = Trip()
      t.duration = int(row.get('Duration'))
      t.start_date = row.get('Start date')
      t.end_date = row.get('End date')
      t.start_st_number = int(row.get('Start station number'))
      t.start_station = row.get('Start station')
      t.end_station_number = int(row.get('End station number'))
      t.end_station = row.get('End station')
      t.bike_number = row.get('Bike number')
      t.member_type = row.get('Member type')
      print(t)                                     # УДАЛИТЬ ПОТОМ!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      Trip.trips.append(t)

with open('general-stats.csv', "a", newline="") as csvfile:
     writer = csv.writer(csvfile, delimiter=' ') # delimiter - это разделитель, по умолчанию была бы запятая, но она не нужна
     writer.writerow(['Количество поездок = ', Trip.trips_number()]) #  3 ЗАДАНИЕ_1 ЧАСТЬ
     writer.writerow(['Количество велосипедов за первый квартал = ', Trip.bikes_number()]) #  3 ЗАДАНИЕ_3 ЧАСТЬ















