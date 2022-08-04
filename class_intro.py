class Dog:
      def __init__(self, name, age):
            self.name = name
            self.age = age

dog1 = Dog('doggy', 12)
print("Name : %s, Age : %d" % (dog1.name, dog1.age))

class car:
      def __init__(self, color, milege):
            self.color = color
            self.milege = milege

      def car_description(self):
            return "The %s car has %s miles." % (self.color, self.milege)

      def __str__(self):
            return "The %s car has %s miles." % (self.color, self.milege)


blue_car = car("blue", "20,000")
red_car = car("red", "30,000")
print(blue_car)
print(red_car)
