from pathlib import Path
p2 = Path('AgroCD')

#To list files in folder
flist = p2.iterdir()
print(list(flist))

