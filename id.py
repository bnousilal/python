str = "Hello"
print(f"address of the string: {id(str)}")
str += "!"
print(f"address of the string: {id(str)}")

list1=["nousi", "riya", "rishik", "alekhya"]
list2=list1
print(f"address of the list1 {id(list1)}, {list1}");
print(f"address of the list2 {id(list2)}, {list2}");
list2.append("dinesh")
print(f"address of the list1 {id(list1)}, {list1}");
print(f"address of the list2 {id(list2)}, {list2}");
print()

tuple1=("nousi", "riya", "rishik", "alekhya")
tuple2=tuple1
print(f"address of the tuple1 {id(tuple1)}, {tuple1}");
print(f"address of the tuple2 {id(tuple2)}, {tuple2}");
tuple2.append("dinesh")
print(f"address of the tuple1 {id(tuple1)}, {tuple1}");
print(f"address of the ruple2 {id(tuple2)}, {tuple2}");
