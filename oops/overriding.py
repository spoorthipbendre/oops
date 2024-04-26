#Overriding:
class Animal:
    def speak(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    pass 
    
dog=Dog()
cat=Cat()
cow=Cow()

print(dog.speak())
print(cat.speak())
print(cow.speak())


class Animal:
    def speak(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    pass

class Cow(Animal):
    def speak(self):
        return "moof"
    
dog=Dog()
cat=Cat()
cow=Cow()

print(dog.speak())
print(cat.speak())
print(cow.speak())
