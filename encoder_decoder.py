def encoder(password):
    result =""
    for i in range(len(password)):
        digit = int(password[i])
        digit +=3
        result += str(digit)
    return result

