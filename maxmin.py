# given a list of integers, return the highest and lowest numbers in the array without using max and min
# [2, 4, 1, 0, 2, -1] returns [-1, 4]

def min_max_list(numbers):
    # using .sort() method
    # changes the original list
    numbers.sort()
    min_max = [numbers[0], numbers[-1]]

    return min_max


numbers = [2, 4, 1, 0, 2, -1]
# numbers = [20, 50, 12, 6, 14, 8]
# numbers = [100, -100]

print(min_max_list(numbers))
