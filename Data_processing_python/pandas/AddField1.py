# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:10:02 2020

@author: hkacker
"""

import os
import pandas
#import glob

def AddField(filename,indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input"):
    os.chdir("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input")
    df = pandas.read_csv(filename)
    df["1984 Euros"] = df["1984"]*0.91
    df["1984 Pounds"] = df["1984"]*0.80
    df.to_csv(filename+"Added_Fields.csv", index=None)