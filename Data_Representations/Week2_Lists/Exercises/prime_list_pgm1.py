""" Program to print required prime numbers in a list """

def print_prime():
    """
    Function which prints 2nd, 4th and 6th numbers in the list
    """
    prime_list = [2, 3, 5, 7, 11, 13]

    for index in range(1, len(prime_list) + 1, 2):
        print(prime_list[index])

print_prime()
