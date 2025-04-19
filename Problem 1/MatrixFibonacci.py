# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:26:20 2023

File name: MatrixFibonacci.py
Author: You!
Date: 2/23/2023

TUse this script to develop the matrix implementation of the Fibonacci
number equation. Only adjust code within the "TODO" brackets.

@author: Calvin
"""

# Imports - tell python to load in other libraries that will be used
# You should not need to import anything else.
import numpy as np

# The main script
def main():
    
    ##########################################################################
    # 1.2 - TODO
    ##########################################################################
    # IMPLEMENT THE MATRIX VERSION OF FIBONACCI HERE. You just need to fill in
    # the blank on this matrix. Some variables that are provided:
    # n = the Nth fibonacci number that you want to solve for

    n = 40 # Which fibonacci number do you want
    mat_fib = np.linalg.matrix_power(np.array([[1,1],[1,0]]), n-2) # TODO - REPLACE THE RIGHT HAND SIDE WITH YOUR SOLUTION

    fib_base = np.array([[1],[1]]); # First and second fibonacci numbers as a column vector
    
    fib_n = np.matmul(mat_fib, fib_base) # Solve for the nth and n-1th fibonacci numbers

    ##########################################################################
    # 1.2 - END TODO
    ##########################################################################
    print(fib_n[0]) # Print out the nth Fibonacci number


"""
The following code allows us to run this file as a script. Note, this not the
only way to do this, but the benefit of using this method is that all the
variables that are created as part of the script have local scope.
"""
if __name__ == "__main__":
    main()