#https://dbader.org/blog/list-dict-set-comprehensions-in-python
list1 = [1, 3, 5]
list2 = [7, 9]
list1.extend(list2)
#Here each element of the list2 is a new element of list1.
print(list1)

list1 = [1, 3, 5]
list2 = [7, 9]
list1.append(list2)
#Here we are simply appending list2 to list1. The whole list2 will append to list1 as a new element. The complete list2 is a new element of the list1. [1, 3, 5, [7, 9]]
print(list1)

list1 = [1, 3, 5]
name = "John"
list1.append(name)
#the append method will append the whole iterable(here a string name="John") to it as a new element.
print(list1) #[1, 3, 5, 'John']

list1 = [1, 3, 5]
name = "John"
list1.extend(name) # The 'extend method' appends each element of the iterable as a new element.
print(list1) #[1, 3, 5, 'J', 'o', 'h', 'n']

