# empty class\
# caps at the start of the name - camel case

# CAB - Class contain Attribute and Behaviour
# Behaviour is also called as Methods(Not the functions)
#methos are part of classes
   #whenever the function is called in a class>> it is called Method
# Attributes is also called as Data Members
class Person:
    #attributes
    name = None
    age= None
    id= None
    Phone = None

    # behaviour
    def talk(self):   # self is first instance of every method,
        print("Hi object, please talk")

    def sleep(self):
        print ("sleep object")

# create a object >> classname()

    def title(self):
        print ("my Title is Mr.",self.name )  # my in self, attribute in a method

shreeram = Person()    #calling of a class