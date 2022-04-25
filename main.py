import data_loader
from data_loader import *

"""
TODO: ticket parking
1. if closing hours are on the border to the next day 00:00:00
"""


def opened_restaurants(restaurants, time=None, day_of_the_week=None):
    """
    Search which restaurants are opened. If time and day_of_the_week is not specified current values are used.
    Current time and day of the week today. \n
    :param dict restaurants: map of restaurants
    :param time: search which restaurant are opened at specific time
    :param int day_of_the_week: search which restaurant are opened at specific day of the week
    :rtype: None
    """
    if time is None and day_of_the_week is None:
        day_of_the_week = datetime.today().weekday()
        time = datetime.now().time()

    for restaurant in restaurants:
        try:
            opens = restaurants[restaurant]['opens'][day_of_the_week]
            closes = restaurants[restaurant]['closes'][day_of_the_week]
            # first basic case that entered time is in interval of opens < time < closes
            # open < close && open <= time && time < close
            if opens < closes and opens <= time < closes:
                print(restaurant)
            # second case closing hours is till next day
            elif opens > closes:
                # restrict the day_of_the_week from jumping out of the interval  <0,6>
                day_of_the_week = (day_of_the_week - 1) % 7
                previous_day_closes = restaurants[restaurant]['closes'][day_of_the_week]
                previous_day_opens = restaurants[restaurant]['opens'][day_of_the_week]
                if (previous_day_opens <= time <= datetime.strptime('23:59', "%H:%M").time()) or (
                        datetime.strptime('00:00', "%H:%M").time() <= time < previous_day_closes):
                    print(restaurant)

                # third case when closing hours are on the border next day 00:00:00
        finally:
            continue


if __name__ == "__main__":
    list_of_restaurants = ["data/restaurants-hours-source-1.csv", "data/restaurants-hours-source-2.csv"]
    dl = data_loader.DataLoader()
    restaurants = dl.import_data(list_of_restaurants)

    print("Welcome to the Restaurant Finder. Here You can find the working "
          "hours of restaurant that You are interested in or some another information")
    t = datetime.strptime('1:00', "%H:%M").time()
    day_of_week = 1
    opened_restaurants(restaurants, t, day_of_week)
