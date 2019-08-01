# tow big string-styled numbers, plus, minus, miltiply and divide


def plus(num1, num2):
    num1Len = len(num1)
    num2Len = len(num2)

    minLen = min(num1Len, num2Len)

    cf = False
    result = []
    for i in range(minLen):
        temp = int(num1[num1Len - i - 1]) + int(num2[num2Len - i - 1])
        if cf:
            temp = temp + 1
            cf = False
        if temp >= 10:
            cf = True
            result.append(str(temp - 10))
        else:
            cf = False
            result.append(str(temp))

    if (i + 1) == num1Len:
        for j in range(num2Len - 1 - i):
            temp = int(num2[num2Len - 1 - i - j - 1])
            if cf:
                temp = temp + 1
                cf = False
            if temp >= 10:
                cf = True
                result.append(str(temp - 10))
            else:
                cf = False
                result.append(str(temp))

    if (i + 1) == num2Len:
        for j in range(num1Len - 1 - i):
            temp = int(num1[num1Len - 1 - i - j - 1])
            if cf:
                temp = temp + 1
                cf = False
            if temp >= 10:
                cf = True
                result.append(str(temp - 10))
            else:
                cf = False
                result.append(str(temp))

    result.reverse()
    return "".join(result)


def minus(num1, num2):
    pass


def multi(num1, num2):
    pass


def divide(num1, num2):
    pass



num1 = "910111213"
num2 = "234567891011121314"
print(plus(num1, num2))