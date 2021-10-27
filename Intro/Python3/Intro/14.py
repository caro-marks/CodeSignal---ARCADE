# # # # # # # # Through the Fog

# # Circle of Numbers
# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.


def circleOfNumbers(n, firstNumber):
    if firstNumber < n/2:
        return n/2+firstNumber
    elif firstNumber > n/2:
        return n/2+firstNumber-n
    else:
        return 0


def circleOfNumbers(n, firstNumber):
    return (firstNumber + n/2) % n

# # Deposit Profit


def depositProfit(deposit, rate, threshold):
    amount = deposit
    years = 0
    while amount < threshold:
        amount = (rate/100+1)*amount
        years += 1
    return years


def depositProfit(deposit, rate, threshold):
    return math.ceil(math.log(threshold/deposit, 1+rate/100))

# # absolute Values Sum Minimization
# Given a sorted array of integers, which element is closest to all other values?


def absoluteValuesSumMinimization(a):
    b = []
    for i in range(len(a)):
        s = 0
        for j in range(len(a)):
            s += (abs(a[i]-a[j]))
        b.append(s)
    return a[b.index(min(b))]


def absoluteValuesSumMinimization(A):
    return A[(len(A)-1)//2]

# # Strings Rearrangement
# Given an array of equal-length strings, check if it's possible to rearrange the order of the elemento in such a way that each consecutive pair of strings differ by exactly one character.


def stringsRearrangement(inputArray):
    from itertools import permutations

    def diffBy1(st1, st2):
        return sum(a != b for a, b in zip(st1, st2)) == 1

    def goodList(lst):
        return all(diffBy1(lst[i], lst[i+1]) for i in range(len(lst) - 1))
    return any(map(goodList, permutations(inputArray)))


def stringsRearrangement(inputArray):
    def differsByOne(s1, s2):
        if len(s1) != len(s2):
            return False
        differentChars = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differentChars += 1
        return differentChars == 1

    def isChainPossible(startIndex, array):
        if len(array) == 1:
            return True
        newArray = array[:startIndex] + array[(1 + startIndex):]
        for i in range(len(newArray)):
            if differsByOne(array[startIndex], newArray[i]) and \
                    isChainPossible(i, newArray):
                return True
        return False
    for startIndex in range(len(inputArray)):
        if isChainPossible(startIndex, inputArray):
            return True
    return False
