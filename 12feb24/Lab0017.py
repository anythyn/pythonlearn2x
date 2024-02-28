## factorial

rang = int(input('enter the fac numb'))
if rang <0:
    print ("Fact should be +ve num")

elif rang == 0:
    print('Factorial', 1)

else:
    for i in range (1,rang+1):
       print (i)
