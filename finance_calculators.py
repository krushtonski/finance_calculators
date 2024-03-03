import math

#Ask user to select if they want to find out their investment or bond and store as a variation "calculation_selection"
print("investment - to calculate the amount of interest you'll earn on your investment, bond - to calculate the amount you'll have to pay on a home loan. Enter either 'investment' or 'bond' from the menu above to proceed")
calculation_selection = input(":")

# Create a if/elif/else statement for investment, bond and error message if they input something else

# IF statement for investments
# Ask user to input deposit, interest, years of investment information and type of interest and save as variables
# Calculate the total repayment for simple interest and compound interest 

if calculation_selection == "investment" or calculation_selection == "Investment" or calculation_selection == "INVESTMENT":
    deposit_invest = int(input("How much is your deposit in whole numbers (without a £ or , symbol)?"))
    interest_invest = int(input("What is the interest rate (enter a whole number without the %)?"))
    years_invest = int(input("How many years do you plan to invest for (enter a whole number)?"))
    interest_type = (input("Enter 'compound' for compound interest or 'simple' for simple interest:"))

    simple_total = float(deposit_invest * (1 + ((interest_invest / 100) * years_invest))) # Calculate the total repayment for simple interest
    compound_total = float(deposit_invest * (math.pow((1+(interest_invest / 100)),years_invest))) # Calculate the total repayment for compound interest 

    if interest_type == "compound":
        print (f"You will get back £{round(compound_total,2)}") 

    elif interest_type == "simple":
        print (f"You will get back £{round(simple_total,2)}")

    else:
         interest = (input("Enter 'compound' or 'simple' for interest type:")) # Error message if user does not input compound or simple interest 
        
# Elif statement for bonds
# Ask user to input current house value, interest and repayment period in months and calculate monthly repayment
         
elif calculation_selection ==  "bond" or calculation_selection == "Bond" or calculation_selection == "BOND":
    house_value = int(input("What is your current house value (without a £ or , symbol)?"))
    interest_bond = int(input("What is the interest rate (enter a whole number without the %)?"))
    months = int(input("How many months do you plan to repay the bond (enter a whole number)?"))

    interest_bond_monthly = (interest_bond / 100 )/12 # Calculate the interest on a monthly basis
    monthly_repayment = float((interest_bond_monthly * house_value)/(1 - (1 + interest_bond_monthly)**(-months))) # Calculate the monthly repayment on the bond
    
    print (f"You will need to pay £{round(monthly_repayment,2)} a month")

# If they don't enter bond or investment, show an error message if the user does not intially input investment or bond
    
else:
    print("Sorry, this a calculator for investment or bond information. Please try again and input investment or bond")