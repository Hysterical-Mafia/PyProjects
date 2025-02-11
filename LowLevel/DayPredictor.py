'''
Day Predictor
a. Randomly select a predicted outlook for the day from six possibilities
b. Display this in the following format:
Today... <outlook>
e.g. Today... you will have a great day!
''' 

import random

outlook = [
    "Today, you will have a sunny day!",
    "Today, you will have a rainy day!",
    "Today, you will have a cloudy day!",
    "Today, you will have a snowy day!",
    "Today, you will have a foggy day!",
    "Today, you will have a humid day!",
]

prediction = random.choice(outlook)

print(prediction)
