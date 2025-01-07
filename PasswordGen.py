#Password Generator
import random
#import string will allow me to use all ascii letters as well as decimal digits without manually writing them down
import string

#creates a list which includes all possible characters
all_poss_char = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

    #Ask User for length of password
userPassLength = int(input("How many characters should the password be?"))

userSpecialChar = input("Would you like to have special characters included, Yes or No? ")
userSpecialChar = userSpecialChar.strip().lower()
    

def generate_password(): 
    if userSpecialChar == "yes":
        all_poss_char = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) 
    else:
        all_poss_char = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

#create loop for the pass generation
    fin_pass = []
    i = 1
    while i <= userPassLength:
        pass_char = random.choice(all_poss_char)
        i = i +1
        fin_pass.append(pass_char)
   
    final_password = ''.join(fin_pass)
    return(final_password)

print(generate_password())

#would user like to create another password?
userPassNum = input("Would you like to create another password?")
userPassNum = userPassNum.strip().lower()
if userPassNum == "yes":
    amount_of_passwords = int(input("How many passwords would you like to generate?"))
    for x in range(amount_of_passwords):
        password = generate_password()
        print(password)  
elif userPassNum == "no": 
    print("Goodbye")
else:
    print("Invalid Input.")
        
        
        