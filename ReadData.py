#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:09:40 2017

@author: xuelin
"""

from os import listdir
from os.path import isfile, join

def readRawData(filePath):
    fileList = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    
    return fileList
    # print(fileList)
    
    