'''
This program prompts the user for an amount of change and calculates the minimum
number of coins required to give a user change.
--- Program written by Son Nguyen ---
'''

# Define a number of constants that shall be used later along with a boolean to
# be used for a condition
PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
bad_input = True

# Prompt the user for a numerical input of change greater than 0 as long as
# the input is not considered a bad input
while bad_input:
    try: 
        owed_value = float(input("How much change is owed?: "))
        rounded_value = round(owed_value, 2)
        totalCents = int(rounded_value * 100)
        if totalCents <= 0:
            print("Please input a value that is greater than 0")
        else:
            bad_input = False
    except:
        print("Please input a numerical value")

#Calculate the total number of coins
num_quarters = totalCents // QUARTER
remainder1 = totalCents % QUARTER
num_dimes = remainder1 // DIME
remainder2 = remainder1 % DIME
num_nickels = remainder2 // NICKEL
remainder3 = remainder2 % NICKEL
num_pennies = remainder3 // PENNY
remainder4 = remainder3 % PENNY
totalCoins = num_quarters + num_dimes + num_nickels + num_pennies

#Print the number of coins to the screen
print("Number of coins: " + str(totalCoins))

