def plusMinus(arr):
    # Write your code here
    arrLength = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in range(arrLength):
        if(arr[i] > 0):
            pos += 1;
            # print("I'm Pos");
        elif(arr[i] < 0):
            neg += 1;
            # print("I'm Neg");
        else:
            zero += 1;
            # print("I'm Zero");
            
    print(round(pos/arrLength, 6))
    print(round(neg/arrLength, 6))
    print(round(zero/arrLength, 6))