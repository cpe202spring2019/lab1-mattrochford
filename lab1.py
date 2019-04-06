
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


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass


def main():

   pass

if __name__ == "__main__":
    main()