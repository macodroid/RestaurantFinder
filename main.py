import data_loader
import restaurant_finder
import datetime
from utils import *

if __name__ == "__main__":
    list_of_restaurants = ["data/restaurants-hours-source-1.csv", "data/restaurants-hours-source-2.csv"]
    dl = data_loader.DataLoader()
    restaurants = dl.import_data(list_of_restaurants)
    rf = restaurant_finder.RestaurantFinder(restaurants)
    restaurants_open_now = rf.opened_restaurants()
    types_of_cuisine = get_all_cuisine_type(restaurants)
    active = True

    print("Welcome to the Restaurant Finder. Here You can find the working "
          "hours of restaurant that You are interested in or some another information")
    print("Restaurants open now!")
    print_restaurants_name(restaurants_open_now)
    while active:
        print("\nPress 1 to find all opened restaurants with specific time and day")
        print("Press 2 to find all information about specific restaurant")
        print("Press 3 to find restaurant with specific cuisine")
        print("Press 4 to quit")
        try:
            user_input = int(input("Type a number: "))
            if user_input < 1 or user_input > 4:
                raise ValueError
        except ValueError:
            print("Please, input valid number. Valid values are 1 2 3 4")

        if user_input == 1:
            print("Please, specify time and day of the week.")
            hours = datetime.datetime.strptime(input("Time (Hours:Minute) 24h-format: "), "%H:%M").time()
            print("Mon = 0, Tue = 1, Wed = 2, Thu = 3, Fri = 4, Sat = 5, Sun = 6")
            day = int(input("Day: "))
            restaurants = rf.opened_restaurants(hours, day)
            print(f"Restaurants open on {enum_days.Days(day).name} at {hours}")
            print_restaurants_name(restaurants)
        elif user_input == 2:
            restaurant_name = input("Enter restaurant name: ")
            info = rf.get_information_about_specific_restaurant(restaurant_name)
            print_all_information(restaurant_name, info)
        elif user_input == 3:
            print_all_cuisine_types(types_of_cuisine)
            selected_cuisine = input("Enter type of cuisine: ")
            restaurants = rf.get_restaurants_info_with_specific_cuisine(selected_cuisine)
            print_restaurants_name(restaurants)
        elif user_input == 4:
            print("\nThank You for using our service.")
            print("Hopeful You found some restaurant that suite your schedule or cuisine. Bon appetite.")
            active = False
