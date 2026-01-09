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

