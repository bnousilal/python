parrot="Norwegian Blue"
       #0123456789 10 11 12 13 14
print(parrot[-4:2])   #stop here 2 is out of range so it will no tprint anything
print(parrot[-4:12])  
print(parrot[-4])
print(parrot[11])
l = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz&']

# I want a string up to 'def' from 'vwx', all in between
# from 'vwx' so -2;to 'def' just before 'abc' so -9; backwards all so -1.
print(l[-2:-9:-1]) #['vwx', 'stu', 'pqr', 'mno', 'jkl', 'ghi', 'def']

# For the same 'vwx' 7 to 'def' just before 'abc' 0, backwards all -1
print(l[7:0:-1]) #['vwx', 'stu', 'pqr', 'mno', 'jkl', 'ghi', 'def']
#slice(start, stop, step)


#split
#The split() method acts on a string and returns a list of substrings
#str.split(sep=None, maxsplit=-1)
#If the string contains consecutive delimiters,
#If the delimiter is not provided or None, then whitespaces are considered as the delimiter.
s = 'Python is Nice'
str_list = s.split(sep=' ')
print(str_list)
str_list = s.split(sep=' ', maxsplit=1) #max split
print(str_list)
str_list = s.split(' ', 1) #max split
print(f"with out giving spe and maxsplit: {str_list}")
str_list = s.split() #None, default is space
print(str_list)

#rsplit
#Python string rsplit() function is very similar to split() function. The only difference is that the splits are done starting at the end of the string and working to the front.
s = 'Python is Nice'
str_list = s.rsplit(sep=' ')
print(str_list)
str_list = s.rsplit(sep=' ', maxsplit=1) #max split
str_list = s.rsplit(' ', 1) #max split
print(str_list)
str_list = s.rsplit() #None, default is space
print(str_list)

#join
#<sep>.join(<iterable>)
#<iterable> is any Python iterable containing the substrings, say, a list or a tuple, and
#<sep> is the separator that you'd like to join the substrings on.
#In essence, the join() method joins all items in <iterable> using <sep> as the separator.

my_string = "Apples,Oranges,Pears,Bananas,Berries"
my_list = my_string.split(',')
print(my_list)
print(','.join(my_list))