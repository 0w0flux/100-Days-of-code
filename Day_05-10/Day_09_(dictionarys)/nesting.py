travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Rotenburg an der Fulda", "Köln"]
}

print(travel_log["France"][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "times_visited": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Rotenburg an der Fulda", "Köln"],
        "times_visited": 5
    }
}

print(travel_log["Germany"]["cities_visited"][0])


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4
print(dict)