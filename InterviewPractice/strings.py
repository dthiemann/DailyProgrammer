# Python scratch file for practicing String manipulation interview questions

""" 
https://igotanoffer.com/blogs/tech/microsoft-software-development-engineer-interview
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
https://igotanoffer.com/blogs/tech/microsoft-software-development-engineer-interview
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

"""
https://igotanoffer.com/blogs/tech/microsoft-software-development-engineer-interview
Given a 2D board and a word, find if the word exists in the grid. 
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""


def findWord(board, word):

    # Build map of indices in findWord
    letterIndexMap = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            result = findWordHelperDef(board, i, j, word)
            if result:
                return True
    return False


# Recursive method for finding if a word can be foudn
def findWordHelperDef(board, i, j, word):
    # Base case
    if len(word) == 0:
        return True

    if i > len(board) - 1 or i < 0 or j < 0 or j > len(board[i]) - 1:
        return False
    if word[0] != board[i][j]:
        return False

    board[i][j] = "-"
    return (
        findWordHelperDef(board, i - 1, j, word[1:])
        or findWordHelperDef(board, i + 1, j, word[1:])
        or findWordHelperDef(board, i, j - 1, word[1:])
        or findWordHelperDef(board, i, j + 1, word[1:])
    )


# print(
#     findWord(
#         [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
#     )
# )
# print(
#     findWord([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
# )
# print(
#     findWord([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
# )

"""
Given an unsorted integer array, find the smallest missing positive integer...
Your algorithm should run in O(n) time and uses constant extra space.

Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 10
"""


def findSmallestMissingPositiveInteger(nums):

    # :type nums: List[int]
    # :rtype: int
    #  Basic idea:
    # 1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
    #     so we only have to care about those elements in this range and remove the rest.
    # 2. we can use the array index as the hash to restore the frequency of each number within
    #      the range [1,...,l+1]

    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):  # delete those useless elements
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(
        len(nums)
    ):  # use the index as the hash to record the frequency of each number
        nums[nums[i] % n] += n
    for i in range(1, len(nums)):
        if nums[i] / n == 0:
            return i
    return n


print(findSmallestMissingPositiveInteger([1, 2, 0]))
print(findSmallestMissingPositiveInteger([3, 4, -1, 1]))
print(findSmallestMissingPositiveInteger([7, 8, 9, 11, 12]))

