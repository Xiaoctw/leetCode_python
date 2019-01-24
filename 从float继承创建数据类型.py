class FuzzyBool(float):
    def __new__(cls,value=0):
        return super().__new__(cls,value if 0.0<=value<=1.0 else 0.0)
    def __invert__(self):
        return FuzzyBool(1.0-float(self))#没有私有属性，直接使用self，因为FuzzyBool直接从float继承来
    def __and__(self, other):
        return FuzzyBool(min(self,other))
    def __iand__(self, other):
        #待定
        self=min(self,other)
        return self
    def __or__(self, other):
        return FuzzyBool(max(self,other))
    def __ior__(self, other):
        # 待定
        self=max(self,other)
        return self
    def __repr__(self):#repr() 函数将对象转化为供解释器读取的形式。
        return ("{0}{1}".format(self.__class__.__name__,super().__repr__()))
    def __bool__(self):
        return self>0.5
    def __int__(self):
        return round(self)
    def __add__(self, other):
        raise NotImplementedError()#一个标准异常
    def __iadd__(self, other):
        raise NotImplementedError()
    def __radd__(self, other):
        raise NotImplementedError()
    def __neg__(self):
        raise TypeError()#此处省略
    def __eq__(self, other):
        raise NotImplemented


