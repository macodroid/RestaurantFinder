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

    def test_get_information_about_specific_restaurant(self):
        restaurant = {'BBQ Tofu Paradise': {'cuisine': 'vegetarian',
                                            'opens': {0: datetime.time(16, 30), 2: datetime.time(16, 30),
                                                      4: datetime.time(16, 30), 5: datetime.time(16, 30),
                                                      6: datetime.time(16, 30)},
                                            'closes': {0: datetime.time(20, 0), 2: datetime.time(20, 0),
                                                       4: datetime.time(20, 0), 5: datetime.time(20, 0),
                                                       6: datetime.time(20, 0)}, 'price': 2, 'rating': 1}}
        rf = restaurant_finder.RestaurantFinder(restaurant)
        info_restaurant = rf.get_information_about_specific_restaurant("BBQ Tofu Paradise")
        self.assertEqual(restaurant["BBQ Tofu Paradise"], info_restaurant)

    def test_get_information_about_specific_restaurant_restaurant_doesnt_exist(self):
        restaurant = {'BBQ Tofu Paradise': {'cuisine': 'vegetarian',
                                            'opens': {0: datetime.time(16, 30), 2: datetime.time(16, 30),
                                                      4: datetime.time(16, 30), 5: datetime.time(16, 30),
                                                      6: datetime.time(16, 30)},
                                            'closes': {0: datetime.time(20, 0), 2: datetime.time(20, 0),
                                                       4: datetime.time(20, 0), 5: datetime.time(20, 0),
                                                       6: datetime.time(20, 0)}, 'price': 2, 'rating': 1}}
        rf = restaurant_finder.RestaurantFinder(restaurant)
        info_restaurant = rf.get_information_about_specific_restaurant("Sauron bar")
        self.assertIsNone(info_restaurant)

if __name__ == '__main__':
    unittest.main()
