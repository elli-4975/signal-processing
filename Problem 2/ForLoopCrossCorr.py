# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:53:40 2021

File name: ForLoopCrossCorr.py
Author: You!
Date: 2/23/2023

Use this function to develop the for loop cross correlation. Only adjust
code within the "TODO" brackets to ensure that this code will still work
with the main script.

@author: Calvin
"""

import numpy as np

def ForLoopCrossCorr(ecg_data, heartbeat):
    
    # The outer for loop is written for you as it cycles through the ecg data
    samples = ecg_data.shape[0];
    heartbeat_samples = heartbeat.shape[0];
    
    cross_data = np.zeros( [(samples - heartbeat_samples), 1] );
    for i in range( samples - heartbeat_samples ):
        
        #######################################################################
        # 2.6 - TODO
        #######################################################################
        # IMPLEMENT THE FOR LOOP CROSS CORRELATION HERE.

        cross_correlation = 0;
        
        for j in range(heartbeat_samples):
            cross_correlation += ecg_data[i+j] * heartbeat[j]
    
        
        #######################################################################
        # 2.6 - END TODO
        #######################################################################
        
        cross_data[i] = cross_correlation;
        
    return cross_data