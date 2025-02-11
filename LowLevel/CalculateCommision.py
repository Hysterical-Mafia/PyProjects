'''
Calculate commission
a. Ask the user to enter the salesman's name
b. Ask the user to enter the value of the goods sold by the salesman
c. Calculate and print the commission due to the salesman
i.  If the value of goods sold is less than 50 then the commission rate is 0%
ii. Otherwise, if the value of goods is less than 200, the commission rate is 5%
iii.    Otherwise, the commission rate is 10%
'''

salesman_name = input("What is the Salesman's name?")
salesman_goods = float(input("What is the value of the Salesman's goods?"))

if salesman_goods < 50:
    total = salesman_goods
elif salesman_goods < 200:
    total = salesman_goods * 0.05
else:
    total = salesman_goods * 0.1
    
print(total)