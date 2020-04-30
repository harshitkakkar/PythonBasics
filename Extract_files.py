# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:26:57 2020

@author: hkacker
"""

import glob
import os
import patoolib

def extractedfiles(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input",
                   out="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted"):
    
    os.chdir(indir)
    archives = glob.glob("*.gz*")
    if not os.path.exists(out):
        os.makedirs(out)
    files = os.listdir("Extracted")
    for archive in archives :
        if archive[:-3] not in files :
            patoolib.extract_archive(archive, outdir=out)
        
    