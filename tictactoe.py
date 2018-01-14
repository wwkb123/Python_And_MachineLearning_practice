def printBoard():
    print(boardlist[0],"|",boardlist[1],"|",boardlist[2])
    print("-- --- --")
    print(boardlist[3],"|",boardlist[4],"|",boardlist[5])
    print("-- --- --")
    print(boardlist[6],"|",boardlist[7],"|",boardlist[8])
def horizontal(mark):
    return boardlist[0]==mark and boardlist[1]== mark and boardlist[2]==mark or boardlist[3]==mark and boardlist[4]==mark and boardlist[5]==mark or boardlist[6]==mark and boardlist[7]==mark and boardlist[8]==mark
def vertical(mark):
    return boardlist[0]==mark and boardlist[3]==mark and boardlist[6]==mark or boardlist[1]==mark and boardlist[4]==mark and boardlist[7]==mark or boardlist[2]==mark and boardlist[5]==mark and boardlist[8]==mark
def diagonal(mark):
    return boardlist[0]==mark and boardlist[4]==mark and boardlist[8]==mark or boardlist[2]==mark and boardlist[4]==mark and boardlist[6]==mark

isFinished = False
isPlayer1 = True
someoneWin = False
moveCount = 0
lastPlayer = 1
boardlist = [1,2,3,4,5,6,7,8,9]
while not isFinished and moveCount<9:
    printBoard()
    if isPlayer1:
        user_input = input("Player 1 (O) enter a number(1-9): ")
        boardlist[int(user_input)-1] = "O"
        isPlayer1 = not isPlayer1
        lastPlayer = 1
    else:
        user_input = input("Player 2 (X) enter a number(1-9): ")
        boardlist[int(user_input)-1] = "X"
        isPlayer1 = not isPlayer1
        lastPlayer = 2
    moveCount+=1
    if lastPlayer==1:
        if horizontal("O") or vertical("O") or diagonal("O") :
            isFinished = True
            someoneWin = True
    else:
        if horizontal("X") or vertical("X") or diagonal("X") :
            isFinished = True
            someoneWin = True

else:
    printBoard()
    if someoneWin:
        print("Player ",lastPlayer, " win!")
    else:
        print("Tied!")


