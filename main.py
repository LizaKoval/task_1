from services import DataService
from trip_data_reader import FileReader
from writer import FileWriter
from abstractstatsservice import StatsGenerator
from general_stats_generator import GeneralStatsCreator
from usage_stats_generator import UsageStatsCreator
from bike_stats_generator import BikeStatsCreator

file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
#TODO: delete it later files_parser = DataService(data_readers=[year_file_reader]) # object of instruments for extracting data
all_trips = file_reader.read()
#TODO: DECIDE how to collect unptocessed data: unprocessed_raw_data = file_reader.get_unprocessed_data() # unprocessed data

generators = [GeneralStatsCreator(),]# objects generating statistics


#general_stats_creation = GeneralStatsCreator(files_parser)
#usage_stats = UsageStatsCreator(files_parser)
#bike_stats = BikeStatsCreator(files_parser)

stats = [
    { "filename": "output/general-stats.csv", "obj": general_stats_creation, },
    {  "filename": "output/usage-stats.csv", "obj": usage_stats},
    { "filename": "output/bike-stats.csv", "obj": bike_stats, }
]

def Output_data(stats):
    def creates_writer(x):
        temp = FileWriter(stats[x]['filename'], stats[x]['obj'])
    return map(creates_writer, stats)

Output_data(stats)

#stats_written = map(lambda stats_obj, x: FileWriter(stats_obj[x]['filename'], stats_obj[x]['obj']), range(0,len(stats)), stats)

#general_stats_file = FileWriter('output/general-stats.csv', general_stats_creation)


#usage_stats_file = FileWriter('output/usage-stats.csv', usage_stats)


#bike_stats_file = FileWriter('output/bike-stats.csv', bike_stats)

#TODO: ИСПРАВИТЬ ВЫВОД - ЗАПЯТЫЕ