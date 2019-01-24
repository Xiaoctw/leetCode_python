import collections
Sales=collections.namedtuple("Sales","productid customerid date quantity price")
sales=[]
sales.append(Sales("001", 1, "2017-4-2", "good", 500))
sales.append(Sales("002",2,"2017-4-5","well",400))
total=0
for sale in sales:
    total+=sale.price**2
#print("{0.productid} and {1.productid} total prices are {3}".format(sales[0],sales[1],total))
print("{0.productid} and {1.productid} total prices are {2}".format(sales[0],sales[1],total))
