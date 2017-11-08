"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""

# Plan:
    # Can start and end anywhere, but in progression
    # Find way to not duplicate loops (e.g. look back)
    # Not allowed to re-arrange (sort) lst
    # No duplicates in final output (store in set then convert to lst?)
    # Can return one value if its the highest (no addition)
    # If all empty, return empty lst


def largest_sum(nums):
    """Find subsequence with largest sum."""

    # Before loop, initialize start/end indices for final lst splice output

    # Keep track of best sum
    best_sum = 0
    start_of_best = 0
    end_of_best = -1  # nothing; -1 r/t lst splicing output

    # Track current sum and start traversal
    current_sum = 0
    start_of_curr = 0

    # loop over lst; track idx for storing start/end of sequences
    for i, n in enumerate(nums):

        # First: initialize first item as current_sum
        # Later: build up seq. sum with next item
        current_sum += n

        # if new largest, update best
        if current_sum > best_sum:
            best_sum = current_sum
            start_of_best = start_of_curr  # track first idx
            end_of_best = i  # track last idx

        # reset sequence if sum ever goes below 0
        if current_sum <= 0:
            start_of_curr = i + 1  # re-initialize seq w/ next item
            current_sum = 0

    # return seq with best sum via lst splicing
    return nums[start_of_best:end_of_best + 1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n"
