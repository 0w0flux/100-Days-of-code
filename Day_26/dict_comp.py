import random
import pandas

def intro():
    # new_dict = {new_key:new_value for key,value in dict.items()if blank}
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    student_grades = {student:random.randint(1, 6) for student in names}
    print(student_grades)

    passed_students = {student:grade for student, grade in student_grades.items() if grade < 3}
    print(passed_students)

def exercise_01():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    result = {word: len(word) for word in sentence.split()}
    print(result)

def exercise_02():
    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
    weather_f = {day: c*9/5+32 for day, c in weather_c.items()}
    print(weather_f)

def loop_through_a_data_frame():
    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }
    student_data_frame = pandas.DataFrame(student_dict)
    print(student_data_frame)

    for (index, row) in student_data_frame.iterrows():
        # print(type(row))
        if row.student == "Angela":
            print(row.score)




intro()
exercise_01()
exercise_02()
loop_through_a_data_frame()