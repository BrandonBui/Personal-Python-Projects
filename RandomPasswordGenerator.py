##Importing random module so that we can have a randomized password
import random
##Importing string so we can use different characters
import string
##Importing time module to use as a delay
import time

print("Hello! Welcome to the random password generator!")

def randomPasswordGenerator():

    ##Asks user how long they want their password to be and sets it as a variable
    passwordLength = int(input("Please enter how many characters you would like the password to be: "))
        
    ##Defines password data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = "!" + "@" + "#" + "$" + "%" + "&" + "?" + "+" + "="

    ##Combines data into three variables depending on password strength
    combLow = lower + upper
    combMed = lower + upper + num
    combHigh = lower + upper + num + symbols

    ##Asks user what strength they would like
    passwordStrength = input("Which strength would you like? [Low, Medium, High]: ")

    ##If user selects low strength, it will create a password with letters only
    if passwordStrength == "Low" :
        
        ##Chooses a random choice for each variable
        tempPass = random.choices(combLow,k = passwordLength)

        ##Combines all the randomized variables into one password
        password = "".join(tempPass)

        print(password)

    ##If user selects medium strength, it will create a password with letters and numbers
    elif passwordStrength == "Medium" :
        ##Chooses a random choice for each variable
        tempPass = random.choices(combMed,k = passwordLength)

        ##Combines all the randomized variables into one password
        password = "".join(tempPass)

        print(password)
        
    ##If user selects strong, it will create a a password with letters, number, and symbols
    elif passwordStrength == "High" :
        ##Chooses a random choice for each variable
        tempPass = random.choices(combHigh,k = passwordLength)

        ##Combines all the randomized variables into one password
        password = "".join(tempPass)

        print(password)

    #If user doesn't input one of the selections, it will restart the generator
    elif passwordStrength != "Low" or "Medium" or "High" :
        print("You have entered an invalid choice, please restart.")
        time.sleep(1)
        randomPasswordGenerator()
        
    ##2 second delay
    time.sleep(2)

    ##Asks user if password is sufficient
    sufficientPassword = input("Is this password sufficient? [y/n]: ")

    ##If the password is sufficient it will thank the user and end the program
    if sufficientPassword == "y" :
        print("Thank you for using the random password generator!")

    ##If the password isn't sufficient it will run the program again
    if sufficientPassword == "n" :
        randomPasswordGenerator()

##Calls the function
randomPasswordGenerator()
