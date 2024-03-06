#car example for object-class

class Car():
    name= None
    make=None
    color= None
    engine = None
    driver = None

    def start_engine(self):
        print("engine starting _method")

    def drive(self):
        print("car driving _method2")

    def fueling(self):
        print("car feuling in gas station _method3")

    def who_is_driving(self):
        print("The driver name is", self.driver)

suzu_object = Car()
suzu_object.driver ="Nithin"
suzu_object.who_is_driving()
suzu_object.drive()
suzu_object.fueling()



