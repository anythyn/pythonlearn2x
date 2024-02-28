## palindrome

str= "12"
str= str.lower()
revi=''
for v in str:
    revi = v+revi

if str == revi:
    print ('pali')
else:
    print('not a pali')
print(revi)