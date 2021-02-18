# dict是一種課變容器模型，且可儲存任意類型物件，由(key->value)組成
## 不允許同一個key出現兩次以上，建立時若同一個key被設定兩次，後值會覆蓋前值
## key不可變，可用數字、字串、元組，但不可用列表
## 字典是無序的，元素沒有順序之分(不須透過位置尋找元素)，所以在儲存元素時保持最佳化

# 建立字典
dict = {'name':'shizu', 'age':22,'sex':'male'}
print("dict['name']: ", dict['name'])

# 修改字典
dict = {'name':'shizu', 'age':22,'sex':'male'}
dict['name'] = 'charles'
dict['interest'] = 'computergames'
print(dict)

# 刪除字典中的元素
## 刪除字典中的元素(項目)
dict = {'name':'shizu', 'age':22,'sex':'male'}
del dict['sex']
print(dict)
## 清空字典所有元素
dict = {'name':'shizu', 'age':22,'sex':'male'}
dict.clear()
print(dict)

# in運算
dict = {'name':'shizu', 'age':22,'sex':'male'}
ans1 = 'age' in dict
print(ans1)

# 取得字典所有值
dict = {'name':'shizu', 'age':22,'sex':'male'}
print(dict.values())

# items方法
dict = {'name':'shizu', 'age':22,'sex':'male'}
for key, value in dict.items():
    print(key, value)
