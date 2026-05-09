import os 

files = os.listdir("clutteredFolder")
i = 1
for file in files :
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}",f"clutteredFloder/{i}.png")
        i = i + 1