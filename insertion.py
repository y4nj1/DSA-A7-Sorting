def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
        print('Array:', array)


data = [62, 28, 41, 15, 12, 89, 78, 51, 35, 83]
print('Array:', data)
insertionSort(data)
print('Array:', data)
