def getWriteFile(path,text,startTime,endTime):
    with open(path, "a",encoding="utf-8") as f:
        f.write(f"{startTime} --> {endTime}")
        f.write("\n")
        f.write(f"{text}")
        f.write("\n")
        f.write("\n")