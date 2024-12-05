def is_safe(report):
    if report[1] > report[0]:  # first, find out if this is an increasing or decreasing report
        increasing = True
    elif report[1] < report[0]:
        increasing = False
    else:
        return False  # if first two terms are equal, already unsafe

    if increasing:
        for i in range(len(report) - 1):
            if report[i + 1] - report[i] < 1 or report[i + 1] - report[i] > 3:
                return False

    if not increasing:
        for i in range(len(report) - 1):
            if report[i] - report[i + 1] < 1 or report[i] - report[i + 1] > 3:
                return False

    return True

print(is_safe([92, 94, 97, 98]))