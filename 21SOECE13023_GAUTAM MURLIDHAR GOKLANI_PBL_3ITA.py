import os,shutil
path=input("Enter path: ")
files=os.listdir(path)
for file in files: 
    fname,ext = os.path.splitext(file)
    ext=ext[1:]
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)