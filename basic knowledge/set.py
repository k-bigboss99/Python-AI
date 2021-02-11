# 集合是無序且不重複的序列
# 建立集合
## ps.建立空集合必須使用set()，而非{}
students = {'Amir', 'Shizu', 'Tye'}
print(students)

# 成員測試
students = {'Amir', 'Shizu', 'Tye'}
if('Amir' in students):
    print(True)
else:
    print(False)

# 集合運算
set1 = set('abcd')
set2 = set('cdef')
print(set1, set2)
print("set1 - set2: ", set1 - set2)
print("set1 + set2: ", set1 | set2)
print("set1 & set2: ", set1 & set2)
print("set1、set2 不同時存在: ", set1 ^ set2)