#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        user_number = int(input('Try any on-word numeral: '))
        if user_number % 2 == 0:
            print('EVEN')
        else:
            print('ODD')
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for x in range (0, 100, 10):
        for y in range(1, 11):
            print(x+y, end='\t')
        print()

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    number_list = list()
    while True:
        try:
            user_number = input('Try any number: ')
            if user_number == 'done' and len(number_list) == 0:
                return 0
            elif user_number == 'done':
                average = float(sum(number_list) / len(number_list))
                return average
            else:
                number_list.append(int(user_number))

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")



##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    #even_odd()
    #ten_by_ten()
    print(find_average())
    pass

if __name__ == '__main__':
    main()
