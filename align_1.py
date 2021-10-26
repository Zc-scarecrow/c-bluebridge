list = []
for i in range(5):
    num = int(input("请输入第%d个正整数：" % (i+1)) )       # 输入五位正整数
    list.append(num)                      # 将输入的数字插入列表中
list.sort(reverse=False)                   # 由小开始排列函数
print("从小到大排序为");print(list)           # 输出序列
list.sort(reverse=True)                    # 有大开始排列函数
print("从大到小排序为");print(list)           # 输出序列



