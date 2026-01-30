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


# Remove multiple elements ia list

nm = [34,67,89,10]
c = [100,34,10,56]

for h in nm:
    if h not in c:
        print(h, sep=",")
        
# Remove empty tuples from the list

kl = [(4,6),(),(5,9),(),(8,9)]

jk = [t for t in kl if t]

print(jk)

# to print duplicates from a list of integers

gh = [4,1,5,2,4,9,8,2]

ll = set()
dup_ele = []

for ch in gh:
    if ch in ll:
        dup_ele.append(ch)
    else:
        ll.add(ch)
        
print(dup_ele)

# Remove first element from List

jg = ["p","k","h","t","o"]

first_element = jg[0]

for i in range(len(jg)-1):
    if jg[i] == first_element:
        del jg[i]
print(jg)

# we can also use del jg[0], pop(0) and jg[1:]


# Remove duplicates from a list

rw = [1,9,1,5,3,5,2,0,3]

get_og = [x for x in set(rw)]

print(get_og)

# Get unique element from list
qo = [5,9,2,4,7,1,8,2,5,3,1,4]

# Convert to set
print(list(set(qo)))

unique = set()
# Using for loop
for i in qo:
    if i not in unique:
        unique.add(i)

print(list(unique))

# Merging Two list

zc = [0,4,2]
mx = [5,7,3]
# adding list
merge_l1 = zc + mx
print(merge_l1)
# using extend
zc.extend(mx)
print(zc)
# using loop

for i in mx:
    zc.append(i)

print(zc)

# iterate over a list

cd = [1,2,3,4,5]

# using for loop
for val in cd:
    print(val)

# using while loop

while i < len(cd):
    print(cd[i])
    i += 1

# Finding the average of the List

lop = [3,1,6,4]

total_sum = sum(lop)
total_length = len(lop)

average_lop = total_sum / total_length

print(average_lop)

# Append at beginning of List

ji = [9,5,3,2]
ji = [6] + ji

print(ji)

# Finding the common elements in Both List

zd = [8,5,23,41,1,4,2,42,12,34,5,4,2,1]
gp = [4,3,12,4,2,4,1,24,5,3,5,31,56,5]

get_common = list(set(zd) & set(gp))

print(get_common)

get_com = list(set(zd).intersection(set(gp)))

print(get_com)

# get last element from the list

wc = [9,4,5]

get_last = wc[-1]
getting_last = wc.pop()
print(get_last)
print(getting_last)


# To remove none values from the list

remove_None = [2,None,3,5,None,5]

removed_none = [x for x in remove_None if x is not None]

print(removed_none)

# print common elements of both list

first_list1 = [56,23,45,12,90]
second_list1 = [54,89,76,32,45,23]

getting_common = list(set(first_list1) & set(second_list1))

print(getting_common)

# Max and Min element's position in a List

dummy_list = [87,98,43,78,23]

max_num = min_num = dummy_list[0]

for num in dummy_list:
    if num > max_num:
        max_num = num
    
    if num < min_num:
        min_num = num
    
print(dummy_list.index(max_num))
print(dummy_list.index(min_num))


def Mx_min(nums):
   max_num = nums.index(max(nums))
   min_num = nums.index(min(nums))
   return max_num, min_num

nums3 = [56,23,90,53]

print(Mx_min(nums3))

#Union of Two or more lists
coins = [2,5,1,50,10,20]

rupee_notes = [100,500,200,10,20]

return_result = list(set(coins).union(rupee_notes))

print(return_result)

re_result = list(set(coins) | set(rupee_notes))

print(re_result)

# Swap elements in a string list

api = ['Gfg', 'is', 'best', 'for', 'Geeks']
print(str(api))

get_replacing = [sub.replace('i','-').replace("-","t").replace("g",'e') for sub in api]

print(get_replacing)

#Converting List to String
list_str = ["A","N","S"]
con_list_str = " ".join(list_str)

print(con_list_str)

#using loop

loop_str = ""

for ch in list_str:
    loop_str += ch + ""    
print(loop_str)

# To separate even or odd in list

a_arr = [5,12,75,34,21,68,31,96]

e_num = []
o_num = []
# using normal for loop
for val in a_arr:
    if val % 2 == 0:
        e_num.append(val)
    else:
        o_num.append(val)

print(e_num)
print(o_num)

# using list comprehension
div_num = [val for val in a_arr if val % 2 == 0]
print(div_num)
non_div = [val for val in a_arr if val % 2 != 0]
print(non_div)

#using lambda

lam_even = list(filter(lambda x: x % 2== 0, a_arr))
print(lam_even)
lam_odd = list(filter(lambda x: x % 2 != 0, a_arr))
print(lam_odd)

#Reversing all the strings in the list

# using loop
soaps = ['hamam','pears','dove','lifebuoy','cinthol']

resullt = []

for soap in soaps:
    resullt.append(soap[::-1])
    
print(resullt)

# using list compre

reverse_string = [soap[::-1] for soap in soaps]

print(reverse_string)


# using lambda

rev_str = list(map(lambda soap: soap[::-1], soaps))

print(rev_str)

# To find the second largest element

fill_list = [2,5,1,6,3,8,30,20,54,32,11,14,8]

max_element = second_element = float('-inf')

for val in fill_list:
    if val > max_element:
        second_element = max_element
        max_element = val
    elif val > second_element and val != max_element:
        second_element = val
        
print(second_element)


# Python program to find the character position of Kth word from a list of strings

sample_list = ["Python","is","great","for","beginners"]

print(f"Original list {sample_list}")

res = [ele[0] for sub in enumerate(sample_list) for ele in enumerate(sub[1])]

k = 7
res = res[k]

print(f"The Position of kth value is {res}")


    
filliers = ["Kite", "Apple", "King", "Banana", "Kangaroo", "cat"]

j = "B"

getting_k = []

for word in filliers:
    if word.startswith(j):
        getting_k.append(word)
        
print(getting_k)
        
