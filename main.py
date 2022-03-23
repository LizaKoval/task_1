
from services import DataServices
from trip_data_reader import FileReader
from writer import FileWriter
from general_stats_generator import GeneralStatsCreator
from usage_stats_generator import UsageStatsCreator
from bike_stats_generator import BikeStatsCreator

year_file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
files_parser = DataServices(data_readers=[year_file_reader]) # object of instruments for processing data

general_stats_creation = GeneralStatsCreator(files_parser)
general_stats_file = FileWriter('output/general-stats.csv', general_stats_creation)

usage_stats = UsageStatsCreator(files_parser)
usage_stats_file = FileWriter('output/usage-stats.csv', usage_stats)

bike_stats = BikeStatsCreator(files_parser)
bike_stats_file = FileWriter('output/bike-stats.csv', bike_stats)

