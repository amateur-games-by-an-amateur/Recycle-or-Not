
import parse_docs


#guard
if __name__ == '__main__':
    text,choices,nextFiles,goodBorN,points = parse_docs.parseChoice('Choices\c1.txt')
    #0: good
    #1: bad
    #2: neutral
    goodBadN = [0,0,0]
    while(True):
        choice = -1
        while (not -1 < choice < len(choices)):    
            print(text)
            for i in range(len(choices)):
                print('\t' + str(i) + ': ' + choices[i])
            
            choice = int(input().strip())
        goodBadN[int(goodBorN[choice].strip())] += int(points[choice].strip())
        if(nextFiles[choice].strip() == 'end.txt'):
            break
        text,choices,nextFiles,goodBorN,points = parse_docs.parseChoice('Choices\\' + nextFiles[choice].strip())
    print('Good Points: ' + goodBadN[0])    
    print('Bad Points: ' + goodBadN[1])    
    print('Neutral Decisions: ' + goodBadN[2])
    if(goodBadN[1] > goodBadN[0]):
        print('You feel the world start to heat up, but it couldn\'t have been just your fault, right?')
    elif(goodBadN[1] < goodBadN[0]):
        print('You feel the world start to cool down, it wasn\'t that hard to make a difference, now was it? Small choices matter too')
    else:
        print('You feel the world start to heat up, but it couldn\'t have been your fault. It\'s it\'s not like your single efforts would have made a difference, right?')
    print('Every choice matters, even the small ones. Make good decisions, some of them aren\'t hard.')