import random

wordList = ('horse', 'wave', 'window', 'human')
life = 6
nowWord = random.choice(wordList)
distWord = len(nowWord)
sliceDistWord = nowWord.split()
textnow = []
fakeWord = []
for i in nowWord:
    textnow.append(i)
    fakeWord.append('*')
game = True
print('Your word is:')
print(fakeWord)
print('Enter letter:')
useLetter = [1]


def checkWord(life, game, textnow, fakeWord, useLetter):
    if life > 0:
        if game == True:
            find = 0
            text = input()
            if all(i != text for i in useLetter):
                useLetter.append(text)
                for i in textnow:
                    if text == i:
                        find += 1
                if find > 0:
                    print('Yes!')
                    x = 0
                    for i in textnow:
                        z = 0
                        if i == text:
                            fakeWord[x] = text
                            for i in fakeWord:
                                if i == '*':
                                    z += 1
                            if z == 0:
                                game = False
                                break
                        x += 1
                else:
                    life -= 1
                    print('NO! -1 life')
                    print('Total life = ' + str(life))
                print(fakeWord)
                print('Used letter:')
                for i in useLetter:
                    print(str(i) + ' ', end='')
                print()
                checkWord(life, game, textnow, fakeWord, useLetter)
            else:
                print('This letter already use!')
                checkWord(life, game, textnow, fakeWord, useLetter)
        else:
            print('Game over. You win')
    else:
        game = False
        print('Game over - life 0')
        print('Right word is:')
        for i in textnow:
            print(str(i), end='')


checkWord(life, game, textnow, fakeWord, useLetter)
