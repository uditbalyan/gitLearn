
import sqlite3 
import git, os, shutil

import sys
import datetime

#LOGGING THE TIME DETAILS 

currentDT = datetime.datetime.now()
print (str(currentDT))


 # CODE TO PULL the commit time and date

 
DIR_NAME = "neel1"
REMOTE_URL = "https://github.com/nileshk1/repo2"
#https://github.com/nileshk1/repo2


 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
 
print ("---- PULLING is DONE ----")


repo = git.Repo(DIR_NAME)
tree = repo.tree()


for blob in tree:
    #commit = repo.iter_commits(paths=blob.path, max_count=1).next()
    commit= next(repo.iter_commits(paths=blob.path))
    print(blob.path, commit.committed_date)




# CODE TO DO THE MYSQL OPERATIONS AS PER OUR USECASE

# connect withe the myTable database 
connection = sqlite3.connect("ia-all") 
  
# cursor object 
crsr = connection.cursor() 
  
# execute the command to fetch all the data from the table emp 
crsr.execute("SELECT * FROM pullstatus")  
  
# store all the fetched data in the ans variable 
ans= crsr.fetchall()  

#var iaportaltime, iaaportaltime, ias 

# loop to print all the data 
for i in ans: 
    #print(i[0]) 
    iaaportaltimes = i[0]   #extracting the string from DB retrived data
    iaportaltimes = i[1]
    iastimes = i[2]

print(iaaportaltimes)   # printing the strings now
print(iaportaltimes)
print(iastimes)

iaaportaltime = int(iaaportaltimes)  # converting String to Interger
print(iaaportaltime)

iaportaltime = int(iaportaltimes)  # converting String to Interger
print(iaportaltime)


iastime = int(iastimes)  # converting String to Interger
print(iastime)

#TESTinf the integere substyraction
#z = iaaportaltime - 2753636363
#print(z)



#newtime = blob.path
#newtime1 = commit.committed_date
#newtimeint = str(newtime1)

#print(newtimeint)

#crsr.execute("UPDATE pullstatus SET iaportal ='"+ newtimeint +"' WHERE sn = 1")
#connection.commit()