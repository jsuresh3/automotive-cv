# %%
import cv2
import os
import shutil
from pathlib import Path
# %%
#set_kitti_path = "..\\datasets" # Path to the kitti dataset ....\\kitti

# %%
#creates imgs and sets them to righ folder

def create_text_img(imgnum, foldernum):
   
   new_name=str(int(foldernum)) + '_' + str(int(imgnum))

   if int(imgnum) %4 != 0:
      new_dir = '..\\datasets\\yolo\\images\\train\\'
      newfile = f'..\\datasets\\yolo\\labels\\train\\{new_name}.txt'
   else:
      new_dir = '..\\datasets\\yolo\\images\\test\\'
      newfile = f'..\\datasets\\yolo\\labels\\test\\{new_name}.txt'
   
   
   with open(newfile, "w") as file:
      pass
   

   
   image_path=f'{set_kitti_path}\\training\\image_02\\{foldernum}\\{str(imgnum).zfill(6)}.png'
   new_name=f'{new_name}.png'
   
   

   # Copy the file to the new location with the new name
   shutil.copy2(image_path, f'{new_dir}{new_name}')

   return newfile
      



def readfile(file_path,filenum):
    nc=['Car','Cyclist','Pedestrian','Truck','Van','Tram','Misc','Person','DontCare']
    with open(file_path) as f:
        strfilenum=(str(filenum)).zfill(4)
        counter=-1
        for line in f:
            elements = line.split()

            imgnum = elements[0]
            
            if imgnum!=str(counter):
                newfile=create_text_img(imgnum, strfilenum)
                counter=imgnum
            
            label = elements[2]
            
            xmin = int(float(elements[6]))/1242
            ymin = int(float(elements[7]))/375
            xmax = int(float(elements[8]))/1242
            ymax = int(float(elements[9]))/375
            
            if nc.index(label)>5:
                continue     
            str_to_append = str(nc.index(label)) + " " + str((xmax+xmin)/2) + " " + str((ymin+ymax)/2) + " " + str(xmax-xmin) + " " + str(ymax-ymin) + "\n"
            imgnum = imgnum.zfill(6)

            with open(newfile, 'a') as file:
                file.write(str_to_append)

                     

                    
                # Check if the folder exists
                


folder_path = Path(set_kitti_path+"\\training\\label_02")
print(folder_path)
for filename in os.listdir(folder_path):
    # print("fn-",filename)
    filenum = filename.split('.')[0]
    filenum = int(filenum)
    print(filenum)
    file_path = os.path.join(folder_path, filename)

    print("fp-",file_path)

    readfile(file_path, filenum)
