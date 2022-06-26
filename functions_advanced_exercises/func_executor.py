def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):  # priema tuples  (sum_numbers, (1, 2)), (multiply_numbers, (2, 4))
    result_list = []
    for i in range(len(args)):  # obhojdame vseki tuple
        current_tuple = args[i]
        function = current_tuple[0]
        nums_tuple = current_tuple[1]  # unpacking tuple
        result_list.append(function(*nums_tuple))
    return result_list


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
