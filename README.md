
#### 1.给一个递增排序的数组，随机从某个位置截取一段并移到前面，查找这个数组的最小值 例如：[1,2,3,4,5,6]->[4,5,6,1,2,3]

```
def search_min(anylist):
    list_len = len(anylist)
    if list_len > 0:
        index1 = 0
        index2 = list_len - 1
        indexmid = index1
        while anylist[index1] >= anylist[index2]:
            if index2 - index1 == 1:
                return anylist[index2]
            indexmid = (index1+index2)//2
            if anylist[index1] == anylist[indexmid] == anylist[index2]:
                tmp_min = anylist[index1]
                for i in range(index1+1,list_len-1):
                    if tmp_min > anylist[i]:
                        tmp_min = anylist[i]
                return tmp_min
            if anylist[indexmid] >= anylist[index1]:
                index1 = indexmid
            elif anylist[indexmid] <= anylist[index2]:
                index2 = indexmid
        return anylist[indexmid]
```
