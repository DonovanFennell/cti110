print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

service1 = input("Select first service:\n")
service2 = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

if service1 == ("Oil change"):
    service1 = "Oil change, $35"
    price1 = 35
elif service1 == ("Tire rotation"):
    service1 = "Tire rotation, $19"
    price1 = 19
elif service1 == ("Car wash"):
    service1 = "Car wash, $7"
    price1 = 7
elif service1 == ("Car wax"):
    sevice1 = "Car wax, $12"
    price1 = 12
else:
    service1 = "No service"
    price1 = 0
                
print("Service 1:", service1)

if service2 == ("Oil change"):
    service2 = "Oil change, $35"
    price2 = 35
elif service2 == ("Tire rotation"):
    service2 = "Tire rotation, $19"
    price2 = 19
elif service2 == ("Car wash"):
    service2 = "Car wash, $7"
    price2 = 7
elif service2 == ("Car wax"):
    service2 = "Car wax, $12"
    price2 = 12
else:
    service2 = "No service"
    price2 = 0

print("Service 2:", service2)
print("")

print("Total: $", price1 + price2,sep='')



