f = open("fulllist", "r")
lines = []

for line in f:
    line = line.replace("\n", "")
    lines.append(line)

lines.sort()
for l in lines:
    print(l)