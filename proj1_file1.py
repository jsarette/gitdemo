#
# Class: Udemy - Modern python 3 Bootcamp
# 
# File Name: myName.py 
#  --------------------------

import sys 

from random import choice, randint
 

# ------------------------------
#  print ("Sys Ver:" + sys.version)
#  print ("Exe: " + sys.executable)

age = 69

round (age, 2)
print (age)
# print ( f"File Name: myName.py by Jim Sarette who is {age} years old")


# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================
calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# calling_in_sick = False 
print (f"actually  Sick ?: {actually_sick}" )
print (f"Kinda Sick ?: {kinda_sick}" )
print (f"Sick days?: {sick_days}" )


if (sick_days > 1):
    if (actually_sick==True):
        calling_in_sick = True
    elif(kinda_sick and hate_your_job):
        calling_in_sick = True
    else:
        calling_in_sick = False
else:
    calling_in_sick = False
    print ("Not calling in sick  " )

if calling_in_sick:
    print ("Calling in Sick is OK")