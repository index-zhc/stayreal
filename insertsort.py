# 插入排序

def insert(value):
    # 外部循环: 对应遍历所有无序数据
    for i in range(1, len(value)):
        # 备份当前取出数据
        temp = value[i]
        # 插入数据的下标值
        pos = i
        # 内部循环: 对应遍历所有有序数据,找到插入位置
        # -> 从后向前遍历
        # -> 从当前无序数据(i)的前一个位置开始
        # -> 遍历到下标为0为止
        for j in range(i-1, -1, -1):
            # 如果当前有序数据比取出数据大
            if value[j] > temp:
                # 则该有序数据后移一位
                value[j+1] = value[j]
                # 对应更新取出数据插入位置
                pos = j
            # 如果当前有序数据比取出数据小/等
            else:
                # 则在该数据后一位置插入取出数据
                pos = j + 1
                # 确认插入位置后,终止遍历
                break
        # 在指定位置插入数据
        value[pos] = temp


values = [23,45,2,67,34,9,86,39,52,73,19,98,27]
print('原始数据:', values)
insert(values)
print('排序后数据:', values)
