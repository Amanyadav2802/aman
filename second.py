
def prime_number(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return prime_number(n, i + 1)
if prime_number(n):
    print( n, "is a Prime number ")
else:
    print( n, "is not a Prime number")
    prime_number(8)
n = int(input("Enter your number"))








