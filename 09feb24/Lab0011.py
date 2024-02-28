#score & grade

sda = int(input('enter the score \n'))
if sda >= 90 and sda <= 100:
    print("A grade")
elif sda < 90 and sda >= 80:
    print("B Grade")
elif sda < 80 and sda >= 70:
    print("C Grade")
elif sda < 70 and sda >= 60:
    print("D Grade")
else: print('invalid')
