import data_loader
from data_loader import *

list_of_restaurants = ["data/restaurants-hours-source-1.csv", "data/restaurants-hours-source-2.csv"]

dl = data_loader.DataLoader()
p = dl.import_data(list_of_restaurants)
for i in p:
    try:
        if p[i]['opens']['Mo'] <= datetime(2020, 1, 1, 9, 30).time():
            print(p[i])
    except:
        pass
