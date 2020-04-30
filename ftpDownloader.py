# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:31:46 2020

@author: hkacker
"""

from ftplib import FTP , error_perm
import os 
import glob
import patoolib

def ftpdownloader(stationID,startYear,endYear,
                  host="ftp.pyclass.com",user="student@pyclass.com",password="student123") :
     ftp = FTP(host)
     ftp.login(user,password)
#     print(ftp.nlst())  
     ftp.cwd("Data")
     if not os.path.exists("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input"):
         os.makedirs("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input")
     os.chdir("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input")
     
     for year in range (startYear,endYear+11):
         fullpath='/Data/%s/%s-%s.gz' %(year,stationID,year)
         filename = os.path.basename(fullpath)
         try:
             with open(filename, 'wb') as file :
                 ftp.retrbinary('RETR %s' %fullpath, file.write)
             print("%s succesfully downloaded" % filename)
                 
         except error_perm:
             print("%s is not available" % filename)
             os.remove(filename)
     ftp.close()
        
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
            

     
    
                 