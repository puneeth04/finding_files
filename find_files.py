import os

i=os.getcwd()

def find_files(i):
     dir_path=os.listdir(i)
     print(j,dir_path)
     for x in os.listdir(i):
         path=os.path.join(i,x)
         if os.path.isdir(path):
             find_files(path)


for j in os.listdir(i):
        new_dir_path=os.path.join(i,j)
        if os.path.isdir(new_dir_path):
                find_files(new_dir_path)
                            
        else:
               print(j)
        

find_files(i)
