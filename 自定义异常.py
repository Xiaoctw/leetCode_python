class FoundException(Exception): pass
try:
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if (i,j,k)==(65,45,87):
                    raise FoundException()#构造函数，加上括号,这种方法比break效率高
except FoundException:
    print("找到位置{0}，{1}，{2}".format(i,j,k))


