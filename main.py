from services import DataService
from trip_data_reader import FileReader
from abstractstatsservice import StatsGenerator
from general_stats_generator import GeneralStatsCreator
from usage_stats_generator import UsageStatsCreator
from bike_stats_generator import BikeStatsCreator
from writting_factory import Factory

file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
trips = file_reader.read()
unprocessed_raw_data = file_reader.get_unprocessed_data() # unprocessed data
generators = [GeneralStatsCreator(), UsageStatsCreator(), BikeStatsCreator()] # objects generating statistics
stats_storage = [map(lambda x: x.get_stats(trips, unprocessed_raw_data), generators)]
stats_factory = Factory()
stats_factory_written_result = map(lambda x: stats_factory.get_writer(x).write(x), stats_storage)


# stats = [
#     { "filename": "output/general-stats.csv", "obj": general_stats_creation, },
#     {  "filename": "output/usage-stats.csv", "obj": usage_stats},
#     { "filename": "output/bike-stats.csv", "obj": bike_stats, }
# ]

