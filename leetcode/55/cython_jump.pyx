# distutils: language = c++
from libcpp.vector cimport vector
from libcpp cimport bool

cpdef bool solution3(vector[int] vect):
    """
    As google for some solution found that the critical point for this question is that:
    `don't concern the route path too much`
    you only need to care if the next step can jump farthest.

    this solution only better than 85% solutions,
    as check most fast solution were count down from the end of array.
    """
    # cdef vector[int] vect = nums

    if vect.size() <= 1:
        return True

    cdef int reach = vect.front()
    cdef int n_nums = vect.size()

    for idx in range(n_nums):
        if idx > reach:  # the farthest position is reach
            break
        if reach >= n_nums - 1:  # already reach the end of list
            break

        reach = max(idx + vect[idx], reach)
    return reach >= n_nums - 1

