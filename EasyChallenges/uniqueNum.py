no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
#complete the function's body to return the unique list of numbers
    # unique = 0  
    l.sort()
    unique = set(l)
    return unique        

print(unique_list(no_list))