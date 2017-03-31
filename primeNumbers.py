
from math import *

#tests if a number is prime or not, if it
#is then that number is returned else 0
def testPrime(testCase):

    betterTest = int(sqrt(testCase))
    for y in range(3, betterTest, 2):
        if (testCase % y) == 0:
            return 0
        elif (testCase % y) != 0:
            continue
    return testCase
            
#look for mersenne prime numbers
for x in range(3, 999999, 2):
    y = testPrime(x)
    if y != 0:
        print("testing %d" % y)
        power = (2**y) - 1
        
        z = testPrime(power)
        if z != 0:
            print("I have found a merssene prime %d" % power)
            print("Formed after %d" % y)

