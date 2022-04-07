from app.data_readers.trip_data_reader import FileReader
from app.generators.general_stats_generator import GeneralStatsGenerator
from app.generators.usage_stats_generator import UsageStatsGenerator
from app.generators.bike_stats_generator import BikeStatsGenerator
from app.data_writers.writting_factory import Factory

file_reader = FileReader('data/input_data/2014Q4-capitalbikeshare-tripdata.csv') # data object
trips = file_reader.read()
unprocessed_raw_data = file_reader.get_unprocessed_data() # unprocessed data
generators = [GeneralStatsGenerator(), UsageStatsGenerator(), BikeStatsGenerator()] # objects generating statistics
stats_storage = list(map(lambda x: x.get_stats(trips, unprocessed_raw_data), generators))
stats_factory = Factory()
stats_factory_written_result = list(map(lambda x: stats_factory.get_writer(x).write(x), stats_storage))


