# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:43:28 2020

@author: hkacker
"""

from ftplib import FTP 
import os 

def ftpdownloader(filename,host="ftp.pyclass.com",user="student@pyclass.com",password="student123") :
     ftp = FTP(host)
     ftp.login(user,password)
#     print(ftp.nlst())  
     ftp.cwd("Data")
     os.chdir("C:\\Users\\hkacker\\Documents\\Python_Scripts")
     with open(filename, 'wb') as file :
         ftp.retrbinary('RETR %s' %filename, file.write)
