import tkinter
import random
root=tkinter.Tk()
root.title("将棋")
cvs=tkinter.Canvas(width=720,height=940,bg="orange")
huhyou=1
kyousya=2
kei=3
ginshou=4
kinshou=5
kakugyou=6
hi=7
ousyou=8
huhyouteki=-1
kyousyateki=-2
keiteki=-3
ginshouteki=-4
kinshouteki=-5
kakugyouteki=-6
hiteki=-7
gyoku=-8
ugokuclick=0
kyoumy=0

board=[
    [-2,-3,-4,-5,-8,-5,-4,-3,-2],
    [0,-7,0,0,0,0,0,-6,0],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1],
    [0,6,0,0,0,0,0,7,0],
    [2,3,4,5,8,5,4,3,2],
]

def bamenn():
    global x,y
    cvs.delete("all")
    cvs.create_oval(235,345,245,355,fill="black")
    cvs.create_oval(475,345,485,355,fill="black")
    cvs.create_oval(235,585,245,595,fill="black")
    cvs.create_oval(475,585,485,595,fill="black")
    for y in range(9):
        for x in range(9):
            X=x*80
            Y=y*80+110
            cvs.create_rectangle(X,Y,X+80,Y+80,outline="black")
            if board[y][x]==huhyou:
                cvs.create_text(X+40,Y+40,text="歩",font=("Times New Roman",40))
            if board[y][x]==kyousya:
                cvs.create_text(X+40,Y+40,text="香",font=("Times New Roman",40))
            if board[y][x]==kei:
                cvs.create_text(X+40,Y+40,text="桂",font=("Times New Roman",40))
            if board[y][x]==ginshou:
                cvs.create_text(X+40,Y+40,text="銀",font=("Times New Roman",40))
            if board[y][x]==kinshou:
                cvs.create_text(X+40,Y+40,text="金",font=("Times New Roman",40))
            if board[y][x]==ousyou:
                cvs.create_text(X+40,Y+40,text="王",font=("Times New Roman",40))
            if board[y][x]==hi:
                cvs.create_text(X+40,Y+40,text="飛",font=("Times New Roman",40))
            if board[y][x]==kakugyou:
                cvs.create_text(X+40,Y+40,text="角",font=("Times New Roman",40))

            if board[y][x]==huhyouteki:
                cvs.create_text(X+40,Y+40,text="歩",font=("Times New Roman",40),angle=180)
            if board[y][x]==kyousyateki:
                cvs.create_text(X+40,Y+40,text="香",font=("Times New Roman",40),angle=180)
            if board[y][x]==keiteki:
                cvs.create_text(X+40,Y+40,text="桂",font=("Times New Roman",40),angle=180)
            if board[y][x]==ginshouteki:
                cvs.create_text(X+40,Y+40,text="銀",font=("Times New Roman",40),angle=180)
            if board[y][x]==kinshouteki:
                cvs.create_text(X+40,Y+40,text="金",font=("Times New Roman",40),angle=180)
            if board[y][x]==gyoku:
                cvs.create_text(X+40,Y+40,text="玉",font=("Times New Roman",40),angle=180)
            if board[y][x]==hiteki:
                cvs.create_text(X+40,Y+40,text="飛",font=("Times New Roman",40),angle=180)
            if board[y][x]==kakugyouteki:
                cvs.create_text(X+40,Y+40,text="角",font=("Times New Roman",40),angle=180)
bamenn()


#        susumu=0
#        sx=x
#        sy=y
#        if board[y+1][x]==0:
#            susumu+1
#            sy=1
#            board[sy][sx]=1







def click(e):
    global ugokerumasuhu
    global mx,my
    global kyoumy
    global ugokuclick
    mx=int(e.x/80)
    my=int(e.y/80)
    if mx>8:mx=8
    if my>8:my=8
    humy=my-1
    if ugokuclick==0:ugokuclick=1
    if board[my][mx]==1:
        board[my][mx]=0
        board[humy][mx]=1
        global huhyouugoku
        bamenn()
    if  board[my][mx]==2:
        if ugokuclick==1:
            kyoumy=my
            board[my][mx]=0 
            board[kyoumy][mx]=2
            ugokuclick=0
            bamenn()


    bamenn()


root.bind("<Button>",click)
cvs.pack()
root.mainloop()

