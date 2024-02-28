
num1 = int(input('first no,'))
num2 = int(input('first no,'))
num3 = int(input('first no,'))

maxi =max (num1,num2,num3)
print( maxi)

if num1>num2 and num1>num3:
    print('max is',num1)
elif num3>num1 and num3>num2:
    print ('max si',num3)
else:
    print ('max si', num2)