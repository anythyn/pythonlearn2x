# triangle clasifier

print('enter the sides of a triangle')
a = float(input('enter the length of first side '))
b = float(input('enter the length of second side '))
c = float(input('enter the length of third side '))
if a == b== c:
    print('equivalent triangle')
elif (a == b) or (a == c) or (b == c):
    print('isosceles triangle')
else:
    print("scalene traingle")
