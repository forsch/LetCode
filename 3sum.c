/*
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return *(int*)a - *(int*)b; //由小到大排序
    //return *(int *)b - *(int *)a; 由大到小排序
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int i = 0, j = 0;
    int cur = 0, low = 0, high = 0, tmp = 0;
    int ans = 0;

    *returnSize = 0;
    if(numsSize < 3)return NULL;
    qsort(nums, numsSize, sizeof(nums[0]), cmp);

    //if(nums[0] > 0 || nums[numsSize - 1] < 0 || numsSize < 3)return NULL;

    int **retArray = (int **)malloc(sizeof(int *)*numsSize*6);
    *returnColumnSizes = (int *)malloc(sizeof(int)*numsSize*6);

    for(i = 0; nums[i] <= 0 && (i + 1 < numsSize - 1); i++)
    {
        if(i >= 1 && nums[i] == nums[i - 1])continue;
        low = i + 1;
        high = numsSize - 1;
        while(low < high){
            tmp = nums[low] + nums[high] + nums[i];
            if(tmp < 0){
                low++;
            }
            else if(tmp > 0){
                high--;
            }
            else{
                retArray[ans] = (int *)malloc(sizeof(int) * 3);                
                retArray[ans][0] = nums[i];
                retArray[ans][1] = nums[low];
                retArray[ans][2] = nums[high];
                returnColumnSizes[0][ans++] = 3;
                low++;high--;
                while(nums[low] == nums[low-1] && low < high)low++;
                while(nums[high] == nums[high+1] && low < high)high--;
            }            
        }
    }
    *returnSize = ans;
    return retArray;
}
