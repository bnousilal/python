#https://stackoverflow.com/questions/58280015/printing-numbers-in-new-lines  
def MathOp():
  
  classic_division = 3/2 ## Calculate 3/2 here
  floor_division = 3//2 ## Calculate 3//2 here
  modulus = 3%2 ## Calculate 3%2 here 
  power = 3**2 ## Calculate 3**2 here
  ## Returning the calculations for evaluation
  return [classic_division, floor_division, modulus, power]

[classic_division, floor_division, modulus, power]=MathOp()
print(*[classic_division, floor_division, modulus, power], sep="\n")
print(f"{classic_division}\n{floor_division}\n{modulus}\n{power}")
print("{0}\n{1}\n{2}\n{3}".format(classic_division, floor_division, modulus, power))
