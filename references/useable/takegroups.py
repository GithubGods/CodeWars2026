global tot
tot = 0

def useGroup(groupString):
    # do whatever
    global tot
    tot += int(groupString)
    pass

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
    
    global tot
    return tot

if __name__ == "__main__":
    print(takegroups("ijsdfl34 flskdfj4"))