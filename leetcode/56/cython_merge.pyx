def solution2(intervals):
    """
    instead of keep the interval pool, we can use a pointer prev to reach our goal
    faster than 98% python solution
    """
    def is_overlapped(left, right):
        overlapped = left[1] - right[0]
        return overlapped >= 0

    result = []
    prev = None

    intervals.sort(key=lambda x: x[0])  # this can be faster with itemgetter
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
