#Yuzheng Wu
#Assignment 10.1: Your Own Class

class CLanguage :
    name = "fall quarter 2021"
    add = "University of California，Santa Cruz"
    def __init__(self):
        self.name = "Assignment 10.1: Your Own Class"
        self.add = "Teacher: Harikrishna Kuttivelil"
    def say(self):
        self.catalog = 13
clang = CLanguage()
clang.name = "CSE-20-03"
clang.add = "Beginning Programming in Python"
print(clang.name)
print(clang.add)
clang2 = CLanguage()
print(clang2.name)
print(clang2.add)
print(CLanguage.name)
print(CLanguage.add)

student_list = []

def std_input():
    Assignment = input("Assignment name: ")
    name = input("student name: ")
    id = input("student id: ")
    grades = input("student grades: ")
    student_dict = {'Assignment name': Assignment, 'name': name, 'id': id, 'grades': grades}
    student_list.append(student_dict)

def std_output(id):
    for i in range(len(student_list)):
        if student_list[i]['id'] == id:
            print(student_list)

def std_output_all():
    for i in range(len(student_list)):
        print(student_list)

if __name__ == '__main__':
    while True:
        print("place choose: \n1. input student data \n2. Output specified student data \n3. Output all student data \n4. break")
        a = int(input())
        if a == 1:
            std_input()
        elif a == 2:
            id = input("student id: ")
            std_output(id)
        elif a == 3:
            std_output_all()
        elif a == 4:
            break