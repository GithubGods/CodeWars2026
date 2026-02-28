def palindrome(liney):
    # One line
    longestStr = liney[0]
    for i, spot in enumerate(liney):
        if not i == len(liney)-1  and liney[i+1] == spot:
            print("hi")
            line = liney[0:i] + liney[i+1:]
        else:
            line = liney
        d = 0
    
        while line[i-d] == line[i+d]:
        
            if not i == len(liney)-1 and not liney[i+1] == spot:
                if len(longestStr) < len(line[i-d: i+d+1]):
                    longestStr = line[i-d: i+d+1]
            else:
                if len(longestStr) < len(line[i-d: i+d+1]) + 1 and not i == len(liney)-1:
                    longestStr = line[i-d: i] + spot + line[i: i+d+1]
            d+=1
            if i-d < 0 or i+d >= len(line): break

    print(longestStr)