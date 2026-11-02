def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))

# Call the function
result = factorial(n)

print("Factorial of", n, "is:", result)