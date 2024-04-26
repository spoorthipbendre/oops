#4 Pillars of Oops
#1.Encapsulation
#2.Inheritance
#3.Abstraction
#4.Polymorphism

class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    def speak(self):
        return "Moo!"
    
def make_animal_speak(animal):
        print(animal.speak())
        
dog=Dog()
cat=Cat()
cow=Cow()

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(cow)