"""This module consists of sorting functions for lists with different
    values."""

from argparse import ArgumentError

def sort_dictionaries(dictionaries, key, arrangement = 'ascending'):
    """Sorts a list of dictionaries using their key-value."""
    
    temporary = {} # A variable for storing a dictionary 
                # temporarily while rearanging them in the list.
    
    if arrangement == 'ascending':
        # Sort the list in ascending order.
        # Find the dictionary with the minimum value and move it to the start
        # of the list.
        for i in range(len(dictionaries)):
            for j in range(i+1, len(dictionaries)):
                if dictionaries[i][key] > dictionaries[j][key]:
                    temporary = dictionaries[i]
                    dictionaries[i] = dictionaries[j]
                    dictionaries[j] = temporary
        return dictionaries

    elif arrangement == 'descending':        
        # Sort the list in descending order.
        # Find the dictionary with the maximum value and move it to the start
        # of the list.
        for i in range(len(dictionaries)):
            for j in range(i+1, len(dictionaries)):
                if dictionaries[i][key] < dictionaries[j][key]:
                        temporary = dictionaries[i]
                        dictionaries[i] = dictionaries[j]
                        dictionaries[j] = temporary
        return dictionaries
    
    else:
        raise ArgumentError("Please specify between 'ascending' or 'descending' arrangement.")

def sort_numbers(input_list, arrangement = 'ascending'):
    """Arranges a list of numbers in a specified order."""

    temporary = 0 # A variable to temporarily store the value being moved.

    if arrangement == 'ascending':    
        for idx in range(len(input_list)): # Find the first value in the list,
            for j in range(idx+1, len(input_list)): # and compare it to the rest
                                                    # of the list.
                if input_list[idx] > input_list[j]:
                    temporary = input_list[idx]
                    input_list[idx] = input_list[j]
                    input_list[j] = temporary
        return input_list

    elif arrangement == 'descending':
        for idx in range(len(input_list)): # Find the first value in the list,
            for j in range(idx+1, len(input_list)): # and compare it to the rest
                                                    # of the list.
                if input_list[idx] < input_list[j]:
                    temporary = input_list[idx]
                    input_list[idx] = input_list[j]
                    input_list[j] = temporary
        return input_list

    else:
        raise ArgumentError("Please specify between 'ascending' or 'descending' arrangement.")
