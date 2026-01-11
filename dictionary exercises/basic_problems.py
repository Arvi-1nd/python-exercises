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
