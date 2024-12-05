def day_1(filename):
    with open(filename, "r") as input_file:
        lines_raw = [lines.strip().split() for lines in input_file]     # read in the lines as a white-space sep list
        list_1 = []                                                     # initialize list 1 and list 2
        list_2 = []
        for line in lines_raw:                                          # populate list 1 and list 2
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))
        list_1.sort()                                                   # sort the lists
        list_2.sort()
        # print(lines_raw)                                              # some print statements for testing
        # print(list_1)
        # print(list_2)
        # print(list_1)
        # print(list_2)

        # Part 1
        # total = 0                                                       # initialize a running total
        # for i in range(len(list_1)):                                    # go through the lists
        #     total += abs(list_1[i] - list_2[i])                         # and sum up the distances of each element

        # print(total)                                                    # print the total (Part 1)

        # Part 2
        total_similarity = 0                                              # initialize total_similarity for P2
        for num in list_1:                                                # for each number in list_1
            count_list2 = list_2.count(num)                               # count how many times it appears in list_2
            total_similarity += num * count_list2                         # add the number*list_2 count to running total

        input_file.close()
        return total_similarity

print(day_1("day 1 input .txt"))






