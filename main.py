
import parse_docs

#guard
if __name__ == '__main__':
    
    #0: good
    #1: bad
    #2: neutral
    while True:
        text,choices,nextFiles,goodBorN,points = parse_docs.parseChoice('Choices\c1.txt')
        goodBadN = [0,0,0]
        while(True):
            choice = -1
            while (not -1 < choice < len(choices)):    
                print(text)
                for i in range(len(choices)):
                    print('\t' + str(i) + ': ' + choices[i])
                
                choice = input().strip()
                if(choice.isdigit()):
                    choice = int(choice)
                else:
                    choice = -1
            goodBadN[int(goodBorN[choice].strip())] += int(points[choice].strip())
            if(nextFiles[choice].strip() == 'end.txt'):
                break
            text,choices,nextFiles,goodBorN,points = parse_docs.parseChoice('Choices\\' + nextFiles[choice].strip())
        print('Good Points: ' + str(goodBadN[0]))    
        print('Bad Points: ' + str(goodBadN[1]))    
        print('Neutral Decisions: ' + str(goodBadN[2]))
        print()
        print("You return home after your work and reflect on your day as you drift to sleep:\nDid you change the world and save it from its fate OR Did you abandon it to its fate.")
        print()
        if(goodBadN[1] > goodBadN[0]):
            print('You feel the world start to heat up, but it couldn\'t have been just your fault, right?')
            if goodBadN[1] == 0:
                print("You have changed the world for the better and saved it from a terrible fate, the seemingly small choices you made, created ripples and people followed your example and together you successfully changed the world. Every action we do counts in Changing the World around us, and every change can allow the future to become even the slightest amount brighter.")
            else:
                print("You have helped ease the world’s burden but have not quite saved it completely. Good job on making a difference, but try to see where you may have fallen short.")
            print()
        
        elif(goodBadN[1] < goodBadN[0]):
            print('You feel the world start to cool down, it wasn\'t that hard to make a difference, now was it? Small choices matter too.')
            if goodBadN[0] == 0:
                print("You have sealed the world\’s coffin and disaster ensues. The continuous death of nature and rising water levels, spells the end for the world, but there is still hope. You still have the power to save the world, your actions shall once again determine our fate.")
            else:
                print("You have eased the world’s burden but have another chance to do more. Try to find where you may have fallen short. Every choice affects our world’s future.")
            print()
        else:
            print('You feel the world start to heat up, but it couldn\'t have been your fault. It\'s it\'s not like your single efforts would have made a difference, right?')
            print("You have not eased the world’s burden, nor did you exacerbate its suffering but you failed to change it at all. Sometimes making choices is difficult, especially when the fate of the world is in our hands but you have another chance to save the world. Try to find where you may have fallen short in decisiveness, every choice affects our world’s future but you can do it.")
        print('Every choice matters, even the small ones. Make good decisions, some of them aren\'t hard.')
        play_again = None
        while(play_again != 'y' and play_again != 'n'):
            play_again = input("Want to play again (y/n): ").lower().strip()
        if play_again == "n":
            break
        