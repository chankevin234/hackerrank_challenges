no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
#complete the function's body to return the unique list of numbers
    # # unique = 0 
    # Method 1: 
    # l.sort()
    # unique = set(l)
    # return unique

    unique_list = []

    for x in l:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()          
    return unique_list

print(unique_list(no_list))