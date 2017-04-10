
import time
#lucas-lehma test
#this is the best available primality test formed after the lucas-lehma sequence:
#[4, 14, 194] (x**2 -1)
#we are testing if the n-1th term in the series is divisible by
#by 2**n -1
#if it is then 2**n - 1 is prime

def isPrime(x):
    CONSTANT = 4
    for num in range(1, x-1):
        CONSTANT = ((CONSTANT**2) -2) % ((2**x) -1)
    if CONSTANT == 0:
        return True
    else:
        return False

for i in range(3, 999999, 2):
    if i % 5 == 0:
        continue
    else:
        
        startTime = time.time()
        if isPrime(i):
            endTime = time.time() - startTime
            print("(2**%d) - 1 is merssene prime" % i)
            print("It took me %f to find it." % endTime)
        else:
            continue
