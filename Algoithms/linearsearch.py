def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index

    return -1


if __name__ == '__main__':
    number_list = [2, 3, 4, 9, 19, 38, 99]
    number_to_find = 38
    index = linear_search(number_list, number_to_find)
    print('The number is found at the index {} by using linear search'.format(index))
