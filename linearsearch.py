# 顺序查找
def linear(values, key):
    # 遍历原始数据
    for i in range(len(values)):
        if values[i] == key:
            # 查找成功
            return i
    # 查找失败
    return -1

#  原数据
values = [3, 9, 10, 12, 34, 56]
#  待查找的元素值
key = int(input('请输入要查找的数值:'))
result = linear(values, key)
if result == -1:
    # 查找失败
    print('查找失败')
else:
    # 查找成功
    print('查找到该数据,对应下标:', result)
