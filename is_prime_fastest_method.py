
# In this video we are going to discuss about a method to check whether a given number is a prime or not . 

import math

def is_prime(x):
    if x<2:
        return False
    elif x==2:
        return True
    elif x>2:
        for t in range(2,int(math.sqrt(x)+1)): ### To make faster we use a property in a prime related to square root .
            if x%t==0:
                return False
        return True

#this is the faster method we will discuss about an slower method in next video
#IA

#lets test

############# TESTING ##################


for x in range(1000):
    if is_prime(x):
        print (x)
    
    
