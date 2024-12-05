import re


def main(filepath):
    with open(filepath, "r") as input_file:
        a_string = input_file.read()
        temp_list = re.split("don\'t\(\)", a_string)
        new_list = []
        new_list.append(temp_list[0])
        for i in range(1, len(temp_list)-1):
            do_index = temp_list[i].find("do()")
            if do_index != -1:
                new_list.append(temp_list[i][do_index:])
        print(new_list)



main("day 3 sample input 3.txt")
