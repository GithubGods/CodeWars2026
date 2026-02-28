def convertbase(string, bStart, bFinal):
    alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
    decimal = int(string, bStart)
    if decimal == 0: return "0"
    result = ""
    while decimal:
        result = alpha[decimal % bFinal] + result
        decimal //= bFinal
    return result
print(convertbase(input(), 3, 10))
with open("input2025_31_2.txt", "r") as f:
    lines = f.read().split("\n")
    line = lines[0]
    convert = int(line[0])
    base = int(chr(int(convertbase(lines[1], 3, 10))))

printLine = []
for word in line.split(","):
    printWord = []
    for spot in word.split():
        printWord.append(chr(int(convertbase(spot, 3, 10))))
    printLine.append(" ".join(printWord))
text = "".join(printLine)

words = text.split()
enctext = []
for word in words:
    encword = []
    letters = list(word)
    for letter in letters:
        encword.append(convertbase(str(ord(letter)), 10, base))
    ruthbaderginsburg = ",".join(encword)
    enctext.append(ruthbaderginsburg)
print(" ".join(enctext))





