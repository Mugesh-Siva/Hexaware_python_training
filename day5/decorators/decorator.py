def before_message(func): #It takes any function as input where the @before_message annotation is used on top of it
    def wrapper():
        print("before function")
        func()
    return wrapper

@before_message # By using this annotation its it internally before_message(greet) 
def greet(): #It is passed in the parameters of before_message()
    print("hello")

greet()