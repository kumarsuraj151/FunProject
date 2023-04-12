import os
import shutil

path="./"
file= os.listdir("./")
for fil in file:
    if '.' in fil:
        res = fil.split('.', 1)
        if os.path.exists('./'+res[1]+"File")==False:
            os.makedirs(res[1]+"File")

for fil in file:
    if '.' in fil:
        res = fil.split('.', 1)
        mpath=res[1]+"File"+"/"
        shutil.move(fil,mpath)