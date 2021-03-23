no_list = [1000,2,3,4,100,1000]

def maximum(no_list):
#complete the function to return the highest number in the list
    maxNum = 0
    for i in no_list:
        if maxNum <= i:
            maxNum = i
    return maxNum  

print(maximum(no_list))