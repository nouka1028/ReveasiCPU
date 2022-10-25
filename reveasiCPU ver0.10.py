"""
ゲームの初期化
"""

stone=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
cand=[]
print_list=[]
import random
"""
関数定義
"""

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RETURN = '\033[07m' #反転
    ACCENT = '\033[01m' #強調
    FLASH = '\033[05m' #点滅
    RED_FLASH = '\033[05;41m' #赤背景+点滅
    END = '\033[0m'
    
def putstone(x,y,stone_color):
    #上からx,左からy
    #1が白、2が黒
    global stone
    stone[y-1][x-1]=stone_color

def init():
    global stone
    putstone(4,4,1)
    putstone(4,5,2)
    putstone(5,4,2)
    putstone(5,5,1)
    
def comple_print():
    global print_list
    print_list=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    for i in range(8):
        for j in range(8):
            if stone[i][j]==0:
                print_list[i][j]=" "
            elif stone[i][j]==1:
                print_list[i][j]="○"
            else:
                print_list[i][j]="●"  
    print("  1 2 3 4 5 6 7 8")          
    for i in range(8):
        t=" ".join(print_list[i])
        print(f"{i+1} {t} {i+1}")
    print("  1 2 3 4 5 6 7 8")  
    
def getstonecolor(x,y):
    global stone
    return stone[y-1][x-1]

def search(x,y,x_ch,y_ch,stone_color,another):
    global cand
    try:
        if getstonecolor(x+x_ch,y+y_ch)==another:
            while True:
                x_ch+=(x_ch!=0)*(2*(x_ch>0)-1)
                y_ch+=(y_ch!=0)*(2*(y_ch>0)-1)
                x_inp=x+x_ch
                y_inp=y+y_ch
                if 0<(x_inp)<9 and 0<(y_inp)<9:
                    if getstonecolor(x_inp,y_inp)==0:
                        if ([x_inp,y_inp] in cand)==False:
                            cand.append([x_inp,y_inp])
                        break
                    elif getstonecolor(x_inp,y_inp)==stone_color:
                        break
                else:
                    break
    except:
        pass
def make_cand(stone_color):
    if stone_color==1:
        another=2
    else:
        another=1
    global cand
    cand=[]
    #横がi,縦がj
    #8方向を探索
    for i in range(1,9):
        for j in range(1,9):
            
            if getstonecolor(i,j)==stone_color:
                #上方向を探索
                search(i,j,0,-1,stone_color,another)
                #右上方向を探索
                search(i,j,1,-1,stone_color,another)
                #右方向を探索
                search(i,j,1,0,stone_color,another)
                #右下方向を探索
                search(i,j,1,1,stone_color,another)
                #下方向を探索
                search(i,j,0,1,stone_color,another)
                #左下方向を探索
                search(i,j,-1,1,stone_color,another)
                #左方向を探索
                search(i,j,-1,0,stone_color,another)
                #左上方向を探索
                search(i,j,-1,-1,stone_color,another)
                
def put(x,y,x_ch,y_ch,stone_color,another):
    global stone
    flag=False
    try:
        if getstonecolor(x+x_ch,y+y_ch)==another:
            while True:
                x_ch+=(x_ch!=0)*(2*(x_ch>0)-1)
                y_ch+=(y_ch!=0)*(2*(y_ch>0)-1)
                x_inp=x+x_ch
                y_inp=y+y_ch
                if 0<(x_inp)<9 and 0<(y_inp)<9:
                    if getstonecolor(x_inp,y_inp)==stone_color:
                        flag=True
                        break
                    elif getstonecolor(x_inp,y_inp)==0:
                        break
                else:
                    break
    except:
        pass
    if flag:
        x_ch=(x_ch!=0)*(2*(x_ch>0)-1)
        y_ch=(y_ch!=0)*(2*(y_ch>0)-1)
        while True:
                x_inp=x+x_ch
                y_inp=y+y_ch
                if 0<(x_inp)<9 and 0<(y_inp)<9:
                        if getstonecolor(x_inp,y_inp)==stone_color:
                            break
                        elif getstonecolor(x_inp,y_inp)==0:
                            break
                        else:
                            putstone(x_inp,y_inp,stone_color)
                else:
                    break
                x_ch+=(x_ch!=0)*(2*(x_ch>0)-1)
                y_ch+=(y_ch!=0)*(2*(y_ch>0)-1)
                
        
                
