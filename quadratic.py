import math
import cmath
import sys
def get_float(msg,allow_zero):
    while True:
        x=input(msg)
        if x:
            try:
                x=int(x)
                if not allow_zero and abs(x)<sys.float_info.epsilon:
                    print("Zero is not allowed")
                    x=None
                if x is not None:
                    return x
            except ValueError as Err:
                print(Err)
print("ax\N{SUPERSCRIPT TWO}+bx+c=0")
a=get_float("enter a:",False)
b=get_float("enter b:",True)
c=get_float("enter c:",True)
x1=None
x2=None
discriminant=b**2-4*a*c
if discriminant==0:
    x1=-(b/(2*a))
else:
    if discriminant>0:
        root=math.sqrt(discriminant)
    else:
        root=cmath.sqrt(discriminant)
    x1=(-b+root)/(2*a)
    x2=(-b-root)/(2*a)
equation=("{0}x\N{SUPERSCRIPT TWO}+{1}x+{2}=0""\N{RIGHTWARDS ARROW}x={3}").format(a,b,c,x1)#打印次方的方式
if x2 is not None:
    equation+=" or x={0}".format(x2)
print(equation)