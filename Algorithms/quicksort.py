# prefered over other sorting algorithms
# uses a pivot to sort the array
# if the numbers are lesser than the pivot then the numbers are pushed to the items_lesser array
# if the numbers are greater than the pivot then the numbers are pushed to the items_greater array
# here we use the last element of the array as the pivot

def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    items_lesser = []
    items_greater = []

    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lesser.append(item)

    return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)


print(quick_sort(['23', '15', '1', '89', '69', '0', '19']))
