# Bubble Sort -> it first compares and then sorts adjacent elements if they are not in the specified order
# moves the highest value towards the right

def bubble_sort(elements):
    size = len(elements)

    # without this j loop the sorting will be done only for the biggest element
    for j in range(size-1):
        swapped = False
        # for i in range(size - 1 - j): (also works)
        # for reducing the time by some milliseconds we can avoid looping through the end by avoiding the already sorted elements
        # so we minus j which is the number of times the loop has run to sort the final j elements
        for i in range(size - 1):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        # if the array is already sorted then only one loop will occur and the loop will break. thus saving time
        if not swapped:
            break


if __name__ == '__main__':
    elements = [4, 1, 78, 45, 99, 69, 23, 65]
    bubble_sort(elements)
    print(elements)
