# 二分查找
# 递归实现
def binary(values, key, left, right):
    # 查找失败,递归提出条件
    if left > right:
        return -1 

    # 获取中间元素
    middle = (left + right) // 2
    if values[middle] == key:
        # 查找成功
        return middle
    elif values[middle] > key:
        # 如果中间值大于key值时
        # 继续在左侧子表中查找
        return binary(values, key, left, middle-1)
    else:
        # 如果中间值小于key值时
        # 继续在右侧子表中查找
        return binary(values, key, middle+1, right)


# 原始数据
values = [3, 9, 10, 12, 25, 34, 45, 56, 67, 76, 84, 99]
# 待查找的数据
key = int(input('请输入要查找的数据:'))
result = binary(values, key, 0, len(values)-1)
if result == -1:
    print("查找失败")
else:
    print('找到该数据,对应下标:', result)
