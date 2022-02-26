
import tkinter
import random
root=tkinter.Tk()
root.title("将棋")
cvs=tkinter.Canvas(width=765,height=940,bg="orange")
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

ToKin=11
NariKyo=12
NariKei=13
NariGin=14
Uma=16
Ryu=17

ToKinAite=-11
NariKyoAite=-12
NariKeiAite=-13
NariGinAite=-14
UmaAite=-16
RyuAite=-17

#表示位置Y
HyoujiY=110

#前の位置
OldClickX=0
OldClickY=0

ugokuclick=0

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

"""
board=[
    [-2,-3,-4,-5,-8,-5,-4,-3,-2],
    [0,-7,0,0,0,0,0,-6,0],
    [-1,-1,-1,-17,-16,-14,-13,-12,-11],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [1,1,1,17,16,14,13,12,11],
    [0,6,0,0,0,0,0,7,0],
    [2,3,4,5,8,5,4,3,2],
]
"""

def bamenn():
    global x,y
    cvs.delete("all")
    
    cvs.create_oval(235,345,245,355,fill="black")
    cvs.create_oval(475,345,485,355,fill="black")
    cvs.create_oval(235,585,245,595,fill="black")
    cvs.create_oval(475,585,485,595,fill="black")
    # 初期盤面
    for y in range(9):
        for x in range(9):
            X=x*80
            Y=y*80+HyoujiY
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

            if board[y][x]==ToKin:
                cvs.create_text(X+40,Y+40,text="と",font=("Times New Roman",40))
            if board[y][x]==NariKyo:
                cvs.create_text(X+40,Y+40,text="成香",font=("Times New Roman",22))
            if board[y][x]==NariKei:
                cvs.create_text(X+40,Y+40,text="成桂",font=("Times New Roman",22))
            if board[y][x]==NariGin:
                cvs.create_text(X+40,Y+40,text="成銀",font=("Times New Roman",22))
            if board[y][x]==Ryu:
                cvs.create_text(X+40,Y+40,text="龍",font=("Times New Roman",40))
            if board[y][x]==Uma:
                cvs.create_text(X+40,Y+40,text="馬",font=("Times New Roman",40))

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

            if board[y][x]==ToKinAite:
                cvs.create_text(X+40,Y+40,text="と",font=("Times New Roman",40),angle=180)
            if board[y][x]==NariKyoAite:
                cvs.create_text(X+40,Y+40,text="成香",font=("Times New Roman",22),angle=180)
            if board[y][x]==NariKeiAite:
                cvs.create_text(X+40,Y+40,text="成桂",font=("Times New Roman",22),angle=180)
            if board[y][x]==NariGinAite:
                cvs.create_text(X+40,Y+40,text="成銀",font=("Times New Roman",22),angle=180)
            if board[y][x]==RyuAite:
                cvs.create_text(X+40,Y+40,text="龍",font=("Times New Roman",40),angle=180)
            if board[y][x]==UmaAite:
                cvs.create_text(X+40,Y+40,text="馬",font=("Times New Roman",40),angle=180)

    # 列
    cvs.create_text(680,90,text="1",font=("Times New Roman",30))
    cvs.create_text(600,90,text="2",font=("Times New Roman",30))
    cvs.create_text(520,90,text="3",font=("Times New Roman",30))
    cvs.create_text(440,90,text="4",font=("Times New Roman",30))
    cvs.create_text(360,90,text="5",font=("Times New Roman",30))
    cvs.create_text(280,90,text="6",font=("Times New Roman",30))
    cvs.create_text(200,90,text="7",font=("Times New Roman",30))
    cvs.create_text(120,90,text="8",font=("Times New Roman",30))
    cvs.create_text(40,90,text="9",font=("Times New Roman",30))
    # 行
    cvs.create_text(740,150,text="一",font=("Times New Roman",30))
    cvs.create_text(740,230,text="二",font=("Times New Roman",30))
    cvs.create_text(740,310,text="三",font=("Times New Roman",30))
    cvs.create_text(740,390,text="四",font=("Times New Roman",30))
    cvs.create_text(740,480,text="五",font=("Times New Roman",30))
    cvs.create_text(740,560,text="六",font=("Times New Roman",30))
    cvs.create_text(740,640,text="七",font=("Times New Roman",30))
    cvs.create_text(740,720,text="八",font=("Times New Roman",30))
    cvs.create_text(740,800,text="九",font=("Times New Roman",30))

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
    global ugokasukoma
    global mx,my,mydash
    global ugokuclick
    global ugokukoma
    mx=int(e.x/80)
    mydash=e.y-HyoujiY
    my=int(mydash/80)
    if mx>8:mx=8
    if my>8:my=8
    if not board[my][mx]==0:
        OldClickX=my
        OldClickY=my
        ugokukoma=board[my][mx]
        if ugokuclick==0:
            ugokuclick=100
        else:
            ugokuclick=0
    
        if ugokukoma==1:
            if ugokuclick==100:
                board[my][mx]=11
                bamenn()
        if ugokukoma==11:
            board[my][mx]=-1
            bamenn()
        if ugokukoma==-1: 
            board[my][mx]=1
            bamenn()
 #   if board[my][my]==0:


    """
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
    """



root.bind("<Button>",click)
cvs.pack()
root.mainloop()

