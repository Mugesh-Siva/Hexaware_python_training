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