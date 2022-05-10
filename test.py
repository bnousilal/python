lang = ['JAVA', 'PYTHON', 'GO', 'COBOL', 'PHP', 'RUST']

out = [i for i in lang if i[1].casefold() == chr(0x79)]
print(*out)

city = ["Mumbai", "Delhi", "Chennai", "Bangalore"]
c1, *c2 = city
print(c2)

L = ['a', 'b', 'c', 'd', 'e']
x, *y, z = L[1:]
print([L[0]] + [x] + y[::-1] + [z])
