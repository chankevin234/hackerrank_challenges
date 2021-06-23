def minMaxSum(arr):
    sumInts = 0; 
    minNum = 0;
    maxNum = 0;
    myArray = arr;
    arrayLength = len(myArray)

    for i in range(arrayLength):
        for y in range(arrayLength):
            sumInts += myArray[y];
            minNum = sumInts;            
                
        sumInts = sumInts - myArray[i];
        if(sumInts > maxNum):
            maxNum = sumInts;

       
        if(sumInts < minNum):
            minNum = sumInts;      
                    
        sumInts = 0;
                
    print("{} {}".format(minNum, maxNum))
 
 # more efficient solution
 def miniMaxSum(arr):
    arr.sort()
    total = 0
    max = arr[len(arr) - 1]
    min = arr[0]
    
    for i in arr:
        total += i
    print(total - max, total - min)