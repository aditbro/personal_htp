f = open("sample.dict", "r")

for line in f:
    line = line.replace("\n", "")
    line = line.split(" ")
    line[1] = line[1].replace("[", "")
    line[1] = line[1].replace("]", "")
    print("{} {}".format(line[1], line[2]))