# 建立元組
# tuple元組與list列表相似，不同為元組元素不可修改，且元組元素類型可不相同
tup1 = ()
tup1 = ('Taiwan', 'USA', 'JAPAN')
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
print("tup1[0]:", tup1[0])
print("tup2[1:5]:", tup2[1:5])

# 連接元組
## 元組中的元组值不允須修改，但可以對元組進行結合
tup1 = (12, 34, 56)
tup2 = (78, 90)
tup3 = tup1 + tup2
print(tup3)

# 刪除元組
## 元組中的元组值不允須刪除，但可以刪除整個元組
tup1 = ('Taiwan', 'USA', 'JAPAN')
del tup1

# 元組與列表轉換
tup1 = (1, 2, 3, 4, 5)
list1 = list(tup1)
print(list1)

list1 = [1, 3, 5, 7, 9]
tup1 = tuple(list1)
print(tup1)


