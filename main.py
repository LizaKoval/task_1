# main.py - is the main interface file
from services import DataServices
from trip_data import FileReader

year_file_reader = FileReader('202003-capitalbikeshare-tripdata.csv') # data object
files_processing_instruments = DataServices(year_file_reader) # object of instruments for processing data

files_processing_instruments.generate_general_stats()