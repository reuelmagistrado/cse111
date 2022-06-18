"""
1. Create a list of numbers
2. Append more numbers onto the list
3. Print the list
"""

import random

def main():
    # create numbers list
    numbers = [16.2, 75.1, 52.3]
    # print numbers list
    print(numbers)
    # call append_random_numbers(x) with one argument
    append_random_numbers(numbers)
    # print numbers list
    print(numbers)
    # call append_random_numbers(x, y) with two argument
    append_random_numbers(numbers, 3)
    # print numbers list
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    """
    Parameters
        numbers_list: list of floating point numbers
        quantity: 
            number of words to be added in the numbers_list
            has a default value of 1
    Return: none
    """
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100),1)
        numbers_list.append(random_number)


if __name__ == "__main__":
    main()
