#列表内涵，列表内涵会生成列表
leaps=[year for year in range(0,2000) if ((year%4==0 and year %100 !=0) or year %400==0)]
print(leaps)
#接下来地两种方法等价
codes=[]
for sex in "MF":
    for size in "SMLX":
        if sex=="F" and size=="X":
            continue
        for color in "BGW":
            codes.append(sex+size+color)
codes1=[sex+size+color for sex in "MF" for size in "SMLX" for color in "BGW" if not (sex=="F" and size=="X")]
print(codes)
print(codes1)
