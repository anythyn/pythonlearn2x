# args
# cannot have 2 args
def pizza_topping(*topping,base='Normal'):
    print("Toppings are",topping,"; Base is",base)
    return topping,base #multiple things are returned and fetched

pramod= pizza_topping("Garlic","Onion","Tomato","celery",base='cheese burst')
Nithin = pizza_topping('Mushroom', base='Thin')
shruthi = pizza_topping('pineapple','babycorn','sweetcorn','paneer') # if base is not mentioned default values are displayed, if there is no base in arguement then error'
print(shruthi)