class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_n = len(nums)
        if l_n < 1:
            return 0
        nums = [1] + nums + [1]
        l_n = len(nums)
        dp = [[-1 for i in range(l_n)] for i in range(l_n)]

        def max_score(left, right):
            if dp[left][right] != -1:
                return dp[left][right]
            if right - left < 2:
                dp[left][right] = 0
                return  dp[left][right]
            for k in range(left+1, right):
                dp[left][right] = max(dp[left][right], nums[left]*nums[k]*nums[right] + max_score(left,k) + max_score(k,right))
            return dp[left][right]

        return max_score(0, l_n-1)

s = Solution()
print(s.maxCoins([9,76,64,21,97,60,5]))
print()
print(s.maxCoins([3,1,5,8]))
