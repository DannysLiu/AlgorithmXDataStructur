
#### 1.给一个排序的数组，随机从某个位置截取旋转到前面，查找这个旋转数组的最小值 例如：[1,2,3,4,5,6]->[4,5,6,1,2,3]
```def xx(xxl):
    index1 = 0
    index2 = len(xxl) - 1
    indexmid = index1
    while xxl[index1] >= xxl[index2]:
        if index2 - index1 == 1:
            return index2
        indexmid = (index1+index2)//2
        if xxl[indexmid] >= xxl[index1]:
            index1 = indexmid
        elif xxl[indexmid] <= xxl[index2]:
            index2 = indexmid
    return indexmid
```
