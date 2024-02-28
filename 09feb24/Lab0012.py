## Assignment for Leap year
## Logic--> Divisible by 4 and not divisible by 100

yea = int(input('Enter the Year to check\n'))

if (yea % 4 == 0) and (yea % 100 != 0):
    print("This is a leap year", yea)

elif (yea % 400 == 0):
    print("This is a leap year", yea)

else:
    print("not a leap year", yea)
