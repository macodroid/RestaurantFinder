import enum_days


def print_restaurants_name(restaurants):
    for i, restaurant in enumerate(restaurants):
        if i % 5 == 0 and i != 0:
            print(restaurant)
        elif i == len(restaurants) - 1:
            print(restaurant)
        else:
            print(f"{restaurant}, ", end=" ")


def print_work_hours(r_key, r_value):
    print(r_key)
    format = "%H:%M"
    for day, hour in r_value.items():
        print(f"{enum_days.Days(day).name}: {hour.strftime(format)}", end=' ')
    print()


def print_all_information(name, restaurant_info):
    print(f"\n{name}")
    for r_key, r_value in restaurant_info.items():
        if r_key == 'opens' or r_key == 'closes':
            print_work_hours(r_key, r_value)
        else:
            print(f"{r_key}: {r_value}")


def get_all_cuisine_type(restaurants):
    types = set()
    for restaurant in restaurants:
        try:
            types.add(restaurants[restaurant]['cuisine'])
        except KeyError:
            continue
    return types


def print_all_cuisine_types(all_cuisine_types):
    for type in all_cuisine_types:
        print(type, end=" ")
    print()
