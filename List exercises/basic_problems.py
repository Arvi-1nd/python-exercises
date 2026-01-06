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