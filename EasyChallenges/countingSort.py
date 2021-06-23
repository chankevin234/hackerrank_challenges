#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    arrayLength = len(arr)
    freq_array = [0] * 100;
    
    for i in range(arrayLength):
        # print(arr[i]);
        current = arr[i];
        print(current);
        # each time you loop through arr, arr[i] is the value at i position
        # for that same position in freq_array, it will add a counter 
        
        freq_array[current] = freq_array[current] + 1;
        
        
    
    return(freq_array);