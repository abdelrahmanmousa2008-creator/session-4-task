def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("is your number prime? Enter your number: "))
print(isprime(n))

