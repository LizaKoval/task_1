from typing import Any
from trip_data_reader import FileReader
from abstractstatsservice import StatsGenerator
from general_stats_generator import GeneralStatsCreator
from usage_stats_generator import UsageStatsCreator
from bike_stats_generator import BikeStatsCreator
from writting_factory import Factory

file_reader = FileReader('input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
trips = file_reader.read()
unprocessed_raw_data = file_reader.get_unprocessed_data() # unprocessed data
# generators = (GeneralStatsCreator(), UsageStatsCreator(), BikeStatsCreator()) # objects generating statistics
# stats_storage = map(lambda x: x.get_stats(trips, unprocessed_raw_data), generators)
gen = GeneralStatsCreator()
us=UsageStatsCreator()
bs =  BikeStatsCreator()
stats = gen.get_stats(trips, unprocessed_raw_data)
us_stats = us.get_stats(trips, unprocessed_raw_data)
#bs_stats = bs.get_stats(trips, unprocessed_raw_data)

stats_factory = Factory()
stats_factory_written_result = stats_factory.get_writer(stats).write(stats)
stats_factory_written_result = stats_factory.get_writer(us_stats).write(stats)
#stats_factory_written_result = stats_factory.get_writer(bs_stats).write(stats)
#stats_factory_written_result = map(lambda x: stats_factory.get_writer(x).write(x), stats_storage)


