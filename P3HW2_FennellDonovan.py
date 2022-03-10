# CTI-110
# P3HW2 - Pizza Order
# Donovan Fennell 
# 03MARCH2022

students = int(input('How many students do you want to order pizza for? '))
students_per = float(input('Enter number of people per pizza (1.5, 2 or 3):'))
print()

pizzas = students / students_per
pizza_cost = pizzas * 5
tax = pizza_cost * .06
price = tax + pizza_cost

if students_per == 1.5:
    students_per = 1.5
    print('------Pizza Order---------')
    print('Number of Students : ',(students))
    print('Pizzas Needed :',round(pizzas))
    print('Price $',(price))
    print('-------------------------')
elif students_per == 2:
    students_per = 2
    print('------Pizza Order---------')
    print('Number of Students : ',(students))
    print('Pizzas Needed :',round(pizzas))
    print('Price $',(price))
    print('-------------------------')
elif students_per == 3:
    students_per = 3
    print('------Pizza Order---------')
    print('Number of Students : ',(students))
    print('Pizzas Needed :',round(pizzas))
    print('Price $',(price))
    print('-------------------------')
else:
     print('INVALID ENTRY!!!!')
     print('Should have entered 1.5, 2 or 3\n')
     print('Run Program again')
     print()


