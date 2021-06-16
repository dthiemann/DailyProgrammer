# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


# recurisve method
def fibRecursive(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibRecursive(n - 1) + fibRecursive(n - 2)


# dynamic programming
def fibDynamic(n):
    map = [-1 for x in range(n + 1)]

    map[0] = 0
    map[1] = 1

    if n < 2:
        return map[n]

    for i in range(2, n + 1):
        map[i] = map[i - 1] + map[i - 2]

    return map[n]


# Given value "n", return the n^th value in the fib sequence
def fib(n):

    return 0


def main():
    print(fibRecursive(9))
    print(fibDynamic(9))


main()
