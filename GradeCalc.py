#introductions
'''
consent = input("Hello, would you like me to find your letter grade? Yes or No?")

consent = consent.strip().lower()


if consent == "yes" or consent == "ye" or consent == "y":
    print("Cool, Lets Continue!")
else: print("Ok, Goodbye")
'''
#how many grades are being input
gradeCount = int(input("How Many Grades do you want to calculate?"))
a = []

i = 1
while i <= gradeCount:
    gradeScore = int(input(f"What is grade {i}?"))
    a.append(int(gradeScore))
    i = i + 1
  
total = sum(a)
average = total / gradeCount

print(round((average)))


#if statement, convert number grade to letters

if average >= 101:
    print("Grades Above 100 are not acceptable")
    
elif average >= 90:
    print("Congradulations on getting an A!")
    
elif average >= 80:
    print("Good Job on getting a B!")
    
elif average >= 70:
    print("Not bad, but I know you can do better than a C")
    
elif average >= 60:
    print("You got a D")
    
elif average <= 59:
    print("You have Failed, meet me after class if you wish to talk to me")
    
else:
    print("At this time I cannot reveal your grade.")