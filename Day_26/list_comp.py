def intro():
    numbers = [1, 2, 3]
    new_numbers = [i + 1 for i in numbers]
    print(new_numbers)

    name = "Owe"
    new_name = [char.lower() for char in name]
    print(new_name)

    new_range = [i*2 for i in range(1, 5)]
    print(new_range)

    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    short_names = [name for name in names if len(name) < 5]
    long_names = [name.upper() for name in names if len(name) > 5]
    print(short_names, long_names)

def exercise_01():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [num*num for num in numbers]
    print(squared_numbers)

def exercise_02():
    list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    numbers = [int(i) for i in list_of_strings]
    result = [num for num in numbers if num % 2 == 0]
    print(result)    

def exercise_03():
    file1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
    file2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
    result = [i for i in file1 if i in file2]
    print(result)

intro()
exercise_01()
exercise_02()
exercise_03()