
# Name: Uzziel Vea-Linares
# Prog Purpose: This program finds the weekly pay of employees
#   Pay for Cashier : $16.50
#   Pay for Stocker : $15.75
#   Pay for Janitor : $15.75
#   Pay for Maintenance : $19.50

import datetime

################ define global variables ################
# define tax rate and prices
CASHIER = 16.50
STOCKER = 15.75
JANITOR = 15.75
MAINTENANCE = 19.50
FEDERAL_RATE = .12
STATE_RATE = .03
SOCIAL_RATE = .062
MEDICARE_RATE = .0145

# define global variables
gross_pay = 0 
deduction_1 = 0
deduction_2 = 0
deduction_3 = 0
deduction_4 = 0
deduction_total = 0
actual_pay = 0
job_type = 0
num_hours = 0

################ define program functions ################
def main():
    another_check = True
    while another_check:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to see another employee rate? (Y/N): ")
        if yesno.upper() == "N":
            another_check = False
            return()
        
def get_user_data():
    global job_type, num_hours
    print("Which employee are you calculating: \n C for Cashier \n S for Stocker \n J for Janitor \n M Maintenance ")
    job_type = input("Enter Job: ")
    num_hours = int(input("Number of hours worked? "))
    
def perform_calculations():
    global gross_pay, deduction_1, deduction_2,deduction_3,deduction_4,deduction_total, actual_pay, job_type, num_hours
    if  job_type.upper() == 'C':
        gross_pay = num_hours * CASHIER
        
    if  job_type.upper() == 'S':
        gross_pay = num_hours * STOCKER
    
    if job_type.upper() == 'J':
        gross_pay = num_hours * JANITOR
   
    if job_type.upper() == 'M':
        gross_pay = num_hours * MAINTENANCE
   
    deduction_1 = gross_pay * FEDERAL_RATE
    deduction_2 =  gross_pay * STATE_RATE
    deduction_3 =  gross_pay * SOCIAL_RATE
    deduction_4 =  gross_pay * MEDICARE_RATE
    deduction_total = deduction_1 + deduction_2 + deduction_3 + deduction_4
    actual_pay = gross_pay - deduction_total
    
def display_results():
    print('---------------------------------')
    print('**** Weekly Pay ****')
    print('---------------------------------')
    print('Number of Hours Worked:           '      +str (num_hours))    
    print('Federal Income:                $'+format (deduction_1,'8,.2f'))
    print('State Income:                  $'+format (deduction_2,'8,.2f'))
    print('Social Security:               $'+format (deduction_3,'8,.2f'))
    print('Medicare:                      $'+format (deduction_4,'8,.2f'))
    print('Total Deduction:               $'+format (deduction_total,'8,.2f'))
    print('Gross Pay:                     $'+format (gross_pay,'8,.2f'))
    print('Net Pay:                       $'+format (actual_pay,'8,.2f'))
    print('---------------------------------')
    print(format(datetime.datetime.now()))
########### call on main program to execute ###########
main()
    
