import csv
class FileWriter:

    def __init__(self, filename, obj):
        self.write_in_file(filename, obj.tittles, obj.stats)

    def write_in_file(self, filename, tittles, stats):
        with open(filename,'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(tittles)
            writer.writerows(stats)