animals           = ['python','gopher']
more_animals      = animals
print(animals == more_animals) #=> True
print(animals is more_animals) #=> True
even_more_animals = ['python','gopher']
print(animals == even_more_animals) #=> True
print(id(animals), id(more_animals), animals is even_more_animals) #=> False

var1 = 123
var2 = 123
print(var1 == var2)
print("id ", id(var1), id(var2), var1 is var2)