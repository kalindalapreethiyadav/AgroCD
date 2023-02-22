from pathlib import Path
path = Path('AgroCD')

#To list files in folder
flist = path.iterdir()
print(list(flist))

#To list all files in folder path
for obj in list(path.iterdir()):
    print(obj)

#