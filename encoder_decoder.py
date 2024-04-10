def encoder(password):
    result =""
    for i in range(len(password)):
        digit = int(password[i])
        digit +=3 # Must include an if statement checking for new digit greater than 10.  Password cannot be greater than 8 digits.
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