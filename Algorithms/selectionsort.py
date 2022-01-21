# selection sort -> sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning

def selection_sort(elements):
    size = len(elements)
    for i in range(size):
        min_index = i  # we are initially assuming the first index to be the minimum index
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j
        # if the minimum index is not the same after looping, we swap the values of the i position with the new minimum value
        # that is the minimum value will be pushed to the starting in the first loop and the process continues
        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]


if __name__ == '__main__':
    elements = [54, 12, 8, 22, 69, 90, 47, 109]
    selection_sort(elements)
    print(elements)
