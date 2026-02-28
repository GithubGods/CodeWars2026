import os
from datetime import datetime

with open("input.txt") as f:
    txt = f.read()
    signal, start, end = txt.strip().split("\n")

startTime = datetime.strptime(start, "%Y-%m-%d")
endTime = datetime.strptime(end, "%Y-%m-%d")

#Just files for prob
dirPath = "exampleFiles"
# if you need a subdirectory (folder) then use \\ to get it
# ex: files\\problem01 for Windows, files/problem01 for Linux and Mac
files = os.listdir(dirPath)


transactions = []
total = 0

for file in files:
    fileTime = datetime.strptime(file.split(".")[0], "%Y-%m-%d")

    if startTime <= fileTime <= endTime:
        #just files
        filePath = os.path.join(dirPath, file)

        with open(filePath) as f:
            lines = f.read().strip().split("\n")

        for line in lines:
            id, date, actionCode, dataIn, dataOut, opCode = line.split(",")

            if opCode == signal:
                transactions.append(id)
                total += float(dataOut)

for transaction in sorted(transactions):
    pass#print(transaction)

print(f"Funds Found: {round(total,2)}")