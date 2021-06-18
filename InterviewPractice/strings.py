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


# print(findSmallestMissingPositiveInteger([1, 2, 0]))
# print(findSmallestMissingPositiveInteger([3, 4, -1, 1]))
# print(findSmallestMissingPositiveInteger([7, 8, 9, 11, 12]))

"""
Remove comments from a C++ comment

Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.

In C++, there are two types of comments, line comments, and block comments.

The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others.

For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.

For example, source = "string s = "/* Not a comment. */";" will not be a test case.
Also, nothing else such as defines or macros will interfere with the comments.

It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

Examples:
Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

Input: source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
"""


def removeComments(source):
    modifiedSource = []

    i = 0
    while i < len(source):
        line = source[i]
        if "//" in line:
            # line comment
            if line.startswith("//") == False:
                modifiedSource.append(line.split("//")[0])

        elif "/*" in line:
            # block comment
            startLineIndex = i
            while "*/" not in source[i]:
                i += 1

            # Same line block comment
            if source[startLineIndex].startswith("/*") == False:
                modifiedSource.append(source[startLineIndex].split("/*")[0])

        else:
            modifiedSource.append(line)

        i += 1

    return modifiedSource


# source1 = [
#     "/*Test program */",
#     "int main()",
#     "{ ",
#     "  // variable declaration ",
#     "int a, b, c;",
#     "/* This is a test",
#     "   multiline  ",
#     "   comment for ",
#     "   testing */",
#     "a = b + c;",
#     "}",
# ]
# print(removeComments(source1))

"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.
"""


def findLongestSubStringWithK(givenString, k):
    subStrings = []

    maxCount = 0
    startIndex = 0
    endIndex = 0

    # i = 0
    # while i < len(givenString):
    #     if

    return subStrings
