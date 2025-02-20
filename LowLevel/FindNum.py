'''
Find Total and Highest Number
Generate a random number between 5 and 10
Tell the user that you will ask them for this number of positive numbers
Ask the user to enter that number of numbers using a loop
Display the total of all the numbers entered
Display the largest number that was entered by the user
'''
import random

nums = [6,7,8,9,]
rand_num = random.choice(nums)


print(f"Can you enter {rand_num} numbers?")

#a while loop to let the suer input numbers
total_of_nums = []
i = 1
while i <= rand_num:
    user_numbers = int(input(f"Number {i}: "))
    i = i + 1
    total_of_nums.append(user_numbers)
    
#displays the list of all the numbers that the user had entered
print(total_of_nums)

#displays the TOTAL of all the numbers entered
print(sum(total_of_nums))


#ordering the list so that the highest number takes the 0 index
total_of_nums.sort(reverse = True)
print(total_of_nums[0])
