# 1 Find the max value of two numbers

# Using max keyword

a = 7
b = 6

print(max(a,b))

# Using if else condition

if a < b:
    print("B is greater", b)
else:
    print("A is greater", a)
    

# using slicing

a,b = 5,7

result = [a,b]

result.sort()
print(result[-1])


# 2 to find the length of the list

g = [2,3,5,7]

print(len(g))

# using for loop

count = 0

for i in g:
    count += 1

print(count)

# 3 To find the minimum
a = 5
b = 4

print(min(a,b))

#using ternary

result = a if a < b else b

print(result)

result3 = [a,b]

result3.sort()

print(result3[-1])

# 4To interchange first and last element

ki = [10,20,30,40,50]

result = ki[-1:] + ki[1:-1] + ki[:1]

print(result) 

# using tuple

pair = ki[-1],ki[0]

ki[0],ki[-1] = pair

print(ki)

# 5 To check if a element is present

rt = [3,6,2,9,7]

flag = False

val = 6

for i in rt:
    if val == i:
        flag = True
        break
    
if flag:
    print("Element Exist")
else:
    print("Element does not exist")
    
    
# using generator

ty = [67,23,78,99]

final = any(x == 30 for x in ty)

if final:
    print("Element exist")
else:
    print("Element does not exist")

# 6 Reversing a list

# slicing

re = [4,2,9,6,2]

print(re[::-1])

# using reverse
jh = [4,2,1,3,9]

jh.reverse()

print(jh)

# using while loop 

op = [4,1,7,3,1]

i,j = 0, len(op)-1

while i < j:
    op[i],op[j] = op[j],op[i]
    i += 1
    j -= 1
    
print(op)


# 7 cloning or copying a list

ui = [4,6,7,8,9]
# slicing creates a new list with same values
kj = ui[:]

print(kj)

# using copy
import copy

ru = copy.copy(ui)
print(ru)

# using list comprehension

lo = [x for x in ui]

print(lo)

# 8 Count Element in the list

ret = [4,1,4,0]

# using len function
print(len(ret))

# using for loop
count = 0

for i in ret:
    count += 1
    
print(f"The length of the list is {count}")

# 9 Sum and Average of list

bu = [4,10,45,32]

total_value = sum(bu)
total_elements = len(bu)

average = total_value / total_elements

print(f"Total value : {total_value} and Average: {average}")


# 10 To get sum of digits in list

# using sum

lp = [2,1,9,2,5,8]

list_sum = sum(lp)

print(list_sum)

# using loop

get_sum = 0

for i in lp:
    get_sum += i

print(get_sum)

# 11 Multiply all numbers in a list

get_prod = 1

# by using for loop

for i in lp:
    get_prod *= i

print(get_prod)

# using math

import math

just_prod = math.prod(lp)

print(just_prod)

# smallest number in a List
me = [8,5,2,9,6]

min_value = me[0]

for val in me:
    if val < min_value:
        min_value = val
        
print(min_value)

# largest value in a list
max_value = me[0]

for val in me:
    if val > max_value:
        max_value = val
        
print(max_value)


# second largest number

max_value = second_max = float("-inf")

for val in me:
    if val > max_value:
        second_max = max_value
        max_value = val
    elif val > second_max and val != max_value:
        second_max = val
        
print(second_max)

# to get even numbers in a list

mb = [7,4,29,36,44,31,8]
# using filter

even_num = filter(lambda x : x % 2 == 0, mb)
print(tuple(even_num))

#using loop

even_nums = []

for val in mb:
    if val % 2 == 0:
        even_nums.append(val)
        
print(even_nums)

# using list comprehension

eveen_nums = [val for val in mb if val % 2 == 0]
print(eveen_nums)

# odd numbers in list

oddy_nums = filter(lambda x : x % 2 != 0, mb)

odd_nums = [val for val in mb if val % 2 != 0]

od_num = []

for val in mb:
    if val % 2 != 0:
        od_num.append(val)
        
print(tuple(oddy_nums))
print(od_num)
print(odd_nums)

# counting even and odd numbers in a list

mj = [9,2,5,8,45,12,87,4]

e_num = list(filter(lambda x: x % 2 == 0, mj))
o_num = list(filter(lambda x: x % 2 != 0, mj))

print(e_num)
print(o_num)

# count positive and negative numbers in a list

lk = [3,-8,9,-10,11,-14,59,-98]

p_num = list(filter(lambda x : x > 0, lk ))
n_num = list(filter(lambda x : x < 0, lk ))

print(p_num)
print(n_num)