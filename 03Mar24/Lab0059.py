
set2 = {1,2,3,4}
set3 = {3,4,5,6}

seta= set2.union(set3)
print (seta)

setb= set2.difference(set3)
print (setb)
setc= set3.difference(set2)
print (setc)


set4 = {3,6}

print(set4.issubset(set3))
print(set4.issubset(set2))