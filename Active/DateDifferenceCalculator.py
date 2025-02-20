'''
 Date Difference Calculator
Core Features:
1. Basic Date Difference Calculation
    Users enter two dates (Start Date and End Date).
    The program calculates the difference in:
    Days
    Weeks (Rounded to the nearest full week)
    Months (Approximated by considering month lengths)
    Years (Taking leap years into account)
2. Leap Year Handling
    Identify if a year is a leap year using the formula:
    A year is a leap year if:
    Divisible by 4 AND
    Not divisible by 100 UNLESS also divisible by 400
    Adjust the day count when calculating across leap years.
3. Working Days Calculation (Excluding Weekends)
    Only count Monday to Friday (weekends are ignored).
    Can use Python's numpy or pandas to efficiently count weekdays.
4. Holiday Exclusion (Optional)
    Allow users to define a list of public holidays.
    If a holiday falls within the date range, it is subtracted from the working days.
    Can use a predefined holiday database (holidays library for country-specific holidays).
5. Date Format Flexibility
    Accept different date formats:
    YYYY-MM-DD, DD-MM-YYYY, MM/DD/YYYY, etc.
    Validate input to prevent incorrect formats.
6. User-Friendly Output
    Display results clearly:
    "The difference between Jan 1, 2024 and March 1, 2024 is 60 days, 8 weeks, or 2 months."
    Allow users to select the desired unit of output.
8. Date Addition/Subtraction Feature
    Allow users to add/subtract a certain number of days, weeks, months, or years to/from a given date.
'''



def run_date_difference():
        #Days, Weeks, Months, Years
    difference_type = difference_in_x()
        #Y-M-D, D-M-Y, M/D/Y
    format_type = date_format()
    print(f"Using this format '{format_type}':" )
        #getting the dates
    user_start_date = input("Start Date: \n")
    user_end_date = input("End Date: \n")

        
    
   



def date_format():
    formats_for_date = ["YYYY-MM-DD", "DD-MM-YYYY", "MM/DD/YYYY"]
    
    #creates a numbered list for each format type
    for i, format_type in enumerate(formats_for_date, start=1):
        print(f"{i}: {format_type}")
    format_chosen =  int(input("Choose the format you would like to use:\n"))
    
    #since the numbered list starts at 1, subtract it in the end to get the true index, if they choose 2,
    # it would technically be at index 1 since 0,1,2 is how it actually is instead of 1,2,3
    chosen_format = formats_for_date[format_chosen - 1]
    return chosen_format
            
    
def difference_in_x():
    difference_types = ["Days","Weeks","Months","Years"]
    for i, diff_type in enumerate(difference_types, start = 1):
        print(f"{i}: {diff_type}")
        
    type_chosen = int(input("How would you like to check the difference: \n"))
    
    chosen_type = difference_types[type_chosen - 1]
    return chosen_type
    
run_date_difference()
