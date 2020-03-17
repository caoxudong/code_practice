"""
题目：已知 sqrt (2)约等于 1.414，要求不用数学库，求 sqrt (2)精确到小数点后 10 位。

出题人：——阿里巴巴出题专家：文景／阿里云 CDN 资深技术专家

参考答案：
* 考察点
基础算法的灵活应用能力（二分法学过数据结构的同学都知道，但不一定往这个方向考虑；如果学过数值计算的同学，应该还要能想到牛顿迭代法并解释清楚）
* 退出条件设计

"""

def sqrt2():
    low = 1.4
    hight = 1.5
    accuracy = 0.0000000001
    mid = (hight + low) / 2
    while hight - low > accuracy:
        if mid * mid > 2:
            high = mid
        else:
            low = mid
        mid = (hight + low) / 2
    return mid