# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:59:16 2020

@author: hkacker
"""

import os
import pandas
import glob

def addField(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted"):
    os.chdir("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted")
    FileList = glob.glob("*")
    for filename in FileList :
        df = pandas.read_csv(filename , sep='\s+', header=None)
        df["Station"]= [filename.rsplit("-",1)[0]]*df.shape[0]
        df.to_csv(filename+".csv", index=None , header=None)
        