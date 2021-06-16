"""
https://www.geeksforgeeks.org/program-nth-catalan-number/
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

1. Count the number of possible Binary Search Trees with n keys (See this)
2. Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
3. Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.

See this for more applications. 
The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …  
"""


def catalanNumbersRecursive(n):
    if n < 1:
        return 1

    total = 0
    for i in range(n):
        total += catalanNumbersRecursive(i) * catalanNumbersRecursive(n - i - 1)

    return total


def catalonNumbersDynamic(n):
    if n == 0 or n == 1:
        return 1

    catalonMap = [0 for x in range(n + 1)]

    catalonMap[0] = 1
    catalonMap[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            catalonMap[i] += catalonMap[j] * catalonMap[i - j - 1]

    return catalonMap[n]


def main():

    for i in range(10):
        print(catalanNumbersRecursive(i))

    for i in range(10):
        print(catalonNumbersDynamic(i))

    return 0


main()
