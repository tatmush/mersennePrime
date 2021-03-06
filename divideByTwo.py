
from math import *
import time #measuring the efficiency of each algorithm used

#tests if a number is prime or not, if it

def testPrime(testCase):

    #simple test
    betterTest = int(ceil(testCase/2))
    for y in range(3, betterTest, 2):
        if testPrime(y) != 0:
            if (testCase % y) == 0:
                return 0
            elif (testCase % y) != 0:
                continue
    return testCase
            
#look for mersenne prime numbers up to  99999

for x in range(3, 99999, 2):
    y = testPrime(x)
    if y != 0:
        print("testing %d" % y)
        mersennePrime = (2**y) - 1

        startTime = time.time()
        z = testPrime(mersennePrime)
        endTime = time.time() - startTime
        if z != 0:
            print("I have found a merssene prime %d" % mersennePrime)
            print("Formed after (2**%d) - 1" % y)
            print("it took me %f" % endTime)
