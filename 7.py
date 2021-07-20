# Write a program that prints a multiplication table for numbers up to 12.

def multiplication_table_up_to_n():
    n = int(input("Enter a number n: "))
    for i in range(1, n+1):
        for q in range(1, 11):
            print(f"{i} * {q} = {i*q}")
        print()
    return


multiplication_table_up_to_n()
