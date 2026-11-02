def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if check_prime(n):
    print(n, "is a Prime Number")
else:
    print(n, "is not a Prime Number")