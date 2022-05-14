input_string = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""

def string_split_ex(unsplit):
    results = []

    # Bonus points for using splitlines() here instead,
    # which will be more readable
    for line in unsplit.split('\n')[1:]:
        print(line)
        results.append(line.split(',', maxsplit=2))

    return results

print(string_split_ex(input_string))

#.join() is smart in that it inserts your “joiner” in between the strings in the iterable you want to join,
# rather than just adding your joiner at the end of every string in the iterable.
#This means that if you pass an iterable of size 1, you won’t see your joiner:

print('b'.join(['a']))

input_list = [
    ['Boston', 'MA', '76F', '65% Precip', '0.15 in'],
    ['San Francisco', 'CA', '62F', '20% Precip', '0.00 in'],
    ['Washington', 'DC', '82F', '80% Precip', '0.19 in'],
    ['Miami', 'FL', '79F', '50% Precip', '0.70 in']
]

# We start with joining each inner list into a single string
joined = [','.join(row) for row in input_list]

# Now we transform the list of strings into a single string
output = '\n'.join(joined)

print(output)