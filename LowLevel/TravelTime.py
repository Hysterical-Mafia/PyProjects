'''
Travel Time
a. Ask the user how many minutes it takes them to travel home each day
b. Display a message to say how many minutes that is per month (assume 30 days per month)
'''

time_to_travel = int(input("How many minutes does it take you to travel home each day?"))
if time_to_travel < 0:
    print("Not Accepted")
else:
    total_in_minutes = time_to_travel * 30
    total = total_in_minutes / 60
    
print(total_in_minutes)
print(total)