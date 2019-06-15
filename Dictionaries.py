'''
Dictionary allows you to map a kep to a value
Keys need to be unique. E.g. "age" can only be used once
Keys are case sensitive
using customer.get() with a key that doesn't exist returns a 'None'. e.g. customer("birthdate")
'''
customer =  {

    "name":"John Smith",
    "age" : "30",
    "is_verified":True
}

#iterating through a dictionary
for index in customer:
    print(customer[index])


#default value for dictionary key using the .get method
customer.get("birthday", "date")
print(customer.get("birthday", "Jan 1 1980"))

#updating a key for a dictionary
customer["name"] = "Kris Harrison"

print(customer)

#Adding key:value pairs
customer["Hometown"]="Brantford"

print(customer)