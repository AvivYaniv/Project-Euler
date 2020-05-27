import math

DESIRED_NUMBER_OF_DIGITS        =  1000

index = 3
a = 1
b = 2
c = a + b
while len(str(c)) < DESIRED_NUMBER_OF_DIGITS:    
    c = a + b
    a = b
    b = c
    index += 1
    
# 4782
print index
