# from typing import List
#
#
# class Solution:
#     def checkCost(self, cost, i):
#         total_cost = 0
#         while i < len(cost):
#             total_cost += cost[i]
#             try:
#                 cost[i+1] and cost[i+2]
#             except IndexError:
#                 return total_cost
#             if cost[i+1] < cost[i+2]:
#                 i += 1
#             else:
#                 i += 2
#         return total_cost
#
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         return min(self.checkCost(cost, 0), self.checkCost(cost, 1))
#
#
# if __name__ == '__main__':
#     cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#     s = Solution()
#     total = s.minCostClimbingStairs(cost)
#     print(total)



from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = 1
        total_cost = 0
        # for i in range(0, len(cost)):
        #     if i+1 < i+2:
        #         j = i +1
        while i < len(cost):
            total_cost += cost[i]
            try:
                cost[i+1]
            except IndexError:
                return total_cost
            try:
                cost[i + 2]
            except IndexError:
                return total_cost
            if cost[i+1] < cost[i+2]:
                i += 1
            else:
                i += 2
        return total_cost


if __name__ == '__main__':
    cost = [10,15,20]
    s = Solution()
    total = s.minCostClimbingStairs(cost)
    print(total)
