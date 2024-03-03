# Exceptions
# error Handling
## ctrl+d for line duplicate


a= int(input('enter A num\n'))
b= int(input('enter B num\n'))

try:
    c=a/b
    print(c)
except ZeroDivisionError as v:
    print('error is:-',v)

