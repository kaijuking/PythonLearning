# Exercise: 'calculator'
# Write a simple calculator that answers questions like:
# 3 + 5, 8 / 2, 4 * 4, 18 - 36

def calculate():

    input_list = []

    x = get_user_input("Please enter intenger #1: ")
    y = get_user_input("Please enter intenger #2: ")

    input_list.append(x)
    input_list.append(y)

    if validate_is_digit(input_list):
        x = int(input_list[0])
        y = int(input_list[1])
        sum_two_numbers(x, y)
        divide_two_numbers(x, y)
        multiply_two_numbers(x, y)
        subtract_two_numbers(x, y)   
    else:
        print("Please input valid integers.")
        calculate()


def validate_is_digit(input_list):
    for i in input_list:
        if i.isdigit():
            return True


def sum_two_numbers(x, y):
    print("{0} + {1} = {2}".format(x, y, x + y))
    return x + y


def divide_two_numbers(x, y):
    print("{0} / {1} = {2}".format(x, y, x / y))
    return x / y


def multiply_two_numbers(x, y):
    print("{0} * {1} = {2}".format(x, y, x * y))
    return x * y


def subtract_two_numbers(x, y):
    print("{0} - {1} = {2}".format(x, y, x - y))
    return x - y


if __name__ == "__main__":
    calculate()