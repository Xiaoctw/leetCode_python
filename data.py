
f=open("hello.txt","w")#打开文件的函数
f.write("Hello world!")
f.close()
fp=open("data.txt","r")
lines=fp.readlines()#包括换行符，读取很多行
print(lines)
fp.close()
count=1
newLines=[]
for line in lines:
    newLines.append(str(count)+" "+line)
    count+=1
fp1=open("data1.txt","w")
fp1.writelines(newLines)#直接写入很多行