# object - class- Multiple parameter in a class

class Mul_param():
    #Name = None >> class variable
    def print_info(self,f_name,last_name, age):
        a= 10        #Local variable
        print("your name is:", f_name+" "+last_name,"and you are",age,"years young")

cal_class = Mul_param()
print(cal_class.print_info("Bhagat", "singh",23))