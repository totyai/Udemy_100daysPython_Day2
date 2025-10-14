#Tip calculator

'''
1. Print, "Welcome to the tip calculator."
2. Ask you for an input for how much the total bill came to.
3. ask you, "What percentage tip would you like to give?"
4. Ask, "How many people are splitting this bill?"
Output: should tell us that each person should pay with 2 decimal places
'''

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#tip = 1+tip/100
people = int(input("How many people are splitting this bill? "))
print(f"Each person should pay: ${round((total*(1+tip/100))/people,2)}")
