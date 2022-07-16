class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0, 1, 1]
        for i in range(3, n+1):
            tribo.append(tribo[i-1] + tribo[i-2] + tribo[i-3])
        return tribo[n]


if __name__ == '__main__':
    n = 5
    s = Solution()
    total = s.tribonacci(n)
    print(total)
