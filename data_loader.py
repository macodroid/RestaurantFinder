import csv
from datetime import datetime


class DataLoader:
    def __int__(self, data):
        self.data = data
        self.data_header = None

    def _load_data_source1(self, data_source_csv: str) -> dict[dict]:
        restaurant_info = {}
        with open(data_source_csv, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            self.data_header = [str.strip(i.lower()) for i in next(csv_reader)]
            for row in csv_reader:
                restaurant_name = None
                open_time, close_time = None, None
                for d_key, d_value in row.items():
                    d_key = d_key.lower().strip()
                    d_value = d_value.strip()
                    if self.data_header[0] == d_key:
                        restaurant_name = d_value
                        restaurant_info[restaurant_name] = {}
                    elif self.data_header[2] == d_key:
                        restaurant_info[restaurant_name][self.data_header[2]] = d_value
                    elif self.data_header[3] == d_key:
                        open_time = datetime.strptime(d_value.strip(), '%H:%M:%S').time()
                    elif self.data_header[4] == d_key:
                        close_time = datetime.strptime(d_value.strip(), '%H:%M:%S').time()
                    elif self.data_header[5] == d_key:
                        # TODO !!!SMELL!!! change variable name
                        p = d_value.strip().split(',')
                        time_dict = {self.data_header[3]: {}, self.data_header[4]: {}}
                        for day in p:
                            time_dict[self.data_header[3]][day] = open_time
                            time_dict[self.data_header[4]][day] = close_time
                        restaurant_info[restaurant_name].update(time_dict)
                    elif self.data_header[6] == d_key:
                        restaurant_info[restaurant_name][self.data_header[6]] = int(d_value)
                    elif self.data_header[7] == d_key:
                        restaurant_info[restaurant_name][self.data_header[7]] = int(d_value)
                    # TODO add location and description
        return restaurant_info

    def _load_data_source1(self, data_source_csv: str) -> dict[dict]:
        restaurant_info = {}
        with open(data_source_csv, mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')

    def import_data(self, sources: list[str]):
        return self._load_data_source1(sources[0])
