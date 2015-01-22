'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

primeArray      = [2,3]
targetCount     = 2
nextNumber      = 4
isPrime         = False

while (targetCount != 10001) :
    
    isPrime = True
    for e in primeArray:
        if nextNumber % e == 0:
            isPrime = False
            break
    
    if isPrime == True:
        primeArray.append(nextNumber)
        targetCount = targetCount + 1
    
    nextNumber = nextNumber + 1

print(primeArray.pop())
