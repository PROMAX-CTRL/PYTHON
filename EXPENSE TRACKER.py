week = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]

# Function to handle all expense input and daily/weekly totaling for one week.
def expenses():
    total = 0
    while True:
        dailyExpense = []
        for day in week:
            dailyTotal = 0
            while True:
                expense = input(f"Enter expenses for {day}: $") # Prompt user for input expense
                if expense.lower() == "x": # Allow exit option
                    break
                try:
                    num = float(expense)
                    if num < 0: # Data validation: prevent negative expenses.
                        print("Expense cannot be a negative number. Please enter a valid amount.")
                        continue  
                    dailyTotal += num
                # Handle invalid input (non-numeric values)
                except ValueError: # Data validation: handle non-numeric input. #reference
                    print("Invalid Input. Please try again")
            dailyExpense.append(dailyTotal)  
            total += dailyTotal
            print() #This is to leave a space after each day
        return total, dailyExpense
        
# Display initial instructions for the user
print("Welcome to the expense tracker")
print ("Type 'x' to proceed to the next day")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #to underline the above instruction for visibility

while True: #Main loop to allow tracking of expenses for multiple weeks
    total, dailyExpense = expenses()
    # Weekly calculations
    avg = round(total/7,2) 
    highest =  max(dailyExpense)
    lowest = min(dailyExpense)
    maxDay = dailyExpense.index(highest) 
    minDay = dailyExpense.index(lowest)   
        
    #Summary for week
    print(f"This week's total expense was : ${total}")
    print(f"This week's average expense was: ${avg}")
    print(f"The day with the highest expense was {week[maxDay]} (${highest})")
    print(f"The day with the lowest expense was {week[minDay]} (${lowest})")
    print() 
    
    # Prompts user to continue or terminate, with input validation
    while True:
        nextWeek = input("Do you want to enter next week's expenses? (Y/N): ").lower()
        if nextWeek  == 'n':
            print("Thank you!")
            break 
        elif nextWeek  == 'y':
            print("")
            print("Proceeding with next week's expenses...")
            break
        else:
            print("Invalid Input. Please enter 'Y'es or 'N'o. Try again.")
    if nextWeek  == 'n':
        break 
            

    
            
    
        


