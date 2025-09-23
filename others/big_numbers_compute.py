# plus tow big string-styled numbers


class Solution:
    def big_numbers_plus(self, num1: str, num2: str) -> str:
        short_num = num1
        long_num = num2
        if len(num2) < len(num1):
            short_num = num2
            long_num = num1
        len_long_num = len(long_num)
        len_short_num = len(short_num)

        len_diff = len_long_num - len_short_num
        additional_one = 0
        result = []
        for index in range(len_short_num - 1, -1, -1):
            short_num_char = short_num[index]
            long_num_char = long_num[index + len_diff]
            sum_chars = int(short_num_char) + int(long_num_char) + additional_one
            additional_one = 0
            cur_char = ""
            if sum_chars >= 10:
                additional_one = 1
                cur_char = str(sum_chars - 10)
            else:
                cur_char = str(sum_chars)
            result.append(cur_char)

        for index in range(len_diff - 1, -1, -1):
            sum_chars = int(long_num[index]) + additional_one
            additional_one = 0
            cur_char = ""
            if sum_chars >= 10:
                additional_one = 1
                cur_char = str(sum_chars - 10)
            else:
                cur_char = str(sum_chars)
            result.append(cur_char)

        if additional_one == 1:
            result.append("1")
            additional_one = 0

        result.reverse()
        return "".join(result)
