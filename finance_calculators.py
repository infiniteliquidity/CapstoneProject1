#========= Title =========
"""
Task 5 Capstone Project
finance_calculators.py
James Allan JA22120007634
DFE Hyperion Data Science 
"""



#======== Pseudocode ==========
"""
This program defines functions for investment and bond calculations.

* The program begins by importing the math library.
* It then defines two functions:
    * investment: Calculates investment amount based on simple or compound interest.
    * bond: Calculates monthly bond repayment.

Both functions prompt the user for input, perform calculations, and display rounded results.
"""


# Start
import math


# Define functions
def investment():
    """
    Calculates the future value of an investment based on principal, interest rate, and time.
    Handles both simple and compound interest.
    """

    while True:
        try:
            P = float(input("Enter the amount of money you are depositing: "))
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
        if interest in ("simple", "compound"):
            break
        else:
            print('Invalid input. Please enter "simple" or "compound" :')

    # Convert percentage value for r into a decimal representation
    r = r / 100

    # Use an if/elif loop to determine the calculation based on interest type
    if interest == "simple":
        A = P * (1 + r * t)
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Error: Invalid input")
        return

    # Print the result with rounded value to 2 decimal places
    print("Your investment will be worth $", round(A, 2))


def bond():
    """
    Calculates the monthly bond repayment amount.
    """

    while True:
        try:
            P = float(input("Enter the present value of the house: "))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value of the house: ")

    while True:
        try:
            r = float(input("Enter the interest rate (as a percentage): "))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value for the interest rate (as a percentage): ")

    while True:
        try:
            n = int(input("Enter the number of months you plan on taking to repay the bond: "))
            break
        except ValueError:
            print("Invalid input. Please enter a correct value for the number of months you plan on taking to repay the bond:")

    # Convert the percentage value for r into a decimal per month
    r = (r / 100) / 12

    # Calculate the monthly bond repayment
    repayment = (r * P) / (1 - math.pow((1 + r), -n))

    # Print the result with rounded value to 2 decimal places
    print("Your monthly repayment will be $", round(repayment, 2))


# Main program
print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment bond")
print("bond - to calculate the amount you'll have to pay on a home loan")


# Ensure user enters a valid choice ("investment" or "bond")
while True:
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if choice in ("bond", "investment"):
        break
    else:
        print("Please make sure you have entered either 'bond' or 'investment'")

# Call the chosen function based on user input
if choice == "investment":
    investment()
elif choice == "bond":
    bond()
else:
    print("Error: Invalid input")
