'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


numbers = range(1, 1000000)
max_length = 0
max_target_number = 1

for x in numbers:
    temp_target_number = x
    temp_length = 0
    while temp_target_number != 1:
        if temp_target_number % 2 == 0:
            temp_target_number = temp_target_number / 2
        else:
            temp_target_number = temp_target_number * 3 + 1
        temp_length = temp_length + 1
    
    if temp_length > max_length:
        max_length = temp_length
        max_target_number = x

print(max_target_number, max_length)
    
