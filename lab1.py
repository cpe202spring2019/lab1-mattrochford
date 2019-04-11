
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if None == int_list: # Check for None list
        raise ValueError('List contains None element')

    elif not int_list: # Check for empty list
        return(None)

    else: # Find max value
        max_int = int_list[0] # Initialize first value as max
        for i in int_list:
            if i > max_int: # Check for new max
                max_int = i # Update max

    return(max_int)

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if None == int_list: # Check for None list
        raise ValueError('List contains None element')   

    elif not int_list: # Check for empty list
        return([])

    else:
        return [int_list[-1]] + reverse_rec(int_list[:-1]) # Add last element and call function again
    



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """

    
    if int_list == None:
        raise ValueError('List contains None element')  
    else:
        for i in int_list:
            if i == None: # Check for None list
                raise ValueError('List contains None element')   

    middle = (high+low)//2 # Find middle index

    if (high-low)//2 == 0: # Check if list only has one number left
        if target == int_list[high]:
            return high
        if target != int_list[middle]: # If last number doesnt match return None
            return None

    if target == int_list[middle]: # If target matches middle number
        return middle
    elif target > int_list[middle]: # If target is less than middle number
        return bin_search(target,middle,high,int_list) # Recursive function call
    else: # If target is greater than middle number
        return bin_search(target,low,middle,int_list) # Recursive function call