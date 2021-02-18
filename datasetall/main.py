import os

for filename in os.listdir("./test/"):
    if filename.endswith(".json"):
        os.remove("./test/"+filename)

for filename in os.listdir("./train/"):
    if filename.endswith(".json"):
        os.remove("./train/"+filename)
