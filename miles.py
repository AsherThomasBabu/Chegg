def mph_and_minutes_to_miles():
    miles_per_hour = float(input())
    minutes_travelled = float(input())
    hours_travelled = minutes_travelled /60.0
    miles_travelled = hours_travelled * miles_per_hour

    print("Miles: {:f}".format(miles_travelled))

mph_and_minutes_to_miles()