#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:39:12 2017

@author: xuelin
"""

import os
from ReadData import readRawData
import torch
import pandas

cwd = os.getcwd()
fileList = readRawData(cwd + '/00-Raw-Data/')

df = pandas.read_excel(cwd + '/00-Raw-Data/' + str(fileList[0]))
x = df['version'].values
y = df['Clustering_Coefficient'].values;

print(x)
print(y)
#print(fileList)