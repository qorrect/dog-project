    
    
    
keepers = [
    "/home/q/Downloads/cpratt.jpg",
    "/home/q/Downloads/cpratt3.jpg",
    "/home/q/Downloads/cpratt4.jpg",
    
    "/home/q/Downloads/bmurray.jpg",
    "/home/q/Downloads/bmurray2.jpg",    
    
    "/home/q/Downloads/bmurray4.jpg",    
    "/home/q/Downloads/bmurray6.jpg",    
    
    "/home/q/Downloads/jroberts.png",
    "/home/q/Downloads/jroberts2.jpg",
    "/home/q/Downloads/jroberts3.jpg"
]

import shutil, os 

for k in keepers:
    shutil.copyfile(k, os.getcwd() + "/" + os.path.basename(k))
    
