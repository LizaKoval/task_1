# main.py - is the main interface file
from services import DataServices
from trip_data_reader import FileReader

year_file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
files_processing_instruments = DataServices(data_readers=[year_file_reader]) # object of instruments for processing data

files_processing_instruments.generate_general_stats()
files_processing_instruments.generate_usage_stats()
files_processing_instruments.generate_bike_stats()
files_processing_instruments.generate_usage_stats()
