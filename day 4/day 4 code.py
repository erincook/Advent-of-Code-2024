def count_solutions(list_of_strings):           # takes a list of strings and returns the total count of XMAS and SAMX
    XMAS_count = 0
    SAMX_count = 0
    for a_string in list_of_strings:            # iterates through each string in the list
        XMAS_count += a_string.count("XMAS")    # counts "XMAS"
        SAMX_count += a_string.count("SAMX")    # counts "SAMX"
    return XMAS_count + SAMX_count              # returns the total of both


def make_vert_strings(list_of_strings):         # generates the vertical strings, starting at top left
    vert_strings_list = []
    for i in range(len(list_of_strings[0])):    # for each position in the horizontal string (each pos of the matrix)
        new_item = ""                           # initialize the element to be added
        for j in range(len(list_of_strings)):   # iterate through all the lines
            new_item += list_of_strings[j][i]   # append the letter found on each line to the new element
        vert_strings_list.append(new_item)      # at the bottom of the matrix, add that vertical string to the list
    return vert_strings_list                    # return the list


def make_TL_to_BR_strings(list_of_strings):
    TL_BR_strings_list = []

    for i in range(len(list_of_strings[0])-1, -1, -1):  # horizontal position starting at far right and working backward
        new_item = ""                                   # initialize element to be added
        j = 0                                           # set initial row value
        while i < len(list_of_strings[0]) and j < len(list_of_strings):     # we don't want to go past the end of a row
            new_item += (list_of_strings[j][i])         # append the current character to the new string
            j += 1                                      # increase the row and the column number and keep building
            i += 1                                      # the string
        TL_BR_strings_list.append(new_item)             # the list now has all the diag's from across the top row

    for j in range(1, len(list_of_strings)):
        new_item = ""

#def count_BL_to_TR_diag_solutions(a_string):




def main(filename):
    with open(filename, "r") as input_file:
        lines = [line.strip() for line in input_file]
        print(lines)
        horiz_count = count_solutions(lines)
        print(horiz_count)
        vert_count = count_solutions(make_vert_strings(lines))
        print(make_vert_strings(lines))
        print(vert_count)
        make_TL_to_BR_strings(lines)



if __name__ == "__main__":
    main("day 4 sample input 1.txt")