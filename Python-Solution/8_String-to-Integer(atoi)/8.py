class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = len(str)
        ret = 0
        is_valid = False    # 是否无效，
        flag = 1            # 1：正数，-1：负数
        i = 0

        if l == 0:
            return 0

        while i < l and str[i] == ' ':
            i += 1

        if str[i] == '+' or str[i] == '-':
            flag = 1 if str[i] == '+' else -1
            i += 1

        while i < l:
            if '0' <= str[i] <= '9':
                is_valid = True
                ret = ret * 10 + int(str[i])
                i += 1
            else:
                break

        # 检查是否有效、是否负数
        if not is_valid:
            return 0
        elif flag == -1:
            ret = -ret

        # 检查是否溢出
        if ret > 2147483647:
            return 2147483647
        elif ret < -2147483648:
            return -2147483648
        else:
            return ret
        
                    

solution = Solution()
r = solution.myAtoi('   +-123')
print(r)
