# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import numpy


def pivot (inFile="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\New_merged_concat.csv" ,
           outFile="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\pivot.csv"):
     df=pandas.read_csv(inFile)
     df.replace(-9999,numpy.nan)
     df['Temp']=df["Temp"]/10.0
     table=pandas.pivot_table(df,index=["ID"],columns="Year",values="Temp")
     table.to_csv(outFile)
     return table