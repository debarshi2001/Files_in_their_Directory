from pathlib import Path
from pkgutil import iter_modules
import shutil,os
from time import process_time


source=os.path.abspath(os.getcwd()) #Current Directory Path
dest_of_IMG=0
dest_of_Music=0
dest_of_Vdo=0
dest_of_Txt=0

start=process_time()  #Starting of CPU time


# Creating Folders/Directories according to the files.
basepath = Path('./')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        if item.name.endswith('.mp3'):                                          #For Music Files
            if os.path.isdir('./yourMUSICS/')==False:
                dest_of_Music=os.path.join(source,'yourMUSICS')
                os.mkdir(dest_of_Music)
            else:
                pass

        elif item.name.endswith(('.jpeg','.JPG','.jpg','.dng','.png')):         #For Image Files
            if os.path.isdir('./yourIMAGES/')==False:                               
                dest_of_IMG=os.path.join(source,'yourIMAGES')
                os.mkdir(dest_of_IMG)
                I=dest_of_IMG
            else:
                pass
                
        elif item.name.endswith(('.mp4','.wav')):                               #For Video Files
            if os.path.isdir('./yourVIDEOS/')==False:
                dest_of_Vdo=os.path.join(source,'yourVIDEOS')
                os.mkdir(dest_of_Vdo)
            else:
                pass
        
        elif item.name.endswith(('.pdf','.txt')):                               #For Text,Pdf Files
            if os.path.isdir('./yourPDFs/')==False:
                dest_of_Txt=os.path.join(source,'yourPDFs')
                os.mkdir(dest_of_Txt)
            else:
                pass
        
# Moving files to their alloted folders/Directories   
basepath = Path('./')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        if item.name.endswith('.mp3'):
            src=os.path.join(source,item.name)
            des=os.path.join(dest_of_Music,item.name)
            shutil.move(src,des)
            print(item.name+' moved successfully')

        elif item.name.endswith(('.jpeg','.JPG','.jpg','.dng','.png')):
            src=os.path.join(source,item.name)
            des=os.path.join(dest_of_IMG,item.name)
            shutil.move(src,des)
            print(item.name+' moved successfully')
                           
        elif item.name.endswith(('.mp4','.wav')):
            src=os.path.join(source,item.name)
            des=os.path.join(dest_of_Vdo,item.name)
            shutil.move(src,des)
            print(item.name+' moved successfully')
        
        elif item.name.endswith(('.txt','.pdf')):
            src=os.path.join(source,item.name)
            des=os.path.join(dest_of_Txt,item.name)
            shutil.move(src,des)
            print(item.name+' moved successfully')
        else:
            print("Failed to move items")
    else:
        print("Sorry!!The Folder is Empty")  
    


end=process_time()             #End of CPU time
print("\nTotal time taken for moving files:{} Seconds.".format((end-start)))

#Steps to run this code are given in the README file.Please check that once.
