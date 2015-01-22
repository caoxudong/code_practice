'''
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
    a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

n = 1000
a = 1
b = 1
c = 1
result = 0

while a < n:
    b = a + 1
    while b < n:        
        c = 1000 - a - b
        if c*c == a*a + b*b:
            result = a * b * c
            break
        b = b + 1
    if result != 0:
        break;
    a = a + 1
print(a,b,c,result)
