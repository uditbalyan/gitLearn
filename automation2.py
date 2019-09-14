import sqlite3 
import git, os, shutil

import sys
import datetime
import time


#LOGGING THE TIME DETAILS 

currentDT = datetime.datetime.now()
print (str(currentDT))


 # CODE TO PULL 

 
DIR_NAME1 = "iaaportal"
DIR_NAME2 = "iaportal"
DIR_NAME3 = "ias"


REMOTE_URL1 = "https://github.com/nileshk1/repo2"
REMOTE_URL2 = "https://github.com/nileshk1/repo2"
REMOTE_URL3 = "https://github.com/nileshk1/repo2"

#https://github.com/nileshk1/repo2


 
if os.path.isdir(DIR_NAME1):
    shutil.rmtree(DIR_NAME1)
 
os.mkdir(DIR_NAME1)

if os.path.isdir(DIR_NAME1):
    shutil.rmtree(DIR_NAME1)
 
os.mkdir(DIR_NAME1)

if os.path.isdir(DIR_NAME2):
    shutil.rmtree(DIR_NAME2)
 
os.mkdir(DIR_NAME2)




 
repo = git.Repo.init(DIR_NAME1)
origin = repo.create_remote('origin',REMOTE_URL1)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
 


repo = git.Repo.init(DIR_NAME2)
origin = repo.create_remote('origin',REMOTE_URL2)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
 

repo = git.Repo.init(DIR_NAME3)
origin = repo.create_remote('origin',REMOTE_URL3)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
 
print ("---- PULLING is DONE ----")


# CODE TO ZIP THE DIRECTORIES

import shutil
shutil.make_archive(DIR_NAME1, 'zip', DIR_NAME1)
shutil.make_archive(DIR_NAME2, 'zip', DIR_NAME2)
shutil.make_archive(DIR_NAME3, 'zip', DIR_NAME3)



print ("---- ZIPPING is DONE ----")








print ("---- UPloading is DONE ----")





##### ADD A DELAY OF 5 min before deleting the files

time.sleep(300000) # 1000 is equal to 1 sec 

os.remove(DIR_NAME1+".zip")
os.remove(DIR_NAME2+".zip")
os.remove(DIR_NAME3+".zip")



print ("---- ZIP files deleted  is DONE ----")