def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None


sequence_a = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
item_a = int(input('Please enter value you wish to find in thr list : '))


print(f'Element found at position {binary_search(sequence_a, item_a)}')

list1 = [4, 5, 6, 8]
list2 = list1
list2[2] = 89
print(list1)