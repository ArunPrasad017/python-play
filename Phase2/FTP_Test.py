import os
import ftplib
import zipfile
import config

ftp = ftplib.FTP("ftp.census.gov")
ftp.login(config.name,config.passwd)
ftp.cwd("/acs2003/Core_Tables")
# fnbase= "PRISM_ppt_stable_4KM"
# fnmid = "2_ " # 2years before 1981
# fnend = "_all_bill.zip"
fn_name = "ACS_2003_001.zip"
savdir = cwd()
os.chdir(savdir)
start_year = 1990
end_year =2016

for year in range(start_year,end_year):
    if year>1980:
        fnmid = "3_"
    ftp.cwd(str(year))
    fn = fnbase + fnmid +str(year)+fnend
    with open(fn,'wb') as f:
        ftp.retrbinary("RETR "+fn,f.write)
    zfile = zipfile(fn)
    zfile.extractall()
    zfile.close()
    os.remove(fn)
    ftp.cwd("../")
    print(str(year)+' is done')

# to upload
fn_name = "ACS_2003_001_modified.zip"
ftp.storbinary('STOR '+os.path.basename(fn_name), open(fn_name,'rb'))
print('upload done')

ftp.quit()