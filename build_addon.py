import shutil, os

# Target folder where to copy the addon's content.
# I use a custom directory to avoid having to reinstall addons at each new Blender version
# If you want to do the same, don't forget to add that path to Blender > Edit menu > Preferences > File Paths tab > Scripts

targetFolder="C:\\AppInstall\\Blender\\MyScripts\\addons"

# Input files and folders. See examples after ::
# Folders will be copied with their full content.
# Put them between quotation marks, one per line, and increment the number between [ ]
# You can write in absolute and relative paths, I chose relative for simplicity.

inputFiles=[
   "convert_Rotation_Mode.py"
   ]

print(__file__)
print(os.path.join(os.path.dirname(__file__)))
print()

# inputFiles[1]="example_file.ext"
# inputFiles[2]="example folder"

for file in inputFiles:
   try:
      shutil.copy(f"{os.path.join(os.path.dirname(__file__))}\\{inputFiles[0]}", targetFolder)
      print(f" copied '{file}' to '{targetFolder}'.")
   except:
      print(f" Couldn't copy '{file}' to '{targetFolder}'.")

# input()