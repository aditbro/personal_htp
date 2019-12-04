from os import walk, listdir

mypath = "..\\Group\\Audio\\"
dirs = listdir(mypath)

with open("codetr.scp", 'w') as output:
    for folder in dirs:
        curdir = mypath+str(folder)
        filenames = listdir(curdir)
        for row in filenames:
            output.write(curdir + "\\" + str(row)  + " ..\\train\\"+ row[:-4] + ".mfc" +'\n')


