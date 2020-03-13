'''
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

提示：
3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        asum = sum(A)
        if asum % 3 is not 0:
            return False

        i=0
        j=len(A)-1
        balanceSum = asum / 3
        isum = sum(A[0:i+1])
        jsum = sum(A[j:])

        while isum != balanceSum and i+1 < j:
            i+=1
            isum = sum(A[0:i+1])

        while jsum != balanceSum and i+1 <j:
            j-=1
            jsum = sum(A[j:])

        if isum == jsum == balanceSum and i+1 < j:
            return True
        
        return False

s=Solution()
print(s.canThreePartsEqualSum([1,-1,1,-1]))
print(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(s.canThreePartsEqualSum([6,1,1,13,-1,0,-10,20]))
print(s.canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10]))
print(s.canThreePartsEqualSum([10,-10,10,-10,10,-10,10,-10]))






