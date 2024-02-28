# functions with default value

def your_name(nia="Admin"):
    print ("Your name is:",nia)


enter =input("ENter A or B")

if enter == 'A':
    your_name("Nithin")
else:
    your_name()