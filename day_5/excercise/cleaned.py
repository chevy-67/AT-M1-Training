array = [5, 2, 9, 1, 7]
sorted_array = sorted(array)

def bubble_sort(array: list[int]) -> list[int]:

    """
        Sort the given array in ascending using bubble sort
        Input:
            array of unsorted elements in int type
        Output:
            array of elements sorted in ascending order 
    """

    array_length = len(array)

    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                # Swap
                array[j], array[j + 1] = array[j + 1], array[j]

def test_bubble_sort():
    bubble_sort(array)
    assert array == sorted_array
