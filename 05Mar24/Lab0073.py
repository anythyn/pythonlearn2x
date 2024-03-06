# object -class> user input inside a method

class Car_user():
    color= None
    model = None
                                #to use class variables we need self
    def car_deets(self):
        print("your car details is",self.color," color",self.model)

car_color= input("enter the color")
car_model= input("enter the model")

car_obj_ref=Car_user()
car_obj_ref.color = car_color
car_obj_ref.model = car_model
car_obj_ref.car_deets()