def turn_stone(i,j,stone_color):
    global stone
    if stone_color==1:
        another=2
    else:
        another=1
    #上方向を探索
    put(i,j,0,-1,stone_color,another)
    #右上方向を探索
    put(i,j,1,-1,stone_color,another)
    #右方向を探索
    put(i,j,1,0,stone_color,another)
    #右下方向を探索
    put(i,j,1,1,stone_color,another)
    #下方向を探索
    put(i,j,0,1,stone_color,another)
    #左下方向を探索
    put(i,j,-1,1,stone_color,another)
    #左方向を探索
    put(i,j,-1,0,stone_color,another)
    #左上方向を探索
    put(i,j,-1,-1,stone_color,another)
    putstone(i,j,stone_color)
    
def cnt_put(x,y,x_ch,y_ch,stone_color,another):
    global stone
    global cnt
    flag=False
    t=0
    try:
        if getstonecolor(x+x_ch,y+y_ch)==another:
            while True:
                x_ch+=(x_ch!=0)*(2*(x_ch>0)-1)
                y_ch+=(y_ch!=0)*(2*(y_ch>0)-1)
                x_inp=x+x_ch
                y_inp=y+y_ch
                if 0<(x_inp)<9 and 0<(y_inp)<9:
                    if getstonecolor(x_inp,y_inp)==stone_color:
                        flag=True
                        break
                    elif getstonecolor(x_inp,y_inp)==0:
                        break
                else:
                    break
    except:
        pass
    if flag:
        x_ch=(x_ch!=0)*(2*(x_ch>0)-1)
        y_ch=(y_ch!=0)*(2*(y_ch>0)-1)
        t=0
        while True:
                x_inp=x+x_ch
                y_inp=y+y_ch
                if 0<(x_inp)<9 and 0<(y_inp)<9:
                        if getstonecolor(x_inp,y_inp)==stone_color:
                            break
                        elif getstonecolor(x_inp,y_inp)==0:
                            break
                        else:
                            t+=1
                else:
                    break
                x_ch+=(x_ch!=0)*(2*(x_ch>0)-1)
                y_ch+=(y_ch!=0)*(2*(y_ch>0)-1)    
    cnt+=t
cnt=0
def turn_stone_num(i,j,stone_color):
    global stone
    global cnt
    if stone_color==1:
        another=2
    else:
        another=1
    cnt=0
    #上方向を探索
    cnt_put(i,j,0,-1,stone_color,another)
    #右上方向を探索
    cnt_put(i,j,1,-1,stone_color,another)
    #右方向を探索
    cnt_put(i,j,1,0,stone_color,another)
    #右下方向を探索
    cnt_put(i,j,1,1,stone_color,another)
    #下方向を探索
    cnt_put(i,j,0,1,stone_color,another)
    #左下方向を探索
    cnt_put(i,j,-1,1,stone_color,another)
    #左方向を探索
    cnt_put(i,j,-1,0,stone_color,another)
    #左上方向を探索
    cnt_put(i,j,-1,-1,stone_color,another)
    cnt+=1
    return cnt
rslt=[]
def think_put_stone():
    global cand
    global rslt
    rslt=[]
    max_cand=[0,0,0]
    for i in cand:
        x=i[0];y=i[1]
        point=turn_stone_num(x,y,2)
        g=max(abs(x-4.5),abs(y-4.5))
        if g==3.5:
            if max_cand[2]<=1.25*point:
                max_cand=[x,y,1.25*point]
        elif g==2.5:
            if max_cand[2]<=0.5*point:
                max_cand=[x,y,0.5*point]
        else:
            if max_cand[2]<=point:
                max_cand=[x,y,point]
    print(max_cand[2])
    rslt=max_cand[:2]


"""
ゲーム実行
1がでたら自分、2が出たらCPUが最初
"""  
init()         
comple_print() 
order=random.randint(1,2)
passed=0
while True:
    if order==1:
        order_tmp=1
        order=2
    else:
        order_tmp=2
        order=1
    make_cand(order)
    if order==1:
        print(pycolor.BLUE)
        print(f"You can put {cand}")
    else:
        print(pycolor.GREEN)
        print(f"CPU can put {cand}")
    if cand!=[]:
        passed=0
        while True:
            if order==1:
                try:
                    x,y=map(int,input(">>>").split())
                    if [x,y] in cand:
                        break
                    else:
                        print("error:not in cand")
                except:
                    print("error:Syntax error")
            else:
                think_put_stone()
                x=rslt[0]
                y=rslt[1]
                print(f"CPU put in {[x,y]}")
                break
        turn_stone(x,y,order)
        comple_print()
    else:
        print("pass")
        passed+=1
        if passed==2:
            break
#ゲームエンド
me=0
cpu=0
for j in range(8):
    me+=stone[j].count(1)
    cpu+=stone[j].count(2)
print(f"Me:{me} CPU:{cpu}")
if me>cpu:
    print("You win")
elif me==cpu:
    print("Draw")
else:
    print("You lose")
        