# Program to check whether a number is prime or not

num = int(input("Enter a number: "))

# Numbers less than or equal to 1 are not prime
if num <= 1:
    print("Not a prime number")
else:
    # Check divisibility from 2 to num - 1
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
