def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left = 0
    right = len(students)

    while left < right:
        index = (left+right)//2
        index_id = students[index].id
        if target_id < index_id:
            right = index
        elif target_id > index_id:
            left = index+1
        else:
            return students[index]
    return None  

class Student:
    def __init__(self, id):
        self.id = id

