import glob

for filename in glob.glob("../audio/*.wav"):
	print(filename)
