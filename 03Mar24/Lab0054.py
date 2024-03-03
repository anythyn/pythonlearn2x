# multiple assignments
x=10
a,b = 12,23
q,w,e= (12,45,78)

#nested tuples
hero1 = ('bhagat','azad')
hero2 = ('vivek','savarkar')
my_heros = hero1+hero2
print (my_heros)  # concatenate tuples

heroes = ( hero1,hero2)
print ("nested tuple: ",heroes)  # nested tuples

print ("nested tuple: ",heroes[0])
# only azad
print ("nested tuple: ",heroes[0][1])
print ("nested tuple: ",heroes[1][1])