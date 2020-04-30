# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:07:36 2020

@author: hkacker
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:41:01 2020

@author: hkacker
"""

import os
import pandas
import glob

def concat(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\New_Input",
           out="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\New_Input\\out\\concatenate_rmerged.csv"):
  #  os.chdir(indir)
    FileList = glob.glob("*.xls")
    dfStates=pandas.read_csv("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\New_Input\\Geoids_states.csv")
    rvduplicate = pandas.read_csv("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\New_Input\\\\out\\concatenate_rmduplicate.csv")
    dfFileList=[]
    columnNames = ["GEOID","1984","GEOID","1985","GEOID","1986","GEOID","1987","GEOID","1988",
                   "GEOID","1989","GEOID","1990","GEOID","1991","GEOID","1992","GEOID","1993",
                   "GEOID","1994","GEOID","1995","GEOID","1996","GEOID","1997","GEOID","1998",
                   "GEOID","1999","GEOID","2000","GEOID","2001","GEOID","2002","GEOID","2003",
                   "GEOID","2004","GEOID","2005","GEOID","2006","GEOID","2007","GEOID","2008",
                   "GEOID","2009","GEOID","2010","GEOID","2011","GEOID","2012","GEOID","2013"]
    for filename in FileList :
        print(filename)
        df = pandas.read_excel(filename , skiprows=[0,1,2])
        dfFileList.append(df)
    concatdf = pandas.concat(dfFileList, axis=1)
    concatdf.columns = columnNames
    rmduplicate = concatdf.T.drop_duplicates().T
    Merged = pandas.merge(rvduplicate,dfStates,rvduplicate_on="GEOID",dfStates_on="GEOID")
    Mergeddf = Merged.set_index(["GEOID","state"], inplace=True)
    Mergeddf.to_csv(out, index=0)
        
        
        
    