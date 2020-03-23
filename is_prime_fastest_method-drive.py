


import math

def is_prime(x):
    if x<2:
        return False
    elif x==2:
        return True
    elif x>2:
        for t in range(2,int(math.sqrt(x)+1)):
            if x%t==0:
                return False
        return True

for x in range(1000):
    if is_prime(x):
        print (x)
    
    
