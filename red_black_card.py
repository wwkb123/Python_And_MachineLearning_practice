from random import shuffle
sum = 0
for trial in range(0,100000):
    redList = ['r' for x in range(0,26)]
    blackList = ['b' for x in range(0,26)]
    cardList = redList+blackList
    shuffle(cardList)
    i = 0
    count = 0
    for card in cardList:
        if i is 0:
            if card is 'b' and cardList[i+1] is 'r':
                count += 1
        elif card is 'r' and i < len(cardList)-1:
            if cardList[i+1] is 'b' or cardList[i-1] is 'b':
                    count += 1
        elif i is len(cardList)-1 and card is 'r' and cardList[i-1] is 'b':
            count += 1
        i += 1
    sum += count
print(sum/100000)