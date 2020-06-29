

def slice_array(arr, length):
    low, high = 0, length
    while low < len(arr):
        yield arr[low:high]
        low += length
        high += length
