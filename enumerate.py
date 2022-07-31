programmming = ["Python", "Programmming", "Is", "Fun"]
print(type(programmming))
enum = enumerate(programmming)
print(type(enum))
#Converting to a list
print(list(enum))
#Converting to a tuple
#enum = enumerate(programmming)
print(tuple(enum))
#Converting to a set
#enum = enumerate(programmming)
print(set(enum))



# python
# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(enumerate(l1))
print(obj1)
print(list(enumerate(l1)))

#By default enumerate starts indexing from zero, but passing a value in the start parameter we can get the desired indexing also
# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele, end=" ")
print()
for ele in enumerate(l1, 100):
    print(ele, end=" ")
print()
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele, end=" ")
print()
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)

#help(enumerate)