#应用try——except——finally处理文件错误
def read_data(filename):
    lines=[]
    fh=None
    try:
        fh=open(filename,"r")
        for line in fh:
            if line.strip():#除去空行，注意字符串是无法改变的，因此这里line没有改变，也就是说结尾还带着换行
                lines.append(line)
    except(IOError,OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines
filename="统计单词noblanks"
lines=read_data(filename)
#print(lines)
fp=open("result1","w")
fp.writelines(lines)