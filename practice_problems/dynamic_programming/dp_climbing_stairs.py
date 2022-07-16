class Solution:
    def climbStairs(self, n: int) -> int:
        climb = [0, 1, 2]
        for i in range(3, n+1):
            climb.append(climb[i-1] + climb[i-2])
        return climb[n]


if __name__ == '__main__':
    n = 6
    s = Solution()
    total = s.climbStairs(n)
    print(total)
