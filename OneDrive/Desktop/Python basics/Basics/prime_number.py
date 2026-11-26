# Program to check whether a number is prime or not

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        print("Checking divisor:", i)
