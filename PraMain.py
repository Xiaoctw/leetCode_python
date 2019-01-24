import sys
#Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，
# 关键就是要明白这参数是从程序外部输入的，而非代码本身的什么地方，
# 要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数
def main():
    if len(sys.argv)==2 and sys.argv[1] in {"-h","-help"}:
        print("Hello")
a=sys.argv[0]
print(a)
main()
