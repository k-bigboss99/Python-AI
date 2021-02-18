
# 建立列表
# List 的資料項目不需具有相同類型，類似陣列
list1 = ['Taiwan', 'USA', 'JAPAN']
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
print("list1[0]:", list1[0])
print("list2[1:5]", list2[1:5])

# 更新列表
list1 = ['shizu', 1999, 9]
print("value available at index2 : ", list1[2])
list1[2] = 17
print("new value available at index2 : ", list1[2])

# 刪除列表元素
list1 = ['Taiwan', 'USA', 'JAPAN', 'Korea', 'UK']
print(list1)

del list1[2]
print("after delecting value at index 2 : ", list1)

list1.remove('USA')
print("after delecting value 'USA' : ", list1)

list1.pop(0)
print("after delecting value at index 0 : ", list1)

list1.pop()
print("after delecting last element : ", list1)

# 新增清單元素
list1 = ['Taiwan', 'USA', 'JAPAN', 'Korea', 'UK']
list1.append('China')
print(list1)

# 定義多維列表
rows = 3
cols = 6
matrix = [[0 for col in range(cols)] for row in range(rows)]
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = i*3 + j
        print(matrix[i][j], end = ",")
    print("")


# 平方數列表
list1 = []
list1 = [x*x for x in range(0, 10)]
print(list1)

# 元素小寫
list2 = []
list2 = ['Hello', 'WORLD', 'ABC']
list2 = [s.lower() for s in list2]
print(list2)

# 'ABC'與'XYZ'字母組合
list3 = []
list3 = [m+n for m in 'ABC' for n in 'XYZ']
print(list3)

# List -> String
## 包含['',]
nums = [1, 2, 3, 4, 5]
str1 = str(nums) 
print(str1)
## 不包含['',]，可自訂分隔符號
string = ['Taiwan', 'Japan', 'USA']
str2 = "."
str2 = str2.join(string)
print(str2)