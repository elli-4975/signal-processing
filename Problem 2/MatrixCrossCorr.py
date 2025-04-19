# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:57:20 2021

File name: MatrixCrossCorr.py
Author: You!
Date: 2/23/2023

Use this function to develop the for loop cross correlation. Only adjust
code within the "TODO" brackets to ensure that this code will still work
with the main script.

@author: Calvin
"""

import numpy as np

def MatrixCrossCorr(ecg_data, heartbeat):
    
    # The outer for loop is written for you as it cycles through the neural
    # data
    samples = ecg_data.shape[0];
    heartbeat_samples = heartbeat.shape[0];
    
    cross_data = np.zeros( [(samples - heartbeat_samples), 1] );
    for i in range( samples - heartbeat_samples ):
        
        #######################################################################
        # 2.7 - TODO
        #######################################################################
        # IMPLEMENT THE MATRIX CROSS CORRELATION HERE.

        cross_correlation = 0;
        cross_correlation = np.dot(ecg_data[i:i+heartbeat_samples], heartbeat)
        
        #######################################################################
        # 2.7 - END TODO
        #######################################################################
        
        cross_data[i] = cross_correlation;
    
    return cross_data