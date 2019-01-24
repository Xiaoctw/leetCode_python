import random
def get_int(msg,minimum,default):
    while True:
        try:
            line=input(msg)
            if not line and default is not None:#如果没有输入的话，而且存在默认值，就返回默认值
                return default
            i=int(line)
            if i<minimum:
                print("must be >=",minimum)
            else:
                return i#如果无法正确输入，那么循环将一直进行下去，不会停止
        except ValueError as Err:
            print(Err)
rows=get_int("rows:",1,None)
columns=get_int("columns:",1,None)
minimun=get_int("minimun(or Enter for 0):",-10000,0)
default=1000
if default<minimun:
    default=2*minimun
maximun=get_int("maximun(or Enter for"+str(default)+"):",minimun,default)
row=0
while row<rows:
    line=""
    column=0
    while column<columns:
        i=random.randint(minimun,maximun)
        s=str(i)
        while len(s)<10:
            s=" "+s
        line+=s
        column+=1
    print(line)
    row+=1