import main
from trip_data import TripData

class DataServices(TripData):

    def find_all_trips_amount(self, arr):
        # self.counter = len(arr)
        # return self.counter
        self.counter = 0
        for i in arr:
            self.counter += 1
        print('Количество поездок', self.counter)
        return self.counter

#def max_time_of_trip(arr): # finding the longest ride in the file
#   max_ = arr[0].trip_duration
#   k=0
#   for i in range(len(arr) - 1):
#      if arr[i].trip_duration > max_:
#         max_=arr[i].trip_duration
#   print(f'Самая продолжительная поездка: {max_} ')
#   return max_
