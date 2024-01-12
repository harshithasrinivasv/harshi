#Tic Tac Toe game with GUI
#using tkinter

#importing all necessary libraries
import random
import  tkinter
from tkinter import*
from functools import partial
from tkinter import messagebox
from  copy import deepcopy

#sign variable to decide the turn of which player

sign = 0

#Create an empty board

global board

board = [["" for x in range(3)]for y in range(3)]

#check I(O/X) won the match or not
#according to the rules of the game


def winner(b,I):
    return ((b[0][0] == I and b[0][1] == I and b[0][2] == I) or
            (b[1][0] == I and b[1][1] == I and b[1][2] == I ) or
            (b[2][0] == I and b[2][1] == I and b[2][2] == I) or
            (b[0][0] == I and b[1][0] == I and b[1][0] == I) or
            (b[0][1] == I and b[1][1] == I and b[2][1] == I) or
            (b[0][2] == I and b[1][2] == I and b[2][2] == I) or
            (b[0][0] == I and b[1][1] == I and b[2][2] == I) or
            (b[0][2] == I and b[1][1] == I and b[2][0] == I))

#Configure text on button while playing with another player
def get_text(i,j,gb,I1,I2):
   global sign
   if board[i][j] == '':
       if sign % 2 == 0:

           I1.config(state=DISABLED)

           I2.config(state=ACTIVE)

           board[i][j] = "X"

       else:

           I2.config(state=DISABLED)

           I1.config(state=ACTIVE)

           board[i][j] = "O"

       sign += 1

       button[i][j].config(text=board[i][j])

   if winner(board,"X"):

       gb.destroy()

       box = messagebox.showinfo("Winner","Player 1 won the match")

   elif(isfull()):

       gb.destroy()

       box = messagebox.showinfo("Tie Game","Tie Game")

#Check if the player can push the button or not
def isfree(i,j):
    return board[i][j] == ""

#Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if(i.count('') > 0):
            flag = False
    return flag

#Create the GUI of game board for play along with  another player
def gameboard_pI(game_board,I1,I2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text,i,j,game_board,I1,I2)
            button[i][j] = Button(game_board,bd=5,command=get_t,height=4,width=8)
            button[i][j].grid(row=m,column=n)
    game_board.mainloop()

#Decide the next move of system
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '':
                possiblemove.append([i,j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O','X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy,let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0,0],[0,2],[2,0],[2,2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0,len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0,1],[1,0],[1,2],[2,1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0,len(edge)-1)
            return edge[move]

#Configure text on button while playing with system
def get_text_pc(i,j,gb,I1,I2):
    global sign
    if board[i][j] == '':
        if sign % 2 == 0:
            I1.config(state=DISABLED)
            I2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            I2.config(state=DISABLED)
            I1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board,"X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner","Player won the match")
    elif winner(board,"O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner","Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game","Tie Game")
    if(x):
        if sign % 2!= 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0],move[1],gb,I1,I2)

#Create the GUI of game board for play along with system
def gameboard_pc(game_board,I1,I2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc,i,j,game_board,I1,I2)
            button[i][j] = Button(game_board,bd=5,command=get_t,height=4,width=8)
            button[i][j].grid(row=m,column=n)
    game_board.mainloop()

#Initialize the game board to play with system
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    I1 = Button(game_board,text="Player : X",width=10)
    I1.grid(row=1,column=1)
    I2 = Button(game_board,iext="Computer:O",width=10,state=DISABLED)
    I2.grid(row=2,column=1)
    gameboard_pc(game_board,I1,I2)

#Initialize the game board to play with another player
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    I1 = Button(game_board,text="Player 1 : X",width=10)
    I1.grid(row=1,column=1)
    I2 = Button(game_board,text="Player 2 : O",width=10,state=DISABLED)
    I2.grid(row=2,column=1)
    gameboard_pI(game_board,I1,I2)

def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc,menu)
    wpc = partial(withplayer,menu)
    head = Button(menu,text="---Welcome to tic-tac-toe---",activeforeground='red',activebackground="yellow",bg="red",fg='yellow',width=500,font='summer',bd=5)
    B1 = Button(menu, text="Single Player", command=wpc, activeforeground='red', activebackground="yellow", bg="red",fg="yellow",width=500,font='summer', bd = 5)
    B2 = Button(menu,text="Multi Player",command=wpc,activeforeground='red',activebackground="yellow",bg="red",fg="yellow",width=500,font='summer',bd=5)
    B3 = Button(menu,text="Exit",command=menu.quit,activeforeground='red',activebackground="yellow",bg="red",fg="yellow",width=500,font='summer',bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()

#Call main function
if __name__ == '__main__':
    play()





