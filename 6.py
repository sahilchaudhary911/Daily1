"""
Write a program that asks the user for a number n and gives them the possibility
to choose between computing the sum and computing the product of 1,…,n.
"""


def computing_sum_or_product_of_n_nums():
    n_number = int(input("Enter a number n of natural number: "))
    yes_or_no = input(f"Press '0' to add natural numbers till {n_number} or '1' in case if you want their product: ")
    if yes_or_no == "0":
        sum_of_n = 0
        for i in range(n_number + 1):
            sum_of_n += i
        print(f"The sum of n natural number till {n_number} is {sum_of_n}")
    else:
        product_of_n = 1
        for i in range(1, n_number + 1):
            product_of_n *= i
        print(f"The product of n natural number till {n_number} is {product_of_n}")


computing_sum_or_product_of_n_nums()
