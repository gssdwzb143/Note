def minlist():
    # print("请输入数组：",end="")
    str = input()
    num = [int(n) for n in str.split()]
    n = len(num)
    addlist = 0
    maxlist = 0
    for i in range(0,n):
        for j in range(i,n):
            addlist = addlist + num[j]
            if (maxlist < addlist):
                maxlist = addlist
        addlist = 0
    # print("最大字段和为："+repr(maxlist))
    return maxlist

minlist()
# print(maxlist,end="")


