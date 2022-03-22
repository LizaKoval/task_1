# main.py - is the main interface file
from services import DataServices
from trip_data_reader import FileReader
from writer import FileWriter
from general_stats_generator import GeneralStatsCreator

year_file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
files_processing_instruments = DataServices(data_readers=[year_file_reader]) # object of instruments for processing data
general_stats_creation = GeneralStatsCreator()
general_stats_file = FileWriter('output/general-stats.csv', general_stats_creation.tittles, general_stats_creation.general_stats)


#files_processing_instruments.generate_usage_stats()
#files_processing_instruments.generate_bike_stats()
#files_processing_instruments.generate_usage_stats()
