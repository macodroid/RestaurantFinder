import datetime


class RestaurantFinder:
    def __init__(self, restaurants):
        self._restaurants = restaurants

    def opened_restaurants(self, time=None, day_of_the_week=None) -> list:
        """
        Search which restaurants are opened. If time and day_of_the_week is not specified current values are used.
        Current time and day of the week today. \n
        :param time: search which restaurant are opened at specific time
        :param int day_of_the_week: search which restaurant are opened at specific day of the week
        :rtype: None
        """
        open_restaurants = []
        if time is None and day_of_the_week is None:
            day_of_the_week = datetime.datetime.today().weekday()
            time = datetime.datetime.now().time()

        for restaurant in self._restaurants:
            try:
                opens = self._restaurants[restaurant]['opens'][day_of_the_week]
                closes = self._restaurants[restaurant]['closes'][day_of_the_week]
                # first basic case that entered time is in interval of opens < time < closes
                if opens < closes and opens <= time < closes:
                    open_restaurants.append(restaurant)
                # second case when closing hours are on the border next day 00:00:00
                elif opens > closes == datetime.time(0, 0):
                    closes = datetime.time(23, 59)
                    if closes > time:
                        open_restaurants.append(restaurant)
                # third case closing hours is till next day
                elif opens > time < closes:
                    # # restrict the day_of_the_week from jumping out of the interval  <0,6>
                    tmp_day_of_week = (day_of_the_week - 1) % 7
                    previous_day_opens = self._restaurants[restaurant]['opens'][tmp_day_of_week]
                    previous_day_closes = self._restaurants[restaurant]['closes'][tmp_day_of_week]
                    if datetime.time(0, 0) <= time < previous_day_closes:
                        open_restaurants.append(restaurant)
            except KeyError:
                continue
        return open_restaurants
