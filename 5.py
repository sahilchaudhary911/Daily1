# Modify the previous program such that only multiples of three or five are considered in the sum.
# e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

def sum_of_n_num_and_multiple_of_3_and_5():
    n_number = int(input("Enter a number n: "))
    sum_n = 0
    for i in range(n_number + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_n += i
    print(f"The sum of natural numbers till {n_number} which is also the multiple of 3 or 5 is {sum_n}")


sum_of_n_num_and_multiple_of_3_and_5()
