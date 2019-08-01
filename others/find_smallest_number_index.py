"""
有这样一个正整数数组，它是由一个有序正整数数组改造而成，数组中没有重复数字，改造方法如下:

1. 从某个位置起，截取其后的全部数组
2. 将截取的内容放到数组的头部，拼接到数组的头部

改造示例: [1,2,3,4,5,6,7,8,9,10,11] -> 
[5,6,7,8,9,10,11,1,2,3,4]
[9,10,11,1,2,3,4,5,6,7,8]

问题: 给定这样一个数组，找出其中最小数字的索引值？

in: int[]
out: int

"""


def find(intArray):
    left = 0
    right = len(intArray) - 1

    while True:
        mid_index = int((left + right) / 2)
        mid_value = intArray[mid_index]
        
        if mid_index == left:
            return mid_index + 1
        
        right_value = intArray[right]
        if mid_value > right_value:
            left = mid_index
        else:
            right = mid_index


a = [5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4]
print(find(a))
b = [9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8]
print(find(b))
c = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
print(find(c))
