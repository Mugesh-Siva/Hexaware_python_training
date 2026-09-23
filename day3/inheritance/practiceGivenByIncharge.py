# multiple 2 parent 1 Child
# hierichary 1 parent 2 Child

# Multilevel 
class animal:
    def makesound(self):
        print("A random Animal Maked a sound")
class dog(animal):
    pass
class puppy(dog):
    pass


dog1=dog()
dog1.makesound()


puppy1=puppy()
puppy1.makesound()

# Muitiple 

class Animal:
    def makesound(self):
        print("Animals sound are loud")
class birds:
    def birdssound(self):
        print("brids sound are not loud")
class livingthing(Animal,birds):
    pass
livingthing1=livingthing()
livingthing1.makesound()

#Hirechachical inheritance

class parent:
    def child(self):
        print("child is here")

class child1(parent):
    
    pass

class child2(parent):
    pass

child_boy=child1()
child_boy.child()

child_girl=child2()
child_girl.child()

#Hybrid inheritance

class car:
    def run(self):
        print("car runs")
class engine(car):
    def prop(self):
        print("Car has engine")
class tires(car):
    def prop(self):
        print("car has tires")
class hybrid(engine,tires):
    pass


hybrids=hybrid()
hybrids.run()



#single inheritance

class laptop:
    def hasbattery(self):
        print("Laptop has battery")
class singlechild(laptop):
    pass
laptop1=laptop()
laptop1.hasbattery()