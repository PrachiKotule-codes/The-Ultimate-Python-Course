# Program to check whether a number is prime or not

num = int(input("Enter a number: "))

# Numbers less than or equal to 1 are not prime
if num <= 1:
    print("The number is not prime")
else:
    # Check whether the number has any divisor
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
