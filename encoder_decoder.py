#Isabella Goodwin
def encoder(password):
    result =""
    for i in range(len(password)):
        digit = int(password[i])
        digit +=3 # Must include an if statement checking for new digit greater than 10.  Password cannot be greater than 8 digits.
        if digit >9:
             digit -= 10
        result += str(digit)
    return result

def decoder(password):
    
    result = ""
    
    for i in range(len(password)): # Iterates through password.
        digit = int(password[i]) # Conforms string to integer, for function's sake.
        digit -= 3 # Subtracts three to encode.
        if digit < 0: # Negative numbers aren't permitted, so when number is less than three,
            digit += 10 # add 10 to compensate.
        result += str(digit) # Adds decoded digit to resultant string.
    
    return result

def main():
    flag = True
    while flag:
        print("Password Encoder ")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        option = int(input("Enter option number: "))
        if option == 3:
            flag = False
            print("Thanks for using Password Encoder!")
            break
        elif option == 1:
            passcode = input("Enter password to be encoded(8 digits): ")
            passcode = encoder(passcode)
            print("Password encoded!")
        elif option == 2:
            passcode = input("enter password to be decoded(8 digits): ")
            passcode = decoder(passcode)
            print("Password decoded!")
        print()
main()