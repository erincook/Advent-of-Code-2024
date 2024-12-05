def day_2_part_1(filename):
    with open(filename, "r") as input_file:
        reports = [lines.strip().split() for lines in input_file]   # read the lines in, cut out the white space

        for i in range(len(reports)):                   # remaking the list with all the numbers cast as integers
            for j in range(len(reports[i])):            # I'm sure there's a better way to do this!
                reports[i][j] = int(reports[i][j])

        safety_dict = {}                                # initialize a dictionary
        for i in range(len(reports)):                   # for each report
            safe = is_safe(reports[i])                  # send reports[i] to "is_safe", which will return True or False
            if not safe:                                # for part 2
                safe = part_2(reports[i])               # if not safe, tries again with part 2 - remove up to 1 item
            safety_dict[i+1] = safe                     # whatever the final verdict of safety is, add it to the dict

        print(safety_dict)                            # print statement for troubleshooting!

        safe_count = 0                                  # count up the number of safe entries in the dict
        for key, value in safety_dict.items():
            if value:
                safe_count += 1

        input_file.close()
        return safe_count                               # return the count


def part_2(report):                                     # a report gets sent here if it's not "safe" as-is
    working_dict = {}                                   # using a dictionary
    for i in range(len(report)):                        # for every item in the list
        working_dict[i] = []                            # make an entry in the dictionary
        for j in range(len(report)):
            if j != i:                                  # where the value is the same list but with that index missing
                working_dict[i].append(report[j])       # (every possible n-1 sub-list)

    for partial_report in working_dict.values():        # iterate through the dictionary
        safe = is_safe(partial_report)                  # and check every sub-list
        if safe:
            return True                                 # return True if safe, False if unsafe
    return False


def is_safe(report):
    if report[1] > report[0]:                      # first, find out if this is an increasing or decreasing report
        increasing = True                           # (just from the first two elements)
    elif report[1] < report[0]:
        increasing = False
    else:
        return False                                # if first two terms are equal, already unsafe

    if increasing:                                  # if the first two are increasing, check the rest for increasing
        for i in range(len(report)-1):              # as well as the appropriate distancing
            if report[i+1] - report[i] < 1 or report[i+1] - report[i] > 3:
                return False                        # False if unsafe

    if not increasing:                              # if the first two are decreasing, check the rest for decreasing
        for i in range(len(report)-1):              # as well as the appropriate distancing
            if report[i] - report[i+1] < 1 or report[i] - report[i+1] > 3:
                return False                        # False if unsafe

    return True                                     # True if make it all the way through the loop without returning F


print(day_2_part_1("kyle day 2 input.txt"))
