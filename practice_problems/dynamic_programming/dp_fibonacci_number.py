class Solution:
    def fib(self, n: int) -> int:
        fiboo = [0, 1]
        for i in range(2, n + 1):
            fiboo.append(fiboo[i - 1] + fiboo[i - 2])
        return fiboo[n]


if __name__ == '__main__':
    n = 8
    s = Solution()
    total = s.fib(n)
    print(total)
