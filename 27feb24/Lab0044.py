# #without return
#
# def doub():
#     new=  old*2
#     print (new)
#
# old = int(input('enter the old salary'))
# doub()
#
# #with return
# def doub(old):
#     return old*2
#
# old = int(input('enter the old salary'))
# new = doub(old)
# print(new)

# lambda function
doub = lambda old:old*2
old = int(input('enter the old salary'))
print (doub(old))

