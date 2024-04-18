#========= Title =========
"""
Task 5 Capstone Project
finance_calculators.py
James Allan JA22120007634
DFE Hyperion Data Science 
"""


#========= Pseudocode ==========
"""
I want to create two functions for this program - One for either calcluation
This will be a cleaner way of writing the code, easier to service, and less prone to mistakes in the syntax


* The program will begin by calling the "math" library
* Next I will define the first function "investement" - This function will be called after the user has selcted "investment" from the opening menu
   
   (Investment function)
    * The "investment" function will ask the user to input data for the amount of money, interest rate, and number of years investing
    * The user will then be propted to decide if they want to use "simple" or "compound" interest - an infinate loop is to be used to ensure accurate data entry
    * An if/elif loop will determine which calculation (simple or compound) to process the calculation and print to a variable
    * The function ends by printing the variable using the "round" function to translate a float into a string
    
    (Bond function)
    * The second function will be called "bond" and will be called after the user has slected "bond" from the opening menu
    * The "bond" function begins by asking the user to input data for the value of the house, the interest rate, and the number of months planned to repay
    * The data stored for these variable is then used to calculate the repayment of the bond calling on the "math" library
    * The function ends by printing the variable using the "round" function to translate a float into a string
"""


# start

import math

#----- define functions-----#

def investment():
    
    # start of investment functon - called when user selects "investment" from the main menu 
    """
        request user to input values for amount of money, interest rate, and length of investment
        an infinate loop to ensure that the program does not break when a user enters an incorrect variable type
        a second type of infinate loop is used to capture the exact data input when requested to enter "simple" or "compound"    
    """


    while True:
        try:
            P = float(input("Enter the amount of money that you are depositing: "))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value for the amount of money you are depositing: ")

    while True:
       try:
           r = float(input("Enter the interest rate (as a percentage): "))
           break    
       except ValueError:
            print("Invalid input. Please enter a correct value for the interest rate (as a percentage)")
        
    while True:
        try:
            t = float(input("Enter the number of years you plan on investing: "))
            break 
        except ValueError:
            print("Invalid input. Enter the number of years you plan on investing")
       
    while True:
        interest = input('Do you want "simple" or "compound" interest? :').lower()
        if interest == "simple" or interest == "compound":
            break
        else:
            print('Invalid input. Please enter "simple" or "compound" :')
            


    # convert the percentage value for r into a decimal representation 
        
    r = r/100   

    
    # using an if/elif loop to determine the calculaton - determined by value input for "interest"
        
    if interest == "simple":
        A = P * (1 + r * t)
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Error: Invalid input")
        return
    
    
    # after the calculaton the result is printed back to the user using the "round" functon to keep make sure the answer is rounded to 2dp. This is also a tidy way of printing the float without converting
        
    print("Your investment will be worth $",round(A, 2))

    
    # end of investment function
    


def bond():
    
    # start of bond function - called when user selects "bond" from the main menu

    """
        request user to input values for value of thei house, interest rate, and length of repyament on the bond
        an infinate loop to ensure that the program does not break when a user enters an incorrect variable type
    """
    
    
    # request user to input values for value of house, interest rate, and length of repayment 
   
    while True:
        try:
            P = float(input("Enter the present value of the house :"))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value of the house: ")

    while True:
        try:
            r = float(input("Enter the interest rate (as a percentage) :" ))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value for the interest rate (as a percentage) : ")

    while True:
        try:
            n = int(input("Enter the number of months you plan on taking to repay the bond :"))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value for the number of months you plan on taking to repay the bond :")
            
    
    # convert the percentage value for r into a decimal 
         
    r = (r/100)/12
        
    
    # calculating the value of the bond
        
    repayment = (r * P) / (1 - math.pow((1+r), -n))
        
    
    # after the calculaton the result is printed back to the user using the "round" functon to keep make sure the answer is rounded to 2dp. This is also a tidy way of printing the float without converting
         
    print("Your monthly repayment will be $",round(repayment, 2))

    
    # end of bond function




#----- main program outline -----#
''' 
    user given two optons for the finance calculator 
    prompted to input either "bond" or "investment"
    the program will convert all entries to lower case to remove case sensitive entries 
    the program will use an infinite loop to ensure the user enters either "bond" or "investment"
'''

# main progran menu

print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment bond")
print("bond - to calculate the amount you'll have to pay on a home loan")


# infinate loop to ensure that the user enters a correct value for "investment" or "bond"

while True:
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if choice == "bond" or choice == "investment":
        break
    else:
        print("Please make sure you have entered either 'bond' or 'investment'")


# assignng user's selection to the varable "choice" - this will determine which function to call

if choice == "investment":
    investment()
elif choice == "bond":
    bond()
else:
    print("Error: Invalid input")
