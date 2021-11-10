##Gets mode the user would like to use
mode = input("Would you like to encrypt or decrypt a message? [encrypt/decrypt]: ")

##Gets the message the user would like to encrypt
message = input("Pleaase enter the message: ")


##Encrypts message
##Creates the translated variable and adds placeholder
if mode == "encrypt":
    translated = ""

    ###Caesar Cipher Portion###

    ##For every character in the message, it is assigned a number using the ascii chart
    for i in message:
        ##If the character is a upper or lowercase letter on alphabet from A to Z
        ##it will run the folowing code
        if i.isalpha():
            ##Assigns the ascii number to a variable named num
            num = ord(i)
            ##Adds 4 to the ascii number to shift the letter down the alphabet
            ##This number can be changed to adjust shift amount
            num += 4

            ##If the character is upper case it will run the following code
            if i.isupper():
                ##If the ascii number is greater than the ascii number assigned to Z
                ##it will subtract 26 to return to the beginning of the alphabet
                if num > ord("Z"):
                    num -= 26
                    
            ##If the character is lower case it will run the following code
            if i.islower():
                ##If the ascii number is greater than the ascii number assigned to z
                ##it will subtract 26 to return to the beginning of the alphabet
                if num > ord("z"):
                    num -= 26
                    
            ##Adds the encrypted message onto the empty placeholder declared at the beginning
            ##Also translates the ascii number back to characters
            translated += chr(num)

        ##If the character isnt a letter it stays the same in the encryption
        else:
            translated += i

    ###Reverse Cipher Portion####

    ##Declares new variable for use in the reverse cipher
    final = ""

    ##Declares n as the length of the string minus 1
    n = len(translated) - 1
    ##While n is greater than 0; while there are still characters in the string
    while n >= 0:
        ##The new translation is built
        final = final + translated[n]
        ##1 gets substracted from 1 to move to the next character
        n = n - 1

if mode == "decrypt":
    translated = ""

    ###Caesar Cipher Portion###

    ##For every character in the message, it is assigned a number using the ascii chart
    for i in message:
        ##If the character is a upper or lowercase letter on alphabet from A to Z
        ##it will run the folowing code
        if i.isalpha():
            ##Assigns the ascii number to a variable named num
            num = ord(i)
            ##Subtracts 4 from the ascii number to shift the letter down the alphabet
            ##If the 4 in the "encrypt" was chnaged, this 4 needs to be changed to match
            num -= 4

            ##If the character is upper case it will run the following code
            if i.isupper():
                ##If the ascii number is less than the ascii number assigned to A
                ##it will add 26 to return to the end of the alphabet
                if num < ord("A"):
                    num += 26
                    
            ##If the character is lower case it will run the following code
            if i.islower():
                ##If the ascii number is less than the ascii number assigned to a
                ##it will add 26 to return to the end of the alphabet
                if num < ord("a"):
                    num += 26
                    
            ##Adds the decrypted message onto the empty placeholder declared at the beginning
            ##Also translates the ascii number back to characters
            translated += chr(num)

        ##If the character isnt a letter it stays the same in the encryption
        else:
            translated += i

    ###Reverse Cipher Portion###

    ##Declares new variable for use in the reverse cipher
    final = ""

    ##Declares n as the length of the string minus 1
    n = len(translated) - 1
    ##While n is greater than 0; while there are still characters in the string
    while n >= 0:
        ##The new translation is built
        final = final + translated[n]
        ##1 gets substracted from 1 to move to the next character
        n = n - 1
        
print(final)
