class Animal:
    def __init__(self):
        self.energy = 50
        print("I am coming to life!")
        
    def eat(self, amount):
        self.energy += amount
    
    def say_hi(self):
        print('Meep!')
    
    def move(self):
        self.energy -= 10
        print("I am running!")
        
    def get_status(self):
        print("My current energy is {}".format(self.energy))
        if self.energy <0:
            print("I am starving")
        elif self.energy >= 0 and self.energy <50:
            print("I am getting hungry")
        elif self.energy >= 50 and self.energy <100:
            print("I am happily full")
        elif self.energy >= 100:
            print ("I am stuffed")
        else:
            print("Not valid")