# goals for today: use more functions; do the "if __name__ == __main__" thing even though i don't understand it yet

import re


def find_valid_strings(a_string):
    valid_string_list = re.findall("mul\([0-9]+,[0-9]+\)", a_string)
    # print("Here are all the valid mul strings: ", valid_string_list)
    return valid_string_list


def find_total_product(mul_list):
    total_product = 0
    for mul_string in mul_list:
        temp = map(int, re.findall("[0-9]+", mul_string))
        temp_list = list(temp)
        # print(temp_list)
        total_product += temp_list[0] * temp_list[1]
    return total_product


def find_do_substrings(a_string):
    temp_list = re.split("don\'t\(\)", a_string)
    new_list = [temp_list[0]]
    for i in range(1, len(temp_list) - 1):
        do_index = temp_list[i].find("do()")
        if do_index != -1:
            new_list.append(temp_list[i][do_index:])

    return new_list


def main(filepath):
    with open(filepath, "r") as input_file:
        a_string = input_file.read()
        input_file.close()

        # Part 1
        mul_list = find_valid_strings(a_string)
        total_product = find_total_product(mul_list)
        print("The total product is ", total_product)

        # Part 2
        do_substrings = find_do_substrings(a_string)
        do_product = 0
        for substring in do_substrings:
            mul_list = find_valid_strings(substring)
            total_product = find_total_product(mul_list)
            do_product += total_product
        print("The modified product is ", do_product)


main("day 3 input.txt")


# if __name__ == "__main__":
#     main("C:\Users\erinc\PycharmProjects\Advent of Code 2024\day 3\day 3 sample input 1.txt")

# OK well that didn't work, gave this error:
#   File "C:\Users\erinc\PycharmProjects\Advent of Code 2024\day 3\day 3 code.py", line 23
#     main("C:\Users\erinc\PycharmProjects\Advent of Code 2024\day 3\day 3 sample input 1.txt")
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
