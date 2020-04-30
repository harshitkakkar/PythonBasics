from ftplib import FTP, error_perm
import os
import glob
import pandas
import numpy
#import patoolib
import seaborn as sns

def ftpDownloader(stationId,startYear,endYear,url="ftp.pyclass.com",user="student@pyclass.com",passwd="student123"):
    ftp=FTP(url)        
    ftp.login(user,passwd)
    if not os.path.exists("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input"):           
        os.makedirs("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input")
    os.chdir("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input")
    for year in range(startYear,endYear+1):
        fullpath='/Data/%s/%s-%s.gz' % (year,stationId,year)    
        filename=os.path.basename(fullpath)
        try:
            with open(filename,"wb") as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
            print("%s succesfully downloaded" % filename)
        except error_perm: 
            print("%s is not available" % filename)
            os.remove(filename)    
    ftp.close()
    
            
def extractFiles(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input",
                 out="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted"):
    os.chdir(indir)
    archives=glob.glob("*.gz")
    print (archives)
    if not os.path.exists(out):
       os.makedirs(out)
    files=os.listdir("Extracted")
    print(files)
    for archive in archives:
        if archive[:-3] not in files:
            patoolib.extract_archive(archive,outdir=out)
            

def addField(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted"):
    os.chdir(indir)
    fileList=glob.glob("*")
    print ("fileList" ,fileList)
    for filename in fileList:
        df=pandas.read_csv(filename,sep='\s+',header=None)
        df["Station"]=[filename.rsplit("-",1)[0]]*df.shape[0]
        df.to_csv(filename+".csv",index=None,header=None)
        os.remove(filename)
        
def concatenate(indir="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted",
                outfile="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\New_concatenate.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    dfList=[]
    colnames=["Year","Month","Day","Hour","Temp","DewTemp","Pressure","WindDir","WindSpeed","Sky","Precip1","Precip6","ID"]
    for filename in fileList:
        print (filename)
        df=pandas.read_csv(filename,header=None)
        dfList.append(df)
    concatDf=pandas.concat(dfList,axis=0)    
    concatDf.columns=colnames
    concatDf.head()
    concatDf.to_csv(outfile,index=None)
    
def merge(left="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\New_concatenate.csv",
          right="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Station_info.txt",
          output="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\New_merged_concat.csv"):
    leftDf=pandas.read_csv(left)   
    rightDf=pandas.read_fwf(right,converters={"USAF":str,"WBAN":str})
    rightDf["USAF_WBAN"]=rightDf["USAF"]+"-"+rightDf["WBAN"]
    mergedDf=pandas.merge(leftDf,rightDf.ix[:,["USAF_WBAN","STATION NAME","LAT","LON"]],left_on="ID",right_on="USAF_WBAN")
    mergedDf.to_csv(output)

def pivot(infile="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\New_merged_concat.csv",
          outfile="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\Pivoted.csv"):
    df=pandas.read_csv(infile)
    df=df.replace(-9999,numpy.nan)
    df['Temp']=df["Temp"]/10.0
    table=pandas.pivot_table(df,index=["ID","LON","LAT","STATION NAME"],columns="Year",values="Temp")
    table.to_csv(outfile)
    return table

def plot (outfile="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\plot.png"):
        df = pivot()
        df.T.plot(subplots=True,kind='bar')
        sns.savefig(outfile , dpi=200)
        
def kml(input="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\Pivoted.csv", 
        out="C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\Weather.kml"):
    
        kml=simplekml.Kml()
        df=pandas.read_csv(input,index_col=["ID","LON","LAT","STATION NAME"])
        for lon,lat, name in zip(df.index.get_level_values("LON"),df.index.get_level_values("LAT"),df.index.get_level_values("STATION NAME")):
            kml.newpoint(name=name , coords=[(lon,lat)])
            kml.save(out)
 
if __name__=="__main__":
    
    stationsIdString=input("Enter name of stationId divided by comas: ")
    startingtYear=int(input("Enter starting year: "))
    endingYear=int(input("Enter ending Year: "))
    stationIdList=stationsIdString.split(',') 
    
    for station in  stationIdList:
        ftpDownloader(station,startingtYear,endingYear)
    
    extractFiles()
    addField()
    concatenate()
    merge()
    pivot()
    plot()
    kml()
    
    
    
    
        
        
        
        