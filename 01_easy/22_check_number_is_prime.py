# Write a program to check if a number is prime

import math

num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")