# factorial in function

def facto():
    fact = 1
    for i in range(1, Numb + 1):
        fact = fact * i
    print(fact)

Numb= int(input('Enter the value for which factorial needs to be provided'))
facto()
