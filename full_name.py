# Firstly we ask the user to input their full name
full_name = input("Please enter your full name: ")

# 1. Then we perform a check to see if the user has entered a full name and ensures 
#2. If there are 0 characters, the program returns this message informing the user
if len(full_name) == 0:
    print("You haven’t entered anything. Please enter your full name.")
#3. If there are less than 4 characters, the program returns a message informing the user.
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
#4. If there are more than 25 characters, the program returns a reminder for the user to check that only the full name is entered.
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
#5. If the input follows the conditions, the program returns a confirmation message thanking the user.
else:
    print("Thank you for entering your name.")