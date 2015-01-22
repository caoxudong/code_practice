'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

all_numbers = range(2, 2000001)
sum = 0

for x in all_numbers:
    if x == 0 :
        continue
    
    n = x
    while n <= (2000000 - x) :
        n = n + x
        all_numbers[n - 2] = 0

for x in all_numbers:
    if x == 0 :
        continue
    sum = sum + x

print(sum)
