class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for _ in range(numRows)]  # 相当于生成一个二维数组
        move, counts = 0, 0

        for c in s:
            if move == 0:  # move为0时相当于在走直线，而move为1时相当于是在走斜线
                rows[counts].append(c)
                counts += 1
                if counts == numRows:  # 到达了下线
                    move = 1
                    counts -= 2
            else:
                rows[counts].append(c)
                counts -= 1
                if counts < 0:
                    move = 0
                    counts += 2
        return ''.join([''.join(r) for r in rows])  # 十分巧妙地连接方法
