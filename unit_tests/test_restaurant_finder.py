import datetime
import unittest

import restaurant_finder


class TestRestaurantFinder(unittest.TestCase):
    def test_restaurantInfo_itIsMonday20h_restaurantIsOpen(self):
        restaurant = {
            "Willy Wonka Factory": {
                'opens': {0: datetime.time(17, 30), 1: datetime.time(17, 30), 2: datetime.time(17, 30)},
                'closes': {0: datetime.time(23, 30), 1: datetime.time(23, 30), 2: datetime.time(23, 30)}},
            "Hogwarts": {
                'opens': {1: datetime.time(17, 30), 2: datetime.time(17, 30), 3: datetime.time(17, 30)},
                'closes': {1: datetime.time(23, 30), 2: datetime.time(23, 30), 3: datetime.time(23, 30)}}
        }
        rf = restaurant_finder.RestaurantFinder(restaurant)
        open_restaurant = rf.opened_restaurants(datetime.time(20, 0), 0)
        self.assertEqual(list(restaurant.keys())[0], open_restaurant[0])

    def test_restaurantFinder_closingHoursEndsAnotherDay_itIsTuesday01h_restaurantIsOpen(self):
        restaurant = {
            "Willy Wonka Factory": {
                'opens': {0: datetime.time(17, 30), 1: datetime.time(17, 30), 2: datetime.time(17, 30)},
                'closes': {0: datetime.time(2, 30), 1: datetime.time(23, 30), 2: datetime.time(23, 30)}},
            "Hogwarts": {
                'opens': {1: datetime.time(17, 30), 2: datetime.time(17, 30), 3: datetime.time(17, 30)},
                'closes': {1: datetime.time(23, 30), 2: datetime.time(23, 30), 3: datetime.time(23, 30)}}
        }
        rf = restaurant_finder.RestaurantFinder(restaurant)
        open_restaurant = rf.opened_restaurants(datetime.time(1, 0), 1)
        self.assertEqual(list(restaurant.keys())[0], open_restaurant[0])


if __name__ == '__main__':
    unittest.main()
