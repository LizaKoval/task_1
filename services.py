import main

def max_time_of_trip(arr): # finding the longest ride in the file
   max_ = arr[0].trip_duration
   k=0
   for i in range(len(arr) - 1):
      if arr[i].trip_duration > max_:
         max_=arr[i].trip_duration
   print(f'Самая продолжительная поездка: {max_} ')
   return max_