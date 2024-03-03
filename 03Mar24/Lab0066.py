# dictionaries are similar to json
# real examples of JSON

api_response ={
    "first_name" :"shruthi",
    "age":33,
    "last_name":"Jagannath",
    "email":"shr@gmail.com",
    "password":"pass"
}

print(api_response)
print(type(api_response))
api_response["password"]="shruhyr"
print(api_response.get("password"))