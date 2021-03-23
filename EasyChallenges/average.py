no_list = [22,68,90,78,90,88]

def average(x):
#complete the function's body to return the average
    sum = 0
    length = len(x)
    for i in x:
        sum += i
    average = sum / length
    return average
    
average = average(no_list)
print(average)