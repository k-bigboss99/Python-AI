# 1-5的平方和
def f(x):
    if x == 4:
        return 1
    else:
        return(f(x-1) + x*x)

ans = f(5)
print(ans)