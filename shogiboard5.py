
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

#円の大きさ
Oval_size=10

#表示位置Y
HyoujiY=140

#前の位置
OUTRANGEVALUE=-1
OldClickX=OUTRANGEVALUE #初期値を範囲外にする
OldClickY=OUTRANGEVALUE #初期値を範囲外にする

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

#王、飛、角、金、銀、桂、香、歩
#持ち駒
motigomalist=[0,0,0,0,0,0,0,0]
motigomalistaite=[0,0,0,0,0,0,0,0]
# motteirukazulist=[0,0,0,0,0,0,0,0]
# motteirukazulistaite=[0,0,0,0,0,0,0,0]

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

def motiKoma(n):
    global Ox,Oy
    count=0
    i=0
    Ox=0*80+40
    Oy=9*80+40+HyoujiY

    if n < 0:
        if abs(n)==(1 or 11):
            count = motigomalist[7]+1
            motigomalist[7]=count
        if abs(n)==(2 or 12):
            count = motigomalist[6]+1
            motigomalist[6]=count
        if abs(n)==(3 or 13):
            count = motigomalist[5]+1
            motigomalist[5]=count    
        if abs(n)==(4 or 14):
            count = motigomalist[4]+1
            motigomalist[4]=count
        if abs(n)==(5 or 15):
            count = motigomalist[3]+1
            motigomalist[3]=count
        if abs(n)==(6 or 16):
            count = motigomalist[2]+1
            motigomalist[2]=count
        if abs(n)==(7 or 17):
            count = motigomalist[1]+1
            motigomalist[1]=count

    if n > 0:
        if abs(n)==(1 or 11):
            count = motigomalistaite[7]+1
            motigomalistaite[7]=count
        if abs(n)==(2 or 12):
            count = motigomalistaite[6]+1
            motigomalistaite[6]=count
        if abs(n)==(3 or 13):
            count = motigomalistaite[5]+1
            motigomalistaite[5]=count    
        if abs(n)==(4 or 14):
            count = motigomalistaite[4]+1
            motigomalistaite[4]=count
        if abs(n)==(5 or 15):
            count = motigomalistaite[3]+1
            motigomalistaite[3]=count
        if abs(n)==(6 or 16):
            count = motigomalistaite[2]+1
            motigomalistaite[2]=count
        if abs(n)==(7 or 17):
            count = motigomalistaite[1]+1
            motigomalistaite[1]=count

