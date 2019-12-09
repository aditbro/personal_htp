import os
for filename in os.listdir("../audio"):
    mfc_file = filename.split(".")[0] + ".mfc"
    print("../mfcc/{}".format(mfc_file))