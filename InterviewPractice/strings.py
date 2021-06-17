# Python scratch file for practicing String manipulation interview questions

""" 
Given an input string, reverse the string word by word
"""

# Using loops/indexing
def reverseStringByWord1(inputString):
    splitString = inputString.split(" ")
    finalString = ""
    for i in range(len(splitString)):
        finalString += splitString[len(splitString) - i - 1] + " "

    return finalString.strip()


# Using built-in array functions
def reverseStringByWord2(inputString):
    splitString = inputString.split(" ")
    return " ".join(splitString[::-1])


# print(reverseStringByWord1("Hello from the planet Mars!"))
# print(reverseStringByWord2("Hello from the planet Mars!"))

"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""


# Brute Force Attempt
def twoSumBruteForce(nums, target):
    for i in range(len(nums)):
        firstIndex = i

        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


def twoSumHash(nums, target):
    # Build dictionary
    numberToIndexMap = {}
    for i in range(len(nums)):
        numberToIndexMap[nums[i]] = i

    # Iterate to find the compliment
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in numberToIndexMap and compliment != nums[i]:
            return [i, numberToIndexMap[compliment]]

    return []


def twoSumHash2(nums, target):
    # Build dictionary
    numberToIndexMap = {}

    # Iterate to find the compliment
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in numberToIndexMap:
            return [i, numberToIndexMap[compliment]]

        numberToIndexMap[nums[i]] = i

    return []


# print(twoSumBruteForce([2, 7, 11, 15], 9))
# print(twoSumBruteForce([3, 2, 4], 6))
# print(twoSumHash([2, 7, 11, 15], 9))
# print(twoSumHash([3, 2, 4], 6))
# print(twoSumHash2([2, 7, 11, 15], 9))
# print(twoSumHash2([3, 2, 4], 6))
