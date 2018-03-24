# algorithm-for-python
Using python to implement various algorithms
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
