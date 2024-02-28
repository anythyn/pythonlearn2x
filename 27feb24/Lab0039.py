
# args and Kargs

def adding_of_numbers(*args):  # instaed of defing arguments like def new(a,b,c),
    return sum(args)           # args will be taken care of defining the arguements automatically

result=adding_of_numbers(2,2,8975489,1231,45,71,154,16,41,485,4)
print(result)


something = adding_of_numbers(21.1,25.1,1584512.212,415.2,12311,154,415,6385,74541)
print(something)


one = adding_of_numbers(21)
print(one)

