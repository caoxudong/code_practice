"""
题目：找出数组中出现次数超过一半的数，现在有一个数组，已知一个数出现的次数超过了一半，请用O(n)的复杂度的算法找出这个数。

出题人：阿里巴巴新零售技术质量部
"""

def find_number(arr):
    map = {}
    total = len(arr)
    for i in arr:
        if map.get(i) is None:
            map[i] = 1
        else:
            map[i] = map[i] + 1
    half = total / 2
    for k,v in map.items():
        if map[k] > half:
            return k
    return None

if __name__ == "__main__":
    arr = [1,2,3,2,2,3,2,4,2]
    print(find_number(arr))