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