def process_data(list_student_data):
    dictionary = {}
    for student in list_student_data:
        sub_dictionary = {}
        student_data = student.split(",")
        sub_dictionary["age"] = int(student_data[1])
        sub_dictionary["courses"] = student_data[2:]
        dictionary[student_data[0]] = sub_dictionary
    return dictionary

def average_age(dictionary):
    return sum([dictionary[name]["age"] for name in dictionary.keys()])/len(dictionary) 

def courses(dictionary):
    return {course for student in dictionary.values() for course in student["courses"]}

def most_common_courses(dictionary):
    courses = [course for student in dictionary.values() for course in student["courses"]]
    return {course for course in courses if courses.count(course) == max([courses.count(course) for course in courses])}
    