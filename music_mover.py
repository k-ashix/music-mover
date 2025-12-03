# 🎵 Music Organizer - Move all MP3 files to one folder

import shutil
import string
import os
from pathlib import Path

print("-"*60)
print("🎵 WELCOME TO MUSIC ORGANIZER 🎵".center(60))
print("-"*60)
print()

def show_ending():
    '''Display Ending Credits'''
    print("🎵 Music organization complete! 🎵")
    print()
    print(f"👋 See you next time!")
    print(f"Created by: @k_ashix")
    print("Follow me on X: https://x.com/k_ashix")
    print()

    import webbrowser
    webbrowser.open("https://x.com/k_ashix")


#Scan drives in windows
def get_available_drives():
    """Scan and return all available drives in the system"""
    drives = [] # List to store our drives leter 
    
    for letter in string.ascii_uppercase:
     if os.path.exists(f"{letter}:\\"):
         drives.append(letter) # Update our drives List
    return drives # return the values to ther get_available_drives function

# Calling def get_available_drives to store drives alphabet in drives list
drives = get_available_drives()

# bounding user to choose only Available Drives
while True:
    #Available dives in system
    print (f"\nAvailable Drives : {drives} \n") 
    chosen_drive = input("➤ Enter only the available drive letter: ").upper()
    
    # getting input form user for choosing driver letter 
    if chosen_drive in drives:
        print(f"✓ You Chose: {chosen_drive} \n") #printing the choose drive
        break #breaking the program to choose again without error 
    else:
        print(f"❌ No drive exits! Please choose from available ones")
    
def dir_name():
    fold = input ("➤ Enter You Folder Name: ").strip()
    return fold

create_folder = input(f"\nDo you want to continue your music sorting (Yes/no): ").lower()
print()
if create_folder == 'yes':
    # Create the folder
    fold = dir_name()
    print (f"Your folder name = {fold} \n")
    os.mkdir(rf"{chosen_drive}:\{fold}")
else:
    show_ending()
    exit()      
# print (f"Directory created at {chosen_drive}:\{fold}")

#Where folder is creted 
print (f"\nYou created folder 📂 in drive: {chosen_drive} with name of {fold}")

# Get the path using pathlib
dir_path = Path(rf"{chosen_drive}:\{fold}")
print (f"Here is Your:📂 {fold} -> {dir_path}\n")

#before moving we have to find all mp3
mp3_files = list(Path(f"{chosen_drive}:/").rglob("*.mp3"))

# Calculating total size of all found MP3 files
total_mp3_size_bytes = sum(file.stat().st_size for file in mp3_files)
# Creating a funciton here to formate found in reaadlable formate
def formate_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} PB"
# it will give no of files 
print (f"🎵 No of Muisc / .mp3 files Found in {(chosen_drive)}: {len(mp3_files)}")  
# it shows size of all files
print(f"💾 Total Size of {len(mp3_files)} files: {formate_size(total_mp3_size_bytes)}")

#Asking user if he need files name in .txt
view_list = input(f"\n👀 Do you want to view you .mp3 files name in terminal? (Yes/no): ").lower()

if view_list == 'yes':
    # printing name fo all files
    print(f"\n---List of all mp3 files found in: {chosen_drive}\n") 
    for index, file in enumerate(mp3_files, start=1):
        print(f"{index}. {file.name} → {file.parent}")
        print ()
    print(f"\n--- End of List ---- \n")
else:
    print(f"Skipping mp3 list view.")
    
# crating a file conating all muisc found in choosen drive
create_list = input(f"\n📄 Do you want to save a list to a text file? (Yes/no): ").lower()
print()

if create_list == 'yes':
    txt_path = rf"{chosen_drive}:\{fold}\Music_List.txt"
    
    with open (txt_path, 'w' , encoding='utf-8') as f:
        f.write(f"🎵 MP3 FILES FOUND IN {chosen_drive} DRIVE \n")
        f.write(f"Toatl No of music: {len(mp3_files)} files \n")
        f.write(f"Toatl Size: {formate_size(total_mp3_size_bytes)}\n \n")
        f.write(f"\n--- List of all mp3 files found in: {chosen_drive} ---\n \n")
               
        for index, file in enumerate(mp3_files, start=1):
            
            f.write(f"{index}. {file.name} → {file.parent} \n")
        f.write(f"\n--- End of List ---- \n")
    print(f"✓ Music List saved as Music_List.txt at {txt_path}")
else:
    print("⏭️  Skipped text file creation")

# moveing all mp3, from windows to fold created above
move_music = input(f"\nDo you want to move all .mp3 files of {chosen_drive} drive in your {fold} fo? (Yes/No) \n").lower()

if move_music == 'yes':
    print(f"\n ⚠️ Moving Files {len(mp3_files)} files to {chosen_drive} {fold}...\n")
    
    for file in mp3_files:
        shutil.move(str(file), rf"{chosen_drive}:\{fold}\{file.name}")
        print (f"✓ MP3 files moved: {file.name}")
    print(f"✓ All {len(mp3_files)} files moved successfully!")
else:
    print(f"Skipped moving files.\n")

show_ending()
exit()