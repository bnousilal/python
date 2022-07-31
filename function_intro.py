#range(start, stop[, step])

def sum_eo_nousi(n, t):
    sum = 0
    if t.casefold() == 'e':
        for i in range(n):
            if i % 2 == 0:
                sum = sum + i
    elif t.casefold() == 'o':
        for i in range(n):
            if i % 2 != 0:
                sum = sum + i
    else:
        sum = -1

    return sum;

def sum_eo(n, t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

print(sum_eo(20, 'o'))
print(sum_eo_nousi(20, 'o'))

numbers = [9, 7, 4, 6, 3, 5]
print(numbers.sort())
print(numbers)