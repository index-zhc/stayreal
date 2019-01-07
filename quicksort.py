# 快速排序


def quick(value):
    # 递归退出条件
    # 当仅有一个数据时,无需排序
    if len(value) < 2:
        return value
    # 设置关键数据
    mark = value[0]
    # 所有比关键数据小的
    smaller = [x for x in value if x < mark]
    # 所有与关键数据相同的
    equal = [x for x in value if x == mark]
    # 所有比关键数据大的
    bigger = [x for x in value if x > mark]
    # 从小到大排序
    return quick(smaller) + equal + quick(bigger)


values = [23,45,2,67,34,9,86,39,52,73,19,98,27]
print('原始数据:', values)
values = quick(values)
print('排序后数据:', values)
