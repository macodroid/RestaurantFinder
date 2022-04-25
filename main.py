import data_loader
import restaurant_finder
import datetime

"""
TODO: ticket parking
"""

if __name__ == "__main__":
    list_of_restaurants = ["data/restaurants-hours-source-1.csv", "data/restaurants-hours-source-2.csv"]
    dl = data_loader.DataLoader()
    restaurants = dl.import_data(list_of_restaurants)
    rf = restaurant_finder.RestaurantFinder(restaurants)

    print("Welcome to the Restaurant Finder. Here You can find the working "
          "hours of restaurant that You are interested in or some another information")
    t = datetime.time(1, 0)
    day_of_week = 0
    open_restaurants = rf.opened_restaurants()
    pass