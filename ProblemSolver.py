#Using a Match Case, will solve simple math problems such as addition, subtraction, multiplication and division

'''
Step-1: Take User Input for the type of equation, +,-,* or, /
Step-2: Create cases for each type
Step-3: Ask for numbers which would go into var num1 and var num2
Step-4: Solve equation 

'''
equation = input("Type the operator you would like to use!\n (Ex.  + , - , * , / ) \n")

solve = input("Type two numbers you would like to solve,")
solve_split = solve.split(" ")

num1 = solve_split[0]
num2 = solve_split[1]

num1 = int(num1)
num2 = int(num2)
match equation:
    case "+":
        ans = (num1 + num2)
        print("The Answer is: ", ans)
    case "-":
        ans = (num1 - num2)
        print("The Answer is: ", ans)
    case "*":
        ans = (num1 * num2)
        print("The Answer is: ", ans)
    case "/":
        ans = (num1 / num2)
        print("The Answer is: ", ans)
    case _:
        print("Could not solve at this time")