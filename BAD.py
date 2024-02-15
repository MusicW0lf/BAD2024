import numpy as np


def find_longest_sequence(array, increasing=True):
    diffs = np.diff(array) < 0 if increasing else np.diff(array) > 0
    indices = np.where(np.concatenate(([True], diffs)))[0]
    lengths = np.diff(np.concatenate((indices, [len(array)])))
    longest_index = np.argmax(lengths)
    start_index = indices[longest_index]
    longest_subseq = array[start_index:start_index + lengths[longest_index]]
    return longest_subseq


with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

np_array = np.array(numbers)
minimum, maximum, mean, median = np.min(np_array), np.max(np_array), np.mean(np_array), np.median(np_array)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
print("Median:", median)
print("Longest sequence of increasing numbers:", find_longest_sequence(np_array))
print("Longest sequence of decreasing numbers:", find_longest_sequence(np_array, False))
