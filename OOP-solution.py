class PodRacer:
    def __init__(self, max_speed, condition, price, owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner
    
    def repair(self):
        self.condition = 'repaired'

class AnakinsPod(PodRacer):
    def __init__(self, max_speed, condition, price, owner = 'Anakin'):
        super().__init__(max_speed, condition, price, owner)
    
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(PodRacer):
    def __init__(self, max_speed, condition, price, owner = 'Sebulba'):
        super().__init__(max_speed, condition, price, owner) 

    def flame_jet(self, other_pod):
        other_pod.condition = 'trashed' 

Anakins_Pod = AnakinsPod(25, 'perfect', 1000)
Sebulbas_Pod = SebulbasPod(50, 'perfect', 2500)

print(Anakins_Pod.condition)
print(Sebulbas_Pod.condition)

Sebulbas_Pod.flame_jet(Sebulbas_Pod)

print(Anakins_Pod.condition)
print(Sebulbas_Pod.condition)

'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    - Encapsulation
        Encapsulation is demonstrated by the use of classes and their associated methods (repair, boost, and flame_jet) to encapsulate data (attributes) and behavior. Attributes like max_speed, condition, price, and owner are encapsulated within the PodRacer and its subclasses.
    - Abstraction
    - Inheritance
        Inheritance is evident in the relationship between the base class PodRacer and its subclasses AnakinsPod and SebulbasPod. Subclasses inherit attributes and methods from the base class and can extend or override them as needed.
    - Polymorphism
        Polymorphism is not explicitly demonstrated in this example. While you have different classes (PodRacer, AnakinsPod, and SebulbasPod) with their own implementations of methods, there's no demonstration of polymorphism in this code. Polymorphism would typically involve using a common interface or base class to work with objects of different derived classes in a uniform way.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    OOP is a reasonable choice because it models a real-world scenario where different types of podracers (Anakin's and Sebulba's) share common characteristics but also have their own unique behavior and attributes.

How in particular did Object Oriented Programming assist in the solving of this problem?
    OOP helped in solving this problem by providing a way to model and organize the entities and their behavior in a modular and reusable manner.
'''