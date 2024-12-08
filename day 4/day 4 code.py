def count_xmas_solutions(list_of_strings):      # takes a list of strings and returns the total count of XMAS and SAMX
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


def make_TL_to_BR_strings(list_of_strings):         # generate diagonal strings, top left to bottom right orientation
    TL_BR_strings_list = []

    for i in range(len(list_of_strings[0])-1, -1, -1):  # horizontal position starting at far right and working backward
        new_item = ""                                   # initialize element to be added
        j = 0                                           # set initial row value
        while i < len(list_of_strings[0]) and j < len(list_of_strings):     # we don't want to go past the end of a row
            new_item += (list_of_strings[j][i])         # append the current character to the new string
            j += 1                                      # increase the row and the column number and keep building
            i += 1                                      # the string
        TL_BR_strings_list.append(new_item)             # the list now has all the diag's from across the top row

    for j in range(1, len(list_of_strings)):            # starting in the second row
        new_item = ""                                   # initialize element to be added
        i = 0                                           # this time set initial COLUMN value
        while j < len(list_of_strings) and i < len(list_of_strings[0]):     # again, not going beyond bottom or right
            new_item += (list_of_strings[j][i])         # append the current character to the new string
            j += 1                                      # increase the row and column number and keep building
            i += 1                                      # the string
        TL_BR_strings_list.append(new_item)             # the list now has all the diag's from left to right going down
                                                        # the left side of the word search.
    return TL_BR_strings_list                           # return the full list of diag strings


def make_BL_to_TR_strings(list_of_strings):         # generate diagonal strings, bottom left to top right orientation
    BL_TR_strings_list = []

    for j in range(len(list_of_strings)):               # starting at top left and working down the word search
        new_item = ""                                   # initialize item to be added
        i = 0                                           # set initial column value
        while j >= 0 and i < len(list_of_strings[0]):   # keep j and i within the bounds of the puzzle
            new_item += (list_of_strings[j][i])         # add the current character to the new string
            j -= 1                                      # decrease the j value (move "up" in the puzzle)
            i += 1                                      # increase the i value (move "right" in the puzzle)
        BL_TR_strings_list.append(new_item)             # append the new item once we reach the edge of the puzzle

    for i in range(1, len(list_of_strings[0])):         # now working across the bottom of the word search
        new_item = ""                                   # initialize item to be added
        j = len(list_of_strings)-1                      # set initial row value (bottom row)
        while j >= 0 and i < len(list_of_strings[0]):   # keep i and j inside the puzzle
            new_item += (list_of_strings[j][i])         # add the current character to the new string
            j -= 1                                      # move up and to the right in the puzzle
            i += 1
        BL_TR_strings_list.append(new_item)             # append the new item once the edge is reached

    return BL_TR_strings_list                           # return the list of diag strings


# Part 2 code. Thought I could reuse some of the above, decided against it.
# The goal is to look at 3x3 windows (without going off the edge of the board)
def find_X_MAS(list_of_strings):
    X_MAS_count = 0
    A_count = 0
    for j in range(len(list_of_strings)-2):             # from top to 3 from the bottom
        for i in range(len(list_of_strings[0])-2):      # from left to 3 from the right
            if list_of_strings[j+1][i+1] == 'A':        # check whether the middle character is "A"
                # check for the M-A-S/S-A-M cross pattern
                if (list_of_strings[j][i] == "M" and list_of_strings[j + 2][i + 2] == "S") or (
                        list_of_strings[j][i] == "S" and list_of_strings[j+2][i+2] == "M"):
                    if (list_of_strings[j][i+2] == "M" and list_of_strings[j + 2][i] == "S") or (
                            list_of_strings[j][i+2] == "S" and list_of_strings[j + 2][i] == "M"):
                        X_MAS_count += 1
    return X_MAS_count                                  # return the total count of cross pattern MAS/SAM


def main(filename):
    with open(filename, "r") as input_file:
        lines = [line.strip() for line in input_file]

        # PART 1
        # horiz count requires no parsing, just count solutions in the strings as they've been brought in
        horiz_count = count_xmas_solutions(lines)
        # vert count --> make vert strings, count solutions
        vert_strings = make_vert_strings(lines)
        vert_count = count_xmas_solutions(vert_strings)
        # TL_BR_count --> make diag strings, count solutions
        TL_to_BR_strings = make_TL_to_BR_strings(lines)
        TL_BR_count = count_xmas_solutions(TL_to_BR_strings)
        # TL_BR_count --> make diag strings, count solutions
        BL_to_TR_strings = make_BL_to_TR_strings(lines)
        BL_TR_count = count_xmas_solutions(BL_to_TR_strings)
        # total count --> add the four counts together
        total_count = horiz_count + vert_count + TL_BR_count + BL_TR_count
        # print the final count and close the file
        print("Total 'XMAS' count is", total_count)
        input_file.close()

        # PART 2
        X_MAS_count = find_X_MAS(lines)
        print("Total 'X-MAS' count is", X_MAS_count)


if __name__ == "__main__":
    main("day 4 input.txt")
