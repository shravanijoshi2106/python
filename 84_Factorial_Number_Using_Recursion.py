def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input a number
num = int(input("Enter a number: "))

# Call the recursive function
result = factorial(num)

print("Factorial of", num, "is:", result)