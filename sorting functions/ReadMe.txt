The program sorts a list of values in ascending or descending arrangement. 
A selection sort algorithm is used. In the case of ascending order
arrangement, the process is accomplished by finding the minimum value in
the given list and moving it to the start of the list.

The process is then repeated for the values in the unsorted part of the list.

You can include the module as part of your project by writing the following code
somewhere in your modules:

import os

def include(filename):
	# Load the module if it exists in the directory.
	if os.path.exists(filename):
		exec(filename)

include('sort_my_list.py') # using a relative or absolute path.
from 'sort_my_lis.py' import *
