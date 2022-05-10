#  https://nedbatchelder.com/text/names.html
#Fact: Assignment never copies data.
#Myth: Python assigns mutable and immutable values differently.
x = 1
print("val of x: {} address of x: {}".format(x, hex(id(x))))
x = x + 1
print("val of x: {} address of x: {}".format(x, hex(id(x))))
print("address is different for immutable variable")
print("*"*80)
nums = [1, 2, 3]
print("val of nums: {} address of nums: {}".format(nums, hex(id(nums))))
nums.append(4)
print("val of nums: {} address of nums: {}".format(nums, hex(id(nums))))
print("address is same for mutable variable")
print("*"*80)
x = 4
y = 4
z = y
#When we said “z = y”, that doesn’t mean that they will always be the same forever. Reassigning z leaves y alone.
#Now z and y both refer to the same value:
w = 9999
v = 9999
a = 12345678
b = 12345678
print("val of x: {} address of x: {}".format(x, hex(id(x))))
print("val of y: {} address of y: {}".format(y, hex(id(y))))
print("val of z: {} address of z: {}".format(z, hex(id(z))))
print("*"*80)
z = 19
#If two names refer to the same value, this doesn’t magically link the two names. Reassigning one of them won’t reassign the other also:
print("val of x: {} address of x: {}".format(x, hex(id(x))))
print("val of y: {} address of y: {}".format(y, hex(id(y))))
print("val of z: {} address of z: {}".format(z, hex(id(z))))
print("*"*80)
print("val of w: {} address of w: {}".format(w, hex(id(w))))
print("val of v: {} address of v: {}".format(v, hex(id(v))))
print("val of a: {} address of a: {}".format(a, hex(id(a))))
print("val of b: {} address of b: {}".format(b, hex(id(b))))
