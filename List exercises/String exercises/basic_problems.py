# 1 Check if a string is symmetrical or palindrome

a = "asdasd"

half = len(a) // 2
# using slicing property here to compare first half and other half it is based on length of the string even or odd
sym = a[:half] == a[half:] if len(a) % 2 == 0 else a[:half] == a[half+1:]

pal = a == a[::-1]

print("symmetrical" if sym else "not symmetrical")
print("palindrome" if pal else "not palindrome")


## Using Two pointer

# Use this for make it efficient and fast
b = "amaama"

pal = True

i, j = 0, len(b)-1

while i < j:
    if b[i] != b[j]:
        pal = False
    i += 1
    j -= 1
    
sym = True
half = len(b)  // 2

for i in range(half):
    if len(b) % 2 == 0:
        if b[i] != b[i + half]:
          sym = False
    else:
        if b[i] != b[i + half + 1]:
            sym = False


print("symmetrical" if sym else "not symmetrical")
print("palindrome" if pal else "not palindrome")

 
        

# For the above problems time complexity is
# Slicing method O(n)
# Two pointer O(n) use it for interviews


# 2 To find the length of the string

f = "JavaorPython"

# using len function
print(len(f))

# using for loop
sum = 0

for i in f:
    sum += 1
    
print(sum)

# Time and space for first in O(n) constant second is l(n) Linear 

# 3 To reverse a String 

s = "Python is fun"
# using slicing and split
result = " ".join(s.split()[::-1])
print(result)

# Using for loop
s = s.split()

result = ""

for i in reversed(s):
    result += i + " "
    
print(result)

# 4 to remove characters in a string

h = "hello world"

result = "".join([i for i in h if i != "o"])
print(result)

result1 = "".join(filter(lambda c: c != "o",h))

print(result1)
