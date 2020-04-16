# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:41:01 2020

@author: hkacker
"""

import os
import pandas
import glob

def concat(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted",
           out="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\concatenate.csv"):
    os.chdir(indir)
    FileList = glob.glob(".csv")
    dfFileList=[]
    columnNames = ["Year","Month","Day","Hour","Temp","DewTemp","Pressure","Windir",
                   "Windspeed","Sky","Precip1","Precip6","ID"]
    for filename in FileList :
        print(filename)
        df = pandas.read_csv(filename , header=None)
        dfFileList.append(df)
    concatdf = pandas.concat(dfFileList, axis=0)
    concatdf.columns = columnNames
    concatdf.to_csv(out, index=None)
        
        
        
    