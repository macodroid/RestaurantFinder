import csv
import re

import enum_days
from datetime import datetime


class DataLoader:
    def __int__(self, data):
        self.data = data
        self.data_header = None

    def _load_data_source1(self, data_source_csv):
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
                        days = d_value.strip().split(',')
                        time_dict = {self.data_header[3]: {}, self.data_header[4]: {}}
                        for day in days:
                            day_int = enum_days.Days[day].value
                            time_dict[self.data_header[3]][day_int] = open_time
                            time_dict[self.data_header[4]][day_int] = close_time
                        restaurant_info[restaurant_name].update(time_dict)
                    elif self.data_header[6] == d_key:
                        restaurant_info[restaurant_name][self.data_header[6]] = int(d_value)
                    elif self.data_header[7] == d_key:
                        restaurant_info[restaurant_name][self.data_header[7]] = int(d_value)
        return restaurant_info

    def _parse_time(self, str_time):
        working_hours = []
        hours = re.search("\\d*:*\\d+ [ap]m - \\d*:*\\d+ [ap]m", str_time)
        parsed_time = hours.group().split('-')
        for t in parsed_time:
            if ':' in t:
                time_format = '%I:%M %p'
            else:
                time_format = '%I %p'
            working_hours.append(datetime.strptime(t.strip(), time_format).time())
        return working_hours[0], working_hours[1]

    def _parse_days(self, str_days):
        code_days = []
        days = re.search("([a-zA-Z]{3}, )?([a-zA-Z]{3})(-[a-zA-Z]{3})*(, [a-zA-Z]{3})?", str_days)
        days = days.group().split(',')
        for d in days:
            if '-' in d:
                code_days.extend(self._get_range_of_days(d.strip()))
            else:
                code_days.append(enum_days.Days[d.strip()].value)
        return code_days

    def _get_range_of_days(self, range_of_days):
        days = range_of_days.split('-')
        start_day = enum_days.Days[days[0]].value
        end_day = enum_days.Days[days[1]].value
        return [i for i in range(start_day, end_day + 1)]

    def _load_data_source2(self, data_source_csv: str) -> dict:
        restaurant_info = {}
        with open(data_source_csv, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for restaurant_name, time in csv_reader:
                restaurant_name = restaurant_name.strip()
                restaurant_info[restaurant_name] = {}
                for t in time.split('/'):
                    opens, closes = self._parse_time(t)
                    days = self._parse_days(t)
                    r_d = {'opens': {}, 'closes': {}}
                    for d in days:
                        r_d['opens'][d] = opens
                        r_d['closes'][d] = closes
                    restaurant_info[restaurant_name].update(r_d)
        return restaurant_info

    def import_data(self, sources: list):
        _restaurant_info = {}
        _restaurant_info.update(self._load_data_source1(sources[0]))
        _restaurant_info.update(self._load_data_source2(sources[1]))
        return _restaurant_info
