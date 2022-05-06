passwordList = ['12345', '123456789', 'qwerty', 'password', '12345', 'qwerty123', '1q2w3e', '12345678', '111111', '1234567890']        
usedPasswords = []

while True:
    userInput = input("Enter a password: ")
    if userInput in passwordList:
        print("Invalid entry! Common passwords cannot be utilized. Please try again.")
        continue
    elif userInput in usedPasswords:
        print("This password has already been used. Please try again.")
        continue
    else:
        usedPasswords.append(userInput)
        print(usedPasswords)
        break
        