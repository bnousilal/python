#(values) = [ (expression) for (item) in (collection) ]
sqr=[]

for i in range(10):
    sqr.append(i**2)

print(sqr)

#alist = [expression for variable in iterable]
sqr=[i**2 for i in range(10)]

print(sqr)

#alist = [expression for variable in iterable if condition]
numbers=[1,2,3,4,5,6,7,8,9]
numbers_greter_than_4=[number for number in numbers if number > 4]
print(numbers_greter_than_4)

numbers_greter_than_4_and_even=[number for number in numbers if number > 4 if number %2 == 0]
print(numbers_greter_than_4_and_even)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
letters_with_index=[]
for index, letter in enumerate(letters):
    letters_with_index.append((index,letter))
print(letters_with_index)

letters_with_index=[(index, letter) for index, letter in enumerate(letters)]
print(letters_with_index)

#The syntax for using 2 for-loops inside list comps.
sizes=['sm', 'lg', 'xl']
colors=['red', 'green', 'white']

shirts=[(size, color) for size in sizes for color in colors]
print(shirts)

lst = [20,23,29,45,87,12]
print([num for num in lst if num in range(20, 30)])
special = [num for num in lst if 20 <= num <= 30]
print(special)
special = (n for n in lst if 20 <= n <= 29)
print(*special, sep=',')