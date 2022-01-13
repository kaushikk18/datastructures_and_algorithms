def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index+1
        else:
            right_index = mid_index-1

    return -1


if __name__ == '__main__':
    number_list = [4, 6, 26, 67, 90, 109]
    number_to_find = 67
    index = binary_search(number_list, number_to_find)
    print('The number is found at the index {} by doing binary search'.format(index))
