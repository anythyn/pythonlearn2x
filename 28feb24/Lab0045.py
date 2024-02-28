# list is collection of items
# multiple type of Datatypes,
# Duplicate items allowed
my_list = [1,2,33]

# indexing
#[0,1,2,3]
#[-3,-2,-1]
print(my_list[0])
print(my_list[-1])
print(my_list.index(33))


#changing the list
my_list[1] = True
print(my_list)

#append the list -- add at the end --one item
my_list.append(4)
print(my_list)

#extend by list -- Add list to list
my_list.extend([55,66,'a'])
print(my_list)

# insert a value/index inbetween the list
my_list.insert(3,3.5)
print(my_list)

#remove
my_list.remove(1)
print(my_list)


#copy of the list
copy_list = my_list.copy()
print(copy_list)


#clear the list
my_list.clear()
print(my_list)
print(copy_list)

# sort the list
# copy_list.sort()
# print(copy_list)


# reverse the list
copy_list.reverse()
print(copy_list)

#not in list
empty_list=[]
if not empty_list:
    print('empty')
else:
    print('not empty')

#pop
# Remove and Return the value of the index
#BY default removes the last value
list1=[1,2,5]
print(list1.pop(1))
print(list1)