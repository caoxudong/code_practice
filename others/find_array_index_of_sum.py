"""
题目：给定一个整数数组和一个整数，返回两个数组的索引，这两个索引指向的数字的加和等于指定的整数。需要最优的算法，分析算法的空间和时间复杂度
"""

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9]
    n = 10

    index_map = {}
    supplment_map = {}
    index = 0
    for i in numbers:
        index_map[i] = index
        supplment_map[i] = n - i
        index = index + 1

    result = []
    for k,v in index_map.items():
        suppliment_element = supplment_map.get(k)
        if suppliment_element is not None:
            supp_index = index_map.get(suppliment_element)
            if supp_index is not None:
                result.append((v, supp_index))

    print(result)
