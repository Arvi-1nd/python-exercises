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