empty_list = [ ]
empty_tuple = ( )
empty_dict = { }
empty_str = ' '
#emprty_set = {} #WRONG
empty_set = set()
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1|x2)
#print(x1 | ('baz', 'qux', 'quux')) #TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
print(x1.union(('baz', 'qux', 'quux')))

a = [1, 2, 3]
#print({a})  #TypeError: unhashable type: 'list'
d = {'a': 1, 'b': 2}
#print({d}) #TypeError: unhashable type: 'dict' 
