/*
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
 
提示：
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

/*
在数论中，正整数，即1、2、3……；
除了0以外的自然数就是正整数
*/
# include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return *(int*)a - *(int*)b; //由小到大排序
    //return *(int *)b - *(int *)a; 由大到小排序
}

int firstMissingPositive(int* nums, int numsSize)
{
    int minNum = 1;
    qsort(nums, numsSize, sizeof(nums[0]), cmp);

    for ( int i = 0; i < numsSize; i++) {
        if (nums[i] <= 0) {
            continue;
        } else if (nums[i] == minNum) {
            minNum ++;
        }
    }

    return minNum;
}

int main () 
{
    int nums[] = {2147483647,2147483646,2147483645,3,2,1,-1,0,-2147483648};
    int numsSize = 9;
    printf("%d\n",firstMissingPositive(nums, numsSize));
}