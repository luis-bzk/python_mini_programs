from resources import numbers_array


def binary_search(search_list, element):
    middle = 0
    start = 0
    end = len(search_list)
    steps = 0

    while start <= end:
        print('Step', steps, ':', str(search_list[start:end + 1]))
        steps = steps + 1
        middle = (start + end) // 2
        if element == search_list[middle]:
            return middle
        if element < search_list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


binary_search(numbers_array, 195)
