f = open("dict", "r")
i = 0

for line in f:
    line = line.replace("\n", "")
    l = line.split(" ")
    l0 = l[0]
    l1 = " ".join(l[1:])
    result = "{} [{}] {}".format(l0, l0, l1)
    i += 1
    print(result)