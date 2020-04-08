"""
1   2   6   7  15 16 28 29 45 46 66 ...
3   5   8   14 17 27 30 44 47 65 ...
4   9   13  18 26 31 43 48 64 ...
10 12   19  25 32 42 49 63 ...
11 20   24  33 41 50 62 ...
21 23   34  40 51 61 ...
22 35   39  52 60 ...
36 38   53  59 ...
37 54   58  ...
55 57   ...
56 ...

假设有上面这样一个数组，行和列可以无限扩展，求索引值[i,j]的数字
"""

def compute(i: int, j:int) -> int:
    """
    arr[0,j] = 1 + 4 * ((j / 2) * (j / 2 + 1) / 2) + (j + 1) / 2
    arr[i,j] = arr[0,i+j] + (+-i)
    """
    sum_ij = i + j
    arrIPlusJ = compute_line(sum_ij)
    delta = 0
    if sum_ij & 1 == 0:
        delta = -i
    else:
        delta = i
    return arrIPlusJ + delta

def compute_line(j:int) -> int:
    return 1 + 4 * ((j // 2) * (j // 2 + 1) / 2) + (j + 1) // 2


if __name__ == "__main__":
    test_params = [
        [0,0,1],
        [8,0,37],
        [0,8,45],
        [5,1,23],
        [5,5,61],
    ]
    for params in test_params:
        print(params[0],params[1],compute(params[0],params[1]),params[2])