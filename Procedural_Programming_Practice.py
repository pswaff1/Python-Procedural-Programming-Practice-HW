# Procedural_Programming_Practice.cs
# 
# This script defines four functions, "filter", "explode", "implode" and "tribble" as well as a 
# main function which calls these functions based on user input passed through command line 
# arguments. The filter function takes in a predicate and a list of integers as input, and returns 
# a new list of integers that match the predicate. The explode function takes a list of strings 
# and returns a list of each character in the input strings, space separated. The implode function 
# takes a list of strings and returns a single concatenated string. The tribble function takes in 
# a number as input and returns a mathematical calculation based on it, and the main function 
# controls the flow of the program and calls the other functions based on the command line 
# arguments passed.
# 
# NCU.edu
# School of Business & Technology Management
# TIM-6110
# 
# Author: Patrick Swafford
# Date: 05 January 2023

import sys as system # renegade for life

def filter(predicate, args):

    # Initialize an empty list to store filtered integers
    mylist = []

    # Iterate over each argument
    if predicate == "odd":
        for arg in args:
            try:
                # Check if the argument is an odd integer
                if int(arg) % 2 == 1:
                    # Append the argument to the filtered list
                    mylist.append(arg)
            except ValueError:
                # Return an error message if the argument is not an integer
                return "Invalid input! Integers only"   

    # Check if predicate is "even"
    elif predicate == "even":
        # Iterate over each argument
        for arg in args:
            try:
                # Check if the argument is an even integer
                if int(arg) % 2 == 0:
                    # Append the argument to the filtered list
                    mylist.append(arg)
            except ValueError:
                # Return an error message if the argument is not an integer
                return "Invalid input! Integers only"          
    
    # Return an error message if the predicate is not "odd" or "even"
    else:
        return "Invalid filter command. Please try again"

    # Return the filtered list
    return mylist

def explode(args):

    # Initialize an empty list to store the exploded string
    exploded_string = []

    # Iterate over each argument
    for arg in args:

        # Iterate over each character in the argument
        for ch in arg:

            # Append the character to the exploded string
            exploded_string.append(ch)
        
        # Append a space to separate the characters from different arguments        
        exploded_string.append(" ")

    # Remove the last space from the exploded string
    return exploded_string[:-1]

def implode(args):

    # Initialize an empty string
    mystring = ""

    # Iterate over each argument
    for arg in args:

        # Iterate over each character in the argument
        for ch in arg:
            # Append the character to the imploded string
            mystring = mystring + str(ch)

    # Return the imploded string
    return mystring

def tribble(arg):

    # Try to convert the argument to an integer
    try:
        # Convert the input to int
        arg = int(arg)

        # Check if input is less than or equal to zero
        if arg <= 0:
            return 0

        # Return 11 to the power of arg // 12
        return 11 ** (int(arg) // 12)

    except ValueError:
        # Return an error message if input cannot be converted to an int
        return "Invalid input!"

def main():
    # If less than 2 CLI arguments, exit the program with an error message
    if len(system.argv) < 2:
        print("Invalid input! Please specify which function you need.")
        return -1
    
    # Check the first argument, which should specify the desired function
    # If the first argument is 'filter', proceed to filter function
    if system.argv[1] == "filter" :
        # Check for the presence of a second argument
        if len(system.argv) < 3:
            print ("Invalid input! Please pass an input list")
            return -1
        print (filter (system.argv[2], system.argv[3:]))

    # If the first argument is 'explode', proceed to explode function
    elif system.argv[1] == "explode":
        # Check for the presence of a second argument
        if len(system.argv) < 3:
            print("Invalid input! Please pass an input string")
            return -1
        print(explode(system.argv[2:]))

    # If the first argument is 'implode', proceed to implode function
    elif system.argv[1] == "implode":
        # Check for the presence of a second argument
        if len(system.argv) < 3:
            print("Invalid input! Please pass an input list")
            return -1
        print(implode(system.argv[2:]))

    # If the first argument is 'tribble', proceed to tribble function
    elif system.argv[1] == "tribble":
        if len(system.argv) < 3:
            # Check for the presence of a second argument
            print("Invalid input. Please enter the hours tribble'd!")
            return -1
        print ("Hours spent = " + str(system.argv[2]))
        print ("Tribble count: " + str(tribble(system.argv[2])))
    
    # If the first argument is anything else, print an error message
    else:
        print ("Command not found. Please Try Again")
        return -1

    # Return with zero exit code
    return 0

if __name__ == "__main__":
    main()