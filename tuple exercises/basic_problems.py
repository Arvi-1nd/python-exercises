# 1 To remove the empty tuples from a list

gi = [(1,2),(),(1,5),(),(3,4)]

# using for loop
res = []

for t in gi:
    if t:
        res.append(t)
        
print(res)

# using list comprehension

resu = [t for t in gi if t]

print(resu)

# using filter

req = list(filter(None, gi))

print(req)

# 2 reversing a tuple

wer = (3,7,1,6,3,0)

# using slicing
print(wer[::-1])

# using reversed returns an iterator

hu = tuple(reversed(wer))

print(hu)

# using loop

tr = tuple(wer[i] for i in range(len(wer)-1,-1,-1))

print(tr)

# converting a list of tuples into dictionary

#converting the data type
re = [("a",1),("b",2),("c",3)]

re = dict(re)

print(re)

# using dict comprehension
er = [("x",5),("p",9),("u",3)]
qw = {key:value for key, value in er}

print(qw)

# using for loop
get_dict = {}

for key, value in er:
    get_dict[key] = value
    
print(get_dict)

# count the number of occurences

def count(tup,en):
    return tup.count(en)

tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8

print(count(tup,enq))
print(count(tup,enq1))
print(count(tup,enq2))

#Python - Count the elements in a list until an element is a Tuple

pl = [1, 2, 3, (4, 5), 6, 7]

counting = 0

for val in pl:
    if  isinstance(val,tuple):
        break
    counting += 1
    
print(counting)