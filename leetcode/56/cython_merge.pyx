from operator import itemgetter

cpdef list solution2(list intervals):
    result = []
    prev = None

    intervals.sort(key=itemgetter(0))  # this can be faster with itemgetter
    for interval in intervals:
        if prev is None:
            prev = interval
            result.append(prev)
        else:
            # overlapped
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                prev = interval
                result.append(prev)
    return result
