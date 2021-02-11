"""
閏年年份必須滿足以下兩個條件之一:
(1)能被4整除，但不能被100整除
(2)能被400整除
"""
year = int(input("enter a year number: "))
if(year % 4 == 0 and year % 100 == 0 or year % 400 == 0):
    print(True)
else:
    print(False)
