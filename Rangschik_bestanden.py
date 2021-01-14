import os
import shutil
import time

while True:
    #Print text to 'wake up' and wait 10 seconds
    print('Wat een rotzooi. Eerst even koffie.')
    time.sleep(10*1)


    sourcepath = 'C:/Users/ovest/Downloads/'
    sourcefiles = os.listdir(sourcepath)
    overig = 'C:/Users/ovest/Downloads/Overig'

#Dictionary for destinations + extensions
    infodict = {
                sourcepath + 'Afbeeldingen': ['jpg', 'png', 'tiff', 'bmp', 'gif', 'jpeg',],
                sourcepath + 'Videos': ['mp4', 'mpeg', 'avi', 'mkv', 'wmv', 'mov', 'MOV', 'MKV',],
                sourcepath + 'Muziek': ['mp3', 'aac', 'flac', 'wav',],
                sourcepath + 'Documenten': ['docx', 'doc', 'txt', 'pdf', 'PDF', 'odt',],
                sourcepath + '3D': ['stl', 'f3d', 'gcode',],
                sourcepath + 'Powerpoint': ['ppt', 'pptx',],
                sourcepath + 'Gecomprimeerd': ['rar', 'zip', '7z',],
                sourcepath + 'Toepassingen en schrijven': ['exe', 'msi', 'iso', 'img',],
                sourcepath + 'Excel': ['xls', 'xlsx',],
                sourcepath + 'Overig': '',
                }

    if len(sourcefiles) > len(infodict): #only runs program when there are new files, compared to existing folders
        for file in sourcefiles:
            filefinish = 0
            foldercheck= 0
            counter = 1
            dest = overig
            checkfile = sourcepath + file

	#Checking whether the file is or is not a folder.
            if checkfile in infodict:
                foldercheck = 1
        
	#When the file is not a folder; we can run the loop to determine which destination the file has to go to.    
            if foldercheck == 0:
                for destinations, extensions in infodict.items():
                    if file.endswith(tuple(extensions)) and filefinish == 0:
                        filefinish = 1
                        dest = destinations
                        if not os.path.exists(dest): #If not existing we want to create the folder, otherwise it keeps the 'Download' folder more neat with fewer folder if not needed.
                            os.makedirs(dest)
                    if not os.path.exists(overig):
                        os.makedirs(overig)
            
                #Move files after determination which file and extension the program is dealing with.
                for error in range (3):
                    try:
                        if counter == 1:
                            shutil.move(sourcepath + file, dest)
                            break
                        if counter > 1:
                            shutil.move(sourcepath + file, dest + '/' + '(' + str(counter) + ')' + file)
                            break
                    except shutil.Error: #When original file already exists, add '(2)' to the filename, when there are three duplicates the system rewrites the file with '(2)' in the filename.
                        #shutil.move(sourcepath + file, dest + '/' + '(2)' + file)
                        counter += 1
                        print(counter)
    
        print('Opgeruimd staat netjes')