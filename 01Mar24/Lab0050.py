# filter
# it can filter the items based on logic and return less number of items
# filter can be added only on functions

numb_r= [1,2,3,4,5]

def evn_nu(num):
    return num%2==0

even_num= filter(evn_nu,numb_r)
print(list(even_num))
