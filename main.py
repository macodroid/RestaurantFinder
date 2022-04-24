import data_loader
from data_loader import *

list_of_restaurants = ["data/restaurants-hours-source-1.csv", "data/restaurants-hours-source-2.csv"]

dl = data_loader.DataLoader()
p = dl.import_data(list_of_restaurants)
# for i in p:
#     try:
#         if p[i]['opens']['Mo'] <= datetime(2020, 1, 1, 9, 30).time():
#             print(p[i])
#     except:
#         pass
# import re
#
# s1 = "Sun, Mon-Thu  11:30 am - 9 pm"
# s2 = "Mon-Thu, Sun  11:30 am - 9 pm"
# s3 = "Sun  11:30 am - 9 pm"
# hours = re.search("\\d*:*\\d+ [ap]m - \\d*:*\\d+ [ap]m", s1)
# a = hours.group()
#
# days1 = re.search("([a-zA-Z]{3}, )?([a-zA-Z]{3})(-[a-zA-Z]{3})*(, [a-zA-Z]{3})?", s1)
# days2 = re.search("([a-zA-Z]{3}, )?([a-zA-Z]{3})(-[a-zA-Z]{3})*(, [a-zA-Z]{3})?", s2)
# days3 = re.search("([a-zA-Z]{3}, )?([a-zA-Z]{3})(-[a-zA-Z]{3})*(, [a-zA-Z]{3})?", s3)
# b1 = days1.group()
# b2 = days2.group()
# b3 = days3.group()
#
# day1 = re.search("-{0}?[a-zA-Z]{3}-{0}?", s1)
# day2 = re.search("-{0}?[a-zA-Z]{3}-{0}?", s2)
# pass
# time 10 am  - 9 pm
# /\d*:*\d+ [ap]m - \d*:*\d+ [ap]m/

# days Mon-Sun
# /[a-z]{3}-[a-z]{3}/i

# Single day
#  /([a-zA-Z]{3})/g
