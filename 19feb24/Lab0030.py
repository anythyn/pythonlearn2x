# find vowels and consonants

vari = input("enter the line/ words to count the vowels or characters\n")

v=c=0
for vari in (vari):
    if vari=="a" or vari=='e' or vari=='i' or vari=='o' or vari=='u':
        v=v+1
    else :
        c=c+1
print ('vowels count=', v,'\nconsonants count =',c)