def bamenn():
    global x,y
    cvs.delete("all")
    
    cvs.create_oval(235,235+HyoujiY,235+Oval_size,235+HyoujiY+Oval_size,fill="black")
    cvs.create_oval(475,235+HyoujiY,475+Oval_size,235+HyoujiY+Oval_size,fill="black")
    cvs.create_oval(235,475+HyoujiY,235+Oval_size,475+HyoujiY+Oval_size,fill="black")
    cvs.create_oval(475,475+HyoujiY,475+Oval_size,475+HyoujiY+Oval_size,fill="black")
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
    cvs.create_text(680,-20+HyoujiY,text="1",font=("Times New Roman",30))
    cvs.create_text(600,-20+HyoujiY,text="2",font=("Times New Roman",30))
    cvs.create_text(520,-20+HyoujiY,text="3",font=("Times New Roman",30))
    cvs.create_text(440,-20+HyoujiY,text="4",font=("Times New Roman",30))
    cvs.create_text(360,-20+HyoujiY,text="5",font=("Times New Roman",30))
    cvs.create_text(280,-20+HyoujiY,text="6",font=("Times New Roman",30))
    cvs.create_text(200,-20+HyoujiY,text="7",font=("Times New Roman",30))
    cvs.create_text(120,-20+HyoujiY,text="8",font=("Times New Roman",30))
    cvs.create_text(40,-20+HyoujiY,text="9",font=("Times New Roman",30))
    # 行
    cvs.create_text(740,40+HyoujiY,text="一",font=("Times New Roman",30))
    cvs.create_text(740,120+HyoujiY,text="二",font=("Times New Roman",30))
    cvs.create_text(740,200+HyoujiY,text="三",font=("Times New Roman",30))
    cvs.create_text(740,280+HyoujiY,text="四",font=("Times New Roman",30))
    cvs.create_text(740,360+HyoujiY,text="五",font=("Times New Roman",30))
    cvs.create_text(740,440+HyoujiY,text="六",font=("Times New Roman",30))
    cvs.create_text(740,520+HyoujiY,text="七",font=("Times New Roman",30))
    cvs.create_text(740,600+HyoujiY,text="八",font=("Times New Roman",30))
    cvs.create_text(740,680+HyoujiY,text="九",font=("Times New Roman",30))


    Ty=0*80-80+HyoujiY
    Ox=0*80+40
    Oy=9*80+40+HyoujiY

    #持ち駒
    """
    cvs.create_text(Ox,Ty,text="歩",font=("Times New Roman",25,"bold"), angle=180)
    cvs.create_text(Ox+80,Ty,text="香",font=("Times New Roman",25,"bold"),angle=180)
    cvs.create_text(Ox+160,Ty,text="桂",font=("Times New Roman",25,"bold"),angle=180)
    cvs.create_text(Ox+240,Ty,text="銀",font=("Times New Roman",25,"bold"),angle=180)
    cvs.create_text(Ox+320,Ty,text="金",font=("Times New Roman",25,"bold"),angle=180)
    cvs.create_text(Ox+400,Ty,text="角",font=("Times New Roman",25,"bold"),angle=180)
    cvs.create_text(Ox+480,Ty,text="飛",font=("Times New Roman",25,"bold"),angle=180)
    """
    if not motigomalistaite[7]==0:
        cvs.create_text(Ox,Ty,text="歩",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+10*0,Ty-20,text=motigomalistaite[7],font=("Times New Roman",25,"bold"), angle=180)
    if not motigomalistaite[6]==0:
        cvs.create_text(Ox+80,Ty,text="香",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+80,Ty-20,text=motigomalistaite[6],font=("Times New Roman",25,"bold"), angle=180)
    if not motigomalistaite[5]==0:
        cvs.create_text(Ox+160,Ty,text="桂",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+160,Ty-20,text=motigomalistaite[5],font=("Times New Roman",25,"bold"), angle=180)
    if not motigomalistaite[4]==0:
        cvs.create_text(Ox+240,Ty,text="銀",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+240,Ty-20,text=motigomalistaite[4],font=("Times New Roman",25,"bold"), angle=180)
    if not motigomalistaite[3]==0:
        cvs.create_text(Ox+320,Ty,text="金",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+320,Ty-20,text=motigomalistaite[3],font=("Times New Roman",25,"bold"), angle=180)
    if not motigomalistaite[2]==0:
        cvs.create_text(Ox+400,Ty,text="角",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+400,Ty-20,text=motigomalistaite[2],font=("Times New Roman",25,"bold"), angle=180)
    if not motigomalistaite[1]==0:
        cvs.create_text(Ox+480,Ty,text="飛",font=("Times New Roman",25,"bold"), angle=180)
        cvs.create_text(Ox+480,Ty-20,text=motigomalistaite[1],font=("Times New Roman",25,"bold"), angle=180)

    if not motigomalist[7]==0:
        cvs.create_text(Ox,Oy,text="歩",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+10*0,Oy+20,text=motigomalist[7],font=("Times New Roman",25,"bold"))
    if not motigomalist[6]==0:
        cvs.create_text(Ox+80,Oy,text="香",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+80,Oy+20,text=motigomalist[6],font=("Times New Roman",25,"bold"))
    if not motigomalist[5]==0:
        cvs.create_text(Ox+160,Oy,text="桂",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+160,Oy+20,text=motigomalist[5],font=("Times New Roman",25,"bold"))
    if not motigomalist[4]==0:
        cvs.create_text(Ox+240,Oy,text="銀",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+240,Oy+20,text=motigomalist[4],font=("Times New Roman",25,"bold"))
    if not motigomalist[3]==0:
        cvs.create_text(Ox+320,Oy,text="金",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+320,Oy+20,text=motigomalist[3],font=("Times New Roman",25,"bold"))
    if not motigomalist[2]==0:
        cvs.create_text(Ox+400,Oy,text="角",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+400,Oy+20,text=motigomalist[2],font=("Times New Roman",25,"bold"))
    if not motigomalist[1]==0:
        cvs.create_text(Ox+480,Oy,text="飛",font=("Times New Roman",25,"bold"))
        cvs.create_text(Ox+480,Oy+20,text=motigomalist[1],font=("Times New Roman",25,"bold"))

bamenn()

def click(e):
    global ugokerumasuhu
    global ugokasukoma
    global mx,my,mydash
    global ugokuclick
    global ugokukoma
    global OldClickX
    global OldClickY
    global n
    global TottaKoma
    mx=int(e.x/80)
    mydash=e.y-HyoujiY
    my=int(mydash/80)
    if mx>8:mx=8
    if my>8:my=8
    
    if OldClickX==OUTRANGEVALUE: # also Y==OUTRANGEVALUE
        if not board[my][mx]==0:
            OldClickX=mx
            OldClickY=my
            ugokukoma=board[my][mx]
        else:
            OldClickX=OUTRANGEVALUE
            OldClickY=OUTRANGEVALUE
    else:
        if mx==OldClickX and my==OldClickY:
            board[my][mx]=ugokukoma
            board[OldClickY][OldClickX]=0 #空白
            
            for n in range(8):
                if ugokukoma==n:
                    board[my][mx]=ugokukoma+10
                if ugokukoma==n+10:
                    board[my][mx]=(ugokukoma-10)*(-1)
                if ugokukoma==n*(-1): 
                    board[my][mx]=ugokukoma-10
                if ugokukoma==(n+10)*(-1): 
                    board[my][mx]=(ugokukoma+10)*(-1)

        else:
            TottaKoma=board[my][mx]
            #motiKoma(TottaKoma) #とった駒（のみ）を表示
            board[my][mx]=ugokukoma
            board[OldClickY][OldClickX]=0 #空白
        
        OldClickX=OUTRANGEVALUE
        OldClickY=OUTRANGEVALUE

        motiKoma(TottaKoma) #とった駒（のみ）を表示
        bamenn()
 #   if board[my][my]==0:




root.bind("<Button>",click)
cvs.pack()
root.mainloop()

