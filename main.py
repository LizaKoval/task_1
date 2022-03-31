
from services import DataService
from trip_data_reader import FileReader
from writer import FileWriter
from abstractstatsservice import StatsGenerator
from general_stats_generator import GeneralStatsCreator
from usage_stats_generator import UsageStatsCreator
from bike_stats_generator import BikeStatsCreator

year_file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
files_parser = DataService(data_readers=[year_file_reader]) # object of instruments for extracting data

general_stats_creation = GeneralStatsCreator(files_parser)
usage_stats = UsageStatsCreator(files_parser)
bike_stats = BikeStatsCreator(files_parser)

stats = [
    { "obj": general_stats_creation, "filename": "output/general-stats.csv"},
    { "obj": usage_stats, "filename": "output/usage-stats.csv"},
    { "obj": bike_stats, "filename": "output/bike-stats.csv"}
]

stats_written = map(lambda stats_obj, x: FileWriter(stats_obj[x]['filename'], stats_obj[x]['obj']), range(0,len(stats)), stats)

#general_stats_file = FileWriter('output/general-stats.csv', general_stats_creation)


#usage_stats_file = FileWriter('output/usage-stats.csv', usage_stats)


#bike_stats_file = FileWriter('output/bike-stats.csv', bike_stats)

#TODO: ИСПРАВИТЬ ВЫВОД - ЗАПЯТЫЕ