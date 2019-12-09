import os
import glob
for filename in glob.glob("*.lab"):
    with open(filename) as f:
        for line in f:
            line = line.split(" ")
            fname = line[0]
            l = " ".join(line[1:])
            fout = open("labra/{}.lab".format(fname), "w")
            fout.write(l)
            fout.close()