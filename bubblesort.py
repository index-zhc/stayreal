# 冒泡排序

def bubble(value):
    # 外层循环: 对应走访数据的次数:长度-1
    for i in range(len(value) - 1):
        # 设置数据交互标识
        flag = False
        # 内层循环: 对应每次走访数据时
        # 相邻数据对比的次数
        # -1: 对应j+1元素所占位置
        # -i: 对应当前已经找出最大值的个数(外层循环)
        for j in range(len(value)-1 - i):
            # 默然从小到大排序,如前者大于后者则数据交互
            if value[j] > value[j+1]:
                # 进行数据交互
                value[j], value[j+1] = value[j+1], value[j]
                flag = True
        # 若未发生数据交互,则证明后续数据均为有序数据
        # 无需继续遍历,退出循环
        if flag == False:
            break    

    print('遍历次数:', i+1)


values = [23,45,2,67,34,9,86,39,52,73,19,98,27]
print('原始数据:', values)
bubble(values)
print("排序后:", values)
values = [100, 200, 2, 9, 19, 23, 27, 34, 39, 45, 52, 67, 73, 86, 98]
bubble(values)
print("再次排序后:", values)
