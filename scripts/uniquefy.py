f = open("fulllist", "r")
uset = {"@"}

for line in f:
    line = line.replace("\n", "")
    uset.add(line)



for entry in sorted(uset):
    print(entry)