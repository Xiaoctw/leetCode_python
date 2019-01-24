def sums_of_powers(*args,power=1):
    result=0
    for arg in args:
        result+=arg**power
    return result
def print_args(*args,**kwargs):#这个函数很是灵活
    for i,arg in enumerate(args):
        print("positional arguments {0}={1}".format(i,arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key,kwargs[key]))
sum=sums_of_powers(1,2,3,4,5,6)
print(sum)
sum1=sums_of_powers(1,2,3,4,5,6,power=4)#如果改变默认参数值，必须带上power=多少
print(sum1)
print_args(1,2,3,4,5,中国="China",日本="Japan",美国="America")