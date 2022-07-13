array = [4,2,5,6,3,5,2,1,4]

def mean(arr):
    """Calculate the mean of the given array
    Args:
    arr(list): the array to calculate the mean

    Returns:
    average: the mean value
    """

    return sum(arr)/len(arr)

def median(arr):
    """Calculate the mean of the given array"""
    
    arr.sort()

    mid_point = len(arr)//2      #floor divison

    if len(arr) % 2 == 0:
        return(arr[mid_point] +arr[mid_point -1] )/2
    else:
        return arr[mid_point]

print(median(array))