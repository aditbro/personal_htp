import glob
import os
for filename in glob.glob("*.lab"):
    f = open(filename, "r")
    line = f.readline()
    line = line.replace("  ", " ")
    line = line.replace(" ", "\n")
    f.close()
    os.remove(filename)
    f = open(filename, "w")
    f.write(line)
    f.close()