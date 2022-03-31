# CTI-110
# P4HW2 - Pizza Order
# Donovan Fennell
# 30MARCH2022
#


def main():
    keep_going = "y"
    while keep_going == "y":
        students = 0
        students = int(input("How many students do you want to order pizza for? "))
        students_per = float(input("Enter number of people per pizza (1.5, 2 or 3): "))
        print()
                    
        while (students_per != 1.5 and students_per != 2 and students_per != 3):
            print("INVALID ENTRY!!!!")
            print("Should have entered 1.5, 2 or 3")
            print()
            students_per = float(input("Enter number of people per pizza again.(1.5, 2 or 3): "))
            print()
            
          
        pizzas = students / students_per
        pizza_cost = pizzas * 5
        tax = pizza_cost * .06
        price = tax + pizza_cost


        if students_per == 1.5:
            students_per = 1.5
            print("------Pizza Order---------")
            print("Number of Students :",students)
            print("Pizzas Needed :",round(pizzas))
            print("Price $" + str(format(price,',.2f')))
            print("-------------------------")
        elif students_per == 2:
            students_per = 2
            print("------Pizza Order---------")
            print("Number of Students :",(students))
            print("Pizzas Needed :",round(pizzas))
            print("Price $" + str(format(price,',.2f')))
            print("-------------------------")
        else:
            students_per == 3
            students_per = 3
            print("------Pizza Order---------")
            print("Number of Students :",(students))
            print("Pizzas Needed :",round(pizzas))
            print("Price $" + str(format(price,',.2f')))
            print("-------------------------")
        keep_going = input("Would you like to run program again(y for yes): ")

        
    
main()
