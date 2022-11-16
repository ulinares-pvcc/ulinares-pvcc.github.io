# Name: Uzziel Vea-Linares
# Prog Purpose: This program finds the cost of a pizza order
#   Sales Tax on total: .055
#   Price for one small pizza: $9.99
#   Price for one medium pizza: $12.99
#   Price for one large pizza: $14.99
#   Price for one extra large pizza: $17.99

import datetime

################ define global variables ################
# define tax rate and prices
SALES_TAX_RATE = .055
S_PIZZA = 9.99
M_PIZZA = 12.99
L_PIZZA = 14.99
X_PIZZA = 17.99

# define global variables
pizza_size = 0 
num_pizza = 0
subtotal = 0
sales_tax = 0
total = 0

################ define program functions ################
def main():
    another_pizza = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like another pizza? (Y/N): ")
        if yesno.upper() == "N":
            another_pizza = False
            return()
        
def get_user_data():
    global pizza_size, num_pizza
    print("What size pizza would you like today: \n S for Small \n M for Medium \n L for Large \n X Extra Large ")
    pizza_size = input("Enter the pizza size: ")
    num_pizza = int(input("How many pizzas would you like today? "))
    
def perform_calculations():
    global pizzacost, salestax, totaldue
    if  pizza_size.upper() == 'S':
        pizzacost = num_pizza * S_PIZZA
        
    if  pizza_size.upper() == 'M':
        pizzacost = num_pizza * M_PIZZA
    
    if pizza_size.upper() == 'L':
        pizzacost = num_pizza * L_PIZZA
   
    if pizza_size.upper() == 'X':
        pizzacost = num_pizza * X_PIZZA
   
    salestax = pizzacost * SALES_TAX_RATE
    totaldue =  pizzacost + salestax
    
def display_results():
    print('---------------------------------')
    print('**** Palermo Pizza ****')
    print('---------------------------------')
    print('Number of pizzas ordered : ' + format(num_pizza,))
    print('Pizza size :       ' + pizza_size)
    print('Pizza cost : $ ' + format(pizzacost, '10,.2f'))
    print('---------------------------------')
    print('Sales Tax    $ ' + format(salestax, '10,.2f'))
    print('Total        $ ' + format(totaldue, '10,.2f'))
    print('---------------------------------')
    print(format(datetime.datetime.now()))
########### call on main program to execute ###########
main()
    
