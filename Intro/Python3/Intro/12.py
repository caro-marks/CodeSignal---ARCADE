# # # Smooth Sailing

# ALL LONGEST STRINGS
# # Given an array of strings, return another array containing all of its longest strings.

def allLongestStrings1(inputArray):
    max_size = 0
    for string in inputArray:
        if len(string) > max_size:
            max_size = len(string)
    longestStrings = []
    for string in inputArray:
        if len(string) == max_size:
            longestStrings.append(string)
    return longestStrings


def allLongestStrings2(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]

# COMMON CHARACTER COUNTS
# # Given two string, find the number of common characters between them.


def commonCharacterCount1(s1, s2):
    s3 = s2
    for letter in s1:
        if letter in s3:
            s3 = s3.replace(letter, '', 1)
    return len(s2)-len(s3)


def commonCharacterCount2(s1, s2):
    com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(com)

# is Lucky
# # Given a ticket number n, determine if the sum of its first half of the digits is equal to the sum of the second half, or not.


def isLucky1(n):
    numbers = [int(item) for item in str(n)]
    half = len(numbers)//2
    return sum(numbers[half:]) == sum(numbers[:half])


def isLucky2(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))

# Sort by Height
# # Rearrange the even numbers heights in a non-descending order


def sortByHeight1(a):
    items = sorted([item for item in a if item > 0])
    for i, j in enumerate(a):
        if j == -1:
            continue
        else:
            a[i] = items[0]
            del(items[0])
    return a


def sortByHeight2(a):

    l = sorted([i for i in a if i > 0])
    for n, i in enumerate(a):
        if i == -1:
            l.insert(n, i)
    return l

# reverse in Parantheses
# # Write a function that reverses in (possibly nested) parentheses in the input string.


def reverseInParentheses1(inputString):
    stack = ['']
    for i in inputString:
        if i == "(":
            stack.append('')
        elif i == ")":
            add = stack.pop()[::-1]
            stack[-1] += add
        else:
            stack[-1] += i
    return stack.pop()


def reverseInParentheses2(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


def reverseInParentheses3(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses3(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

# alternating sums
# # Return an array of 2 integers, where its elements are the weight.


def alternatingSums1(a):
    total_weight_1 = sum([w for index, w in enumerate(a) if index % 2 == 0])
    total_weight_2 = sum(a)-total_weight_1
    return [total_weight_1, total_weight_2]


def alternatingSums2(a):

    return [sum(a[::2]), sum(a[1::2])]

# Add Border
# # Given a rectangular matrix of characters, add a border of asterisks * to it.


def addBorder1(picture):
    size = len(picture[0])+2
    borded = [size*'*']
    pic = [f'*{p}*' for p in picture]
    borded.extend(pic)
    borded.append(size*'*')
    return borded


def addBorder2(picture):
    l = len(picture[0])+2
    return ["*"*l]+[x.center(l, "*") for x in picture]+["*"*l]

# Are Similar
# # Given two arrays, check if one can be obtained from another by syapping at most one pair of elements


def areSimilar(a, b):
    pairs = tuple(zip(a, b))
    diffs = []
    for pair in pairs:
        if pair[0] != pair[1]:
            diffs.append(list(pair))
    if len(diffs) == 1 or len(diffs) > 2:
        return False
    elif len(diffs) == 2 and diffs[0] != list(reversed(diffs[1])):
        return False
    else:
        return True


def areSimilar(A, B):
    return sorted(A) == sorted(B) and sum([a != b for a, b in zip(A, B)]) <= 2

# arrayChange
# # Find the minimal nuimber of moves required to obtain a strictly increasing sequence from an input array


def arrayChange(inputArray):
    loops = 0
    for index in range(1, len(inputArray)):
        diff = inputArray[index-1] - inputArray[index] + 1
        if diff > 0:
            inputArray[index] += diff
            loops += diff
    return loops


def arrayChange(inputArray):
    target = inputArray[0] - 1
    steps = 0
    for i in inputArray:
        if i > target:
            target = i
        else:
            target = target + 1
            steps += target - i

    return steps

# Palindrome Rearranging
# # Given a string, find out if tis chars can form a palindrome


def palindromeRearranging(inputString):
    chars = set(list(inputString))  # all single chars
    return sum([list(inputString).count(char) % 2 for char in chars]) < 2


def palindromeRearranging(inputString):
    s = set()
    for c in inputString:
        if c in s:
            s.remove(c)
        else:
            s.add(c)
    return len(s) <= 1
