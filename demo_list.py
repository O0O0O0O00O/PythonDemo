b=[]
b.append("test")
b.append("apple")
b.append("banana")
for a in b:
    print(a)


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
print("阶乘：", fact(3))

print('__name__是模块名字（文件名），值为：'+__name__)