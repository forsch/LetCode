# include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return *(int*)a - *(int*)b; //由小到大排序
    //return *(int *)b - *(int *)a; 由大到小排序
}
int majorityElement(int* nums, int numsSize)
{
    int m;

    if (numsSize == 0) {
        return nums[0];
    }

    qsort(nums, numsSize, sizeof(nums[0]), cmp);
    m = numsSize / 2;
    return nums[m];
}

int main() 
{
    int nums[15] = {1,2,3,4,3,7,9,0,5,6,3,3,3,9,2};
    int numsSize = 15;
    printf("%d\n", majorityElement(nums, numsSize));
}