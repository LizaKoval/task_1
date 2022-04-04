import csv
import datetime
from typing import List
from trip_data import TripData


class FileReader:

    def __init__(self, filename) -> None:
        self.filename = filename
        self.unprocessed_count = 0

    def read(self) -> List[TripData]:
        rows = []
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                try:
                    td = TripData(
                        duration=int(row['Duration']),
                        start_date=to_date(row['Start date']),
                        end_date=to_date(row['End date']),
                        start_st_number=int(row['Start station number']),
                        start_station=row['Start station'],
                        end_station_number=int(row['End station number']),
                        end_station=row['End station'],
                        bike_number=row['Bike number'],
                        member_type=row['Member type'],
                    )
                    rows.append(td)
                except (ValueError, TypeError, KeyError):
                    # TODO: открыть стр.34
                    self.unprocessed_count += 1
                    # print("Ошибка чтения файлов")
        return rows

    def get_unprocessed_data(self):
        return self.unprocessed_count

def to_date(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')