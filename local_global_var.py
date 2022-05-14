global_var=28
def f():
    print(s)

def with_in_function():
    global global_var #to tell Python, that we want to use the global variable, we have to explicitly state this by using the keyword
    print(f"global_var {global_var}, global_var_id {id(global_var)}")
    local_var=28 #local_var and global_var addresses will be same
    #A variable can't be both local and global inside a function
    global_var = 28

    print(f"local_var {local_var}, local_var_id {id(local_var)}")

#Global Variables in Nested Functions
#global keyword in nested functions does not affect the namespace of their enclosing namespace!
#https://python-course.eu/python-tutorial/global-local-variables-namespaces.php
def nested_fn():
    city = "first level in fn Hamburg"

    def g():
        #global city
        nonlocal city
        city = "second level in fn Geneva"

    print("Before calling g with in fn city: " + city)
    print("Calling g now:")
    g()
    print("After calling g with in fn city: " + city)
    #print("even city is declared as global in the g fn, it did not change")

nested_fn()
print("*"*50)
city = "Stuttgart"
print("Value of city in main: " + city)

#print(f"global_var {global_var}, ")
with_in_function()
s = "I love Paris in the summer!"
f()