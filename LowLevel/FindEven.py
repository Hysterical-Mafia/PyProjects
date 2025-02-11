''' 
Find an Even Number
a. In the main function, ask the user to enter a number
b. Write a function which works out if the number is even or not

If it is even, print "Even number"
If it is not even, print "Odd number"

c. Continue to ask for numbers until the user enters an even one
Hint: You will need the modulus (%) operator
'''
def main():
    user_num = int(input("Enter a number: ")) 
    check_even_odd(user_num)


def check_even_odd(user_num):
    if user_num % 2 == 1:
        print(f"{user_num} is an odd number\n")
    else:
        print(f"{user_num} is an even number\n")
     
       
    if user_num % 2 != 0:
        main()

    
main()