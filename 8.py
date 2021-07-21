"""
Write a program that prints all prime numbers.
(Note: if your programming language does not support arbitrary size numbers,
printing all primes up to the largest number you can easily represent is fine too.)
"""


def all_prime_no_till_n():
    n = int(input("Enter a number n: "))
    comosite_no = []
    prime_no = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                comosite_no.append(i)
                break
        if i not in comosite_no:
            prime_no.append(i)
    print(f"Prime no's: {prime_no}")
    print(f"Composite no's: {comosite_no}")


all_prime_no_till_n()


