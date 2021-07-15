# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

def sum_of_n_numbers():
    n_number = int(input("Enter a number n: "))
    sum_n = 0
    for i in range(n_number + 1):
        sum_n += i
    print(f"The sum of natural numbers till {n_number} is {sum_n}")


sum_of_n_numbers()
