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

def edge_rating(x,y,x_ch,y_ch,stone_color):
    global stone
    tmp=0
    if stone_color==1:
        another=2
    else:
        another=1
    #x,yの座標を端に設定
    #縦リスト
    xlist=[getstonecolor(x,y),getstonecolor(x+x_ch,y),getstonecolor(x+2*x_ch,y)]
    #斜めリスト
    xylist=[getstonecolor(x,y),getstonecolor(x+x_ch,y+y_ch),getstonecolor(x+2*x_ch,y+2*y_ch)]
    #縦リスト
    ylist=[getstonecolor(x,y),getstonecolor(x,y+2*y_ch),getstonecolor(x,y+2*y_ch)]
    if xlist[0]==stone_color:
        if xlist[1]==stone_color:
            if xlist[2]==stone_color:
                tmp+=20
            elif xlist[2]==another:
                tmp+=15
        else:
            if xlist[2]==stone_color:
                tmp+=14
            elif xlist[2]==another:
                tmp+=13
    else:
        if xlist[1]==stone_color:
            if xlist[2]==stone_color:
                tmp+=-15
            elif xlist[2]==another:
                tmp+=-14
        else:
            if xlist[2]==stone_color:
                tmp+=-15
            elif xlist[2]==another:
                tmp+=-20
    if ylist[0]==stone_color:
        if ylist[1]==stone_color:
            if ylist[2]==stone_color:
                tmp+=20
            elif ylist[2]==another:
                tmp+=15
        else:
            if ylist[2]==stone_color:
                tmp+=14
            elif ylist[2]==another:
                tmp+=13
    else:
        if ylist[1]==stone_color:
            if ylist[2]==stone_color:
                tmp+=-15
            elif ylist[2]==another:
                tmp+=-14
        else:
            if ylist[2]==stone_color:
                tmp+=-15
            elif ylist[2]==another:
                tmp+=-20
    if xylist[0]==stone_color:
        if xylist[1]==stone_color:
            if xylist[2]==stone_color:
                tmp+=20
            elif xylist[2]==another:
                tmp+=15
        else:
            if xylist[2]==stone_color:
                tmp+=14
            elif xylist[2]==another:
                tmp+=13
    else:
        if xylist[1]==stone_color:
            if xylist[2]==stone_color:
                tmp+=-15
            elif xylist[2]==another:
                tmp+=-14
        else:
            if xylist[2]==stone_color:
                tmp+=-15
            elif xylist[2]==another:
                tmp+=-20
    return tmp
    
    


def eval_func(stone_color):
    score=0
    if stone_color==1:
        another=2
    else:
        another=1
    #端っこの石の配置を探索
    me=0;cpu=0
    score=edge_rating(1,1,1,1,stone_color)+edge_rating(8,1,-1,1,stone_color)+edge_rating(8,8,-1,-1,stone_color)+edge_rating(1,8,1,-1,stone_color)

    for i in range(8):
        for j in range(8):
            t=max(abs(i-4.5),abs(j-4.5))
            if t==3.5:
                if getstonecolor(i,j)==stone_color:
                    score+=1.5
                elif getstonecolor(i,j)==another:
                    score+=-1.5
            elif t==2.5:
                if getstonecolor(i,j)==stone_color:
                    score+=0.5
                elif getstonecolor(i,j)==another:
                    score+=-0.5
            else:
                if getstonecolor(i,j)==stone_color:
                    score+=1
                elif getstonecolor(i,j)==another:
                    score+=-1
    
    return score
                
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
    

rslt=[]
def think_put_stone():
    global cand
    global rslt
    global stone
    global stoneCopy
    rslt=[]
    max_cand=[0,0,-1000000]
    for i in cand:
        x=i[0];y=i[1]
        temp=[]
        for i in stone:
            temp.append(i[:])
        turn_stone(x,y,2)
        point=eval_func(2)
        if point>max_cand[2]:
            max_cand=[x,y,point]
        stone=[]
        for i in temp:
            stone.append(i[:])
            
        
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
                #元々のstoneのリストを格納
                temp=[]
                for i in stone:
                    temp.append(i[:])
                think_put_stone()
                stone=[]
                for i in temp:
                    stone.append(i[:])
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
        