from random import choices
import random

t=1
n=0
board=[[0 for i in range(8)] for i in range(8)]
flag_rows = [0 for i in range(8)]
flag_col = [0 for i in range(8)]
flags=[[0 for i in range(8)] for i in range(8)]
diagonal = [[0 for i in range(8)] for i in range(8)]
invalidmoves=0

def drawboard():
   for i in range (8):
    for j in range (1):
      print(board[i])

def geneartedisgonal(i,j):
    tempi=i
    tempj=j

    while(i>=0 and j>=0):
        diagonal[i][j]=1
        i-=1
        j-=1
    i=tempi
    j=tempj
    while (i >= 0 and j <=7):
        diagonal[i][j] = 1
        i -= 1
        j += 1
    i = tempi
    j = tempj
    while (j >= 0 and i <= 7):
        diagonal[i][j] = 1
        i += 1
        j -= 1
    i = tempi
    j = tempj

    while (i <= 7 and j <= 7):
        diagonal[i][j] = 1
        i += 1
        j += 1
    i = tempi
    j = tempj

def play(i,j):
    global n,invalidmoves
    if flags[i][j] == 1 or flag_col[j] == 1 or flag_rows[i] == 1 or diagonal[i][j] == 1:
        print("Inavlid move")
        invalidmoves+=1
        if invalidmoves==12:
            n=9
            print("Retry re-running code,Cant find solution with current configuration")
    else:
        flag_rows[i] = 1
        flag_col[j] = 1
        flags[i][j] = 1
        board[i][j] = 1
        drawboard()
        geneartedisgonal(i, j)
        n += 1

def toggle(togglev):
    if togglev == 1:
        togglev=0
        print("Computer's turn")
        a = random.choices([0, 1, 2, 3, 4, 5, 6, 7], k=2)
        i=a[0]
        j=a[1]
        play(i, j)
        return togglev
    else:
        togglev=1
        print("Your turn")
        i = int(input("Enter i"))
        j = int(input("Enter j"))
        play(i, j)
        return togglev

while n<=8:
    t=toggle(t)

if (n==9):
    print("Available squares were")
    for i in range(8):
        for j in range(1):
            print(diagonal[i])
    print("One Solution is")
    print("1  0  0  0  0  0  0  0\n0  0  0  0  0  0  1  0\n0  0  0  0  1  0  0  0\n0  0  0  0  0  0  0  1 \n0  1  0  0  0  0  0  0 \n0  0  0  1  0  0  0  0 \n0  0  0  0  0  1  0  0 \n0  0  1  0  0  0  0  0\n")

