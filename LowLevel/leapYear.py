#Leap Year Calc

#Enter a Year
year = int(input("Enter a Year: "))

#Checks if that Year is a Leap Year
def is_leap():
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
is_leap()
