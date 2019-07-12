reponses ={}
flag =True
while flag:
    name = input("请输入姓名： ")
    reponse = input("请输入回答：")
    reponses[name] = reponse #添加进字典
    isGoingOn =input("停止请输入：no，继续请输入任意字符: ")
    if isGoingOn=="no":
        flag=False
print(reponses)
