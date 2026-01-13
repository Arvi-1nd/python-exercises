# 1 sorting the dictionary by key or values
d = {"ranga":34,"raajnessh":56,"aarav":32}

myKeys = list(d.keys())

myKeys.sort()

sd = {i: d[i] for i in myKeys}
print(sd)

# 2 handling missing keys

dic = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

try:
    print(dic['Australia'])
    print(dic['India'])
    print(dic["japan"])
except KeyError:
    print("not found")
    
# Python dictionary with keys having multiple inputs

import random as rn

dict = {}

x, y, z = 10, 20, 30

dict[x,y,z] = x + y - z

x,y,z = 5,2,4

dict[x,y,z] = x+ y - z

print(dict)

# Python program to find the sum of all items in a dictionary

dt = {'a':100,'b':200,'c':400}
# using sum

fg = sum(dt.values())

print(fg)

# using list comrehension

get_sum = sum([dt[v] for v in dt])

print(get_sum)

# using for loop

total_sum = 0

for i in dt.values():
    total_sum += i

print(total_sum)

# size of dict

import sys

dp = {"a":1,"b":3,"c":4}

res = sys.getsizeof(dp)

print(res)

# sorting by lambda

dice = [
    {"name": "Harry", "age": 20},
    {"name": "Robin", "age": 20},
    {"name": "Kevin", "age": 19}
]

print("sorted by age:")
print(sorted(dice, key=lambda x: x["age"]))

# merging two dictionaries

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)

# Program to create grade calculator in Python

ajay = {
    "name": "ajay kumar",
    "assignment": [80,60,30,10],
    "test": [59,78],
    "lab": [98, 56.89]
}

nikil = {
    "name": "nikil babu",
    "assignment": [50,45,30,20],
    "test": [90,88],
    "lab": [80.89, 78.89]
}

peter = {
    "name": "peter paul",
    "assignment": [25,66,38,76],
    "test": [70.08,98.09],
    "lab": [94.67, 97.89]
}

deva = {
    "name": "deva raj",
    "assignment": [90,96,67,30],
    "test": [65.09,70.98],
    "lab": [85.90, 45.89]
}

# This calculates the average

def get_average(marks):
   total_sum = sum(marks)
   total_sum = float(total_sum)
   return total_sum / len(marks)

def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])
    


    return (0.1 * assignment +
            0.7 * test + 0.2 * lab)
    
def assign_letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "E"
        
        
def class_average_is(students_list):
    result_list = []
    
    for student in students_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
    return get_average(result_list)
    
students =[ajay,nikil,peter,deva]

for student in students:
    avg = calculate_total_average(student)

    print(f"Student Name: {student['name']}")
    print(f"Average Mark of {student['name']} is {avg:.2f}")
    print(f"Letter grade of {student['name']} is {assign_letter_grade(avg)}")
    print()

    
   
class_av = class_average_is(students)

print(f"Class average is {class_av}")
print(f"Letter grade of class is {assign_letter_grade(class_av)}")
 
 
from collections import OrderedDict

fill = OrderedDict([("a",1),("b",2)])
fill.update({"c":3})
fill.move_to_end("c", last=False)
print(fill)