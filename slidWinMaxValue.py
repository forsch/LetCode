'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3 (1, 3)
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  1] 3  6  7       5 ()
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import unittest
import collections

class Solution:
    def maxSlidingWindowII(self, nums, k):
        ans = []
        que = collections.deque()
        for i in range(len(nums)):
            # remove out range : append from right pop/popleft/append/appendleft
            while que and que[0] < i - k + 1:
                que.popleft()

            # remove all less than nums[i]
            while que and nums[que[-1]] < nums[i]:
                que.pop()

            # append i
            que.append(i)

            # pick ans
            if i >= k - 1:
                ans.append(nums[que[0]])
        return ans

    def maxSlidingWindow(self, nums, k):
        ans = []
        if not nums:
            return ans

        maxValue = max(nums[0:k])
        ans.append(maxValue)

        for i in range(k, len(nums)):
            if nums[i] > maxValue:
                maxValue = nums[i]
            else:
                maxValue = max(nums[i-k+1:i+1])
            ans.append(maxValue)

        return ans

    def slidingWindowTemplate():
        begin = end = 0

        while f(end):
            # do something
            end += 1

            while g(begin, end):
                # do something
                begin += 1
        
        return


class MaxSlidingWindowTestSuite(unittest.TestCase):
    s = Solution()
    def test_nums_empty(self):
        self.assertEqual(self.s.maxSlidingWindow([],0), [])
    def test_nums_0(self):
        self.assertEqual(self.s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        
    def test_nums_i_0(self):
        self.assertEqual(self.s.maxSlidingWindowII([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
    def test_nums_i_1(self):
        self.assertEqual(self.s.maxSlidingWindowII([7,2,4],2) ,[7,4])
if __name__ == "__main__":
    unittest.main()

            
