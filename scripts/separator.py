from os import walk, listdir

mypath = "..\\individual\\Transkrip\\"
outputpath = "..\\train\\"
filenames = listdir(mypath)

for filename in filenames:
    with open(mypath + filename, 'r') as inputf:
        for line in inputf:
            if line.strip():
                cur = outputpath + str(line[:12]) + ".lab"
                with open(cur, 'w') as outputf:
                    print(cur)
                    out = line[12:]
                    outputf.write(out.lower())
                with open("..\\all.lab", 'a') as tot:
                    tot.write(out.lower())



