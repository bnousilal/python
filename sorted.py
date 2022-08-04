#If you want your own implementation for sorting, sorted() also accepts a key function as an optional parameter.
#sorted(iterable, key=len) Here, len() is Python's in-built function to count the length of an object.

# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))

#=======
#Sort the list using sorted() having a key function
#=======
# take the second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list)

"""
We want to sort the list in such a way that the student with the highest marks is in the beginning.
In case the students have equal marks, they must be sorted so that the younger participant comes first.
"""
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12),
    ('Chris', 45, 11)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)
"""
Since the sorting logic function is small and fits in one line, lambda function is used inside key rather than passing a separate function name.
"""
sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)