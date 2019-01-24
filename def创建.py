def append_if_even(x,lst=[]):
    if x%2==0:
        lst.append(x)
    return x
def append_if_even(x,lst=None):#惯用法：有一个默认的None，并创建一个对象
    if lst==None:
        lst=[]
    if x%2==0:
        lst.append(x)
    return x
def documents():
    """这是一个文档信息

    这是文档信息内容
    """
lst=[]
lst=append_if_even(4)
lst=append_if_even(6)
print(lst)