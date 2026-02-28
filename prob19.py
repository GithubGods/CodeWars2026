with open("input.txt", "r") as f:
	INPUT = f.read().strip()

global dictionary
dictionary = {}

def useGroup(groupString):
    # do whatever
    if len(groupString) > 2 or len(groupString) == 1: return
    global dictionary
    if not dictionary.get(groupString): dictionary[groupString] = 0
    dictionary[groupString] += 1

def takegroups(string, targetChars="1234567890"):
    groupString = ""
    for char in string:
        if char in targetChars:
            groupString += char
        else:
            if groupString:
                useGroup(groupString)
                groupString = ""
    if groupString:
        useGroup(groupString)
        groupString = ""
    
    global dictionary
    return dictionary

if __name__ == "__main__":
    print(takegroups(INPUT, "aeiou"))