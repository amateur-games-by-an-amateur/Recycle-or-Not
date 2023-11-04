def parseChoice(fname):
    lines = []
    for i in open(fname):
        lines.append(i)
    text = lines[0]
    choices = lines[1].split('|')
    nextFiles = lines[2].split('|')
    goodBorN = lines[3].split('|')
    points = lines[4].split('|')
    return text,choices,nextFiles,goodBorN,points