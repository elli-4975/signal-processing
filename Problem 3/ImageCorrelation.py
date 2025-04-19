# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:51:05 2021

File name: ImageCorrelation.py
Author: You!
Date: 1/24/2021

Use this function to develop the for loop cross correlation. Only adjust
code within the "TODO" brackets to ensure that this code will still work
with the main script.

@author: Calvin
"""

import numpy as np

def ImageCorrelation( template, image ):

    # Book-keeping - To do this type of image correlation, it is common to
    # first subtract the mean value from the template.
    template = template / 255.
    template = template - np.mean( template );
    image = image / 255.

    corr_matrix = np.zeros( [image.shape[0], image.shape[1]] );

    ###########################################################################
    # 3.3 - TODO
    ###########################################################################
    # Implement your 2-D image cross correlation here. You'll need to
    # implement the outer for loops that let you extract sections of Sthe
    # larger "image" to cross correlate against the "template". Use the
    # equivalent code in problem 2 for inspiration on how to set this up.
    # You are welcome to use any method you like to perform this cross
    # correlation. Use the variable corr_matrix to store the correlation
    # values
    img_width = image.shape[1]
    img_height = image.shape[0]
    template_width = template.shape[1]
    template_height = template.shape[0]
    
    test_section = np.zeros( [template.shape[0], template.shape[1]] )
    for i in range( img_height - template_height):
        for j in range ( img_width - template_width):
            test_section = image[i:i+template_height,j:j+template_width]
            correlation = np.sum(test_section * template)
            corr_matrix[i,j]=correlation
    
    return corr_matrix