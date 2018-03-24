
#### 1.给一个递增排序的数组(没有重复)，随机从某个位置截取旋转到前面，查找这个旋转数组的最小值 例如：[1,2,3,4,5,6]->[4,5,6,1,2,3]

```
def search_min(anylist):
    index1 = 0
    index2 = len(anylist) - 1
    indexmid = index1
    while anylist[index1] >= anylist[index2]:
        if index2 - index1 == 1:
            return index2
        indexmid = (index1+index2)//2
        if anylist[indexmid] >= anylist[index1]:
            index1 = indexmid
        elif anylist[indexmid] <= anylist[index2]:
            index2 = indexmid
    return indexmid
```
