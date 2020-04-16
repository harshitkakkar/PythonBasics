# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:09:30 2020

@author: hkacker
"""

import pandas
#import os

def merged(left="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\concatenate.csv",
           right="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\Station_info.txt",
          out="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\merged_concat.csv"):
    
    leftdf = pandas.read_csv(left)
    rightdf = pandas.read_fwf(right, converters={"USAF":str , "WBAN":str})
    rightdf["USAF_WBAN"] = rightdf["USAF"]+"-"+rightdf["WBAN"]
    mergedDf= pandas.merge(leftdf, rightdf.ix[:,["USAF_WBAN","STATION NAME","LAT","LON"]],
                           left_on="ID", right_on="USAF_WBAN")
    mergedDf.to_csv(out)