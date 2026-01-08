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

# Reversing a list

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


# cloning or copying a list

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

