from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            tmp = nums[pointer]
            nums[pointer] = nums[i]
            nums[i] = tmp
            pointer += 1

def main():
    moveZeroes([0,1,0,3,12])

if __name__ == "__main__":
    main()