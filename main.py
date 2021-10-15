# Amber Harding
# CSCI 261 Assign 3


def imperativeSearch(array, value):
    i = len(array) - 1
    while i >= 0:
        if i == 0:
            return False            # Array has been exhausted and value not found
        if array[i] == value:
            return True
        i -= 1                      # If value not found decrement counter


def sortedHasSum(s, x):
    l = 0
    r = len(s)-1
    while l <= r:
        sum = s[l] + s[r]
        if sum == x:
            return True
        elif sum < x:
            l += 1
        else:
            r -= 1

    return False


def hasSum(s, x):
    quickSort(s)
    return sortedHasSum(s, x)


def quickSort(s):
    elements = len(s)

    # Base case
    if elements < 2:
        return s

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):
        if s[i] <= s[0]:
            current_position += 1
            temp = s[i]
            s[i] = s[current_position]
            s[current_position] = temp

    temp = s[0]
    s[0] = s[current_position]
    s[current_position] = temp

    left = quickSort(s[0:current_position])
    right = quickSort(s[current_position + 1:elements])

    arr = left + [s[current_position]] + right  # Merge array back together

    return arr


if __name__ == '__main__':
    a = [3, 4, 5, 1, 2]
    s = [1, 2, 3, 4, 5]

    print(imperativeSearch(a, 5))
    print(sortedHasSum(s, 16))
    print(hasSum(a, 5))