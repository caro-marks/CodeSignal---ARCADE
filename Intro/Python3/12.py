# # # Smooth Sailing

# ALL LONGEST STRINGS
# # Given an array of strings, return another array containing all of its longest strings.

def allLongestStrings1(inputArray):
    max_size = 0
    for string in inputArray:
        if len(string)>max_size:
            max_size=len(string)
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
    s3=s2
    for letter in s1:
        if letter in s3:
            s3=s3.replace(letter,'',1)
    return len(s2)-len(s3)

def commonCharacterCount2(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
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
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l

# reverse in Parantheses
# # Write a function that reverses in (possibly nested) parentheses in the input string.

def reverseInParentheses1(inputString):
    stack =['']
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
    total_weight_1 = sum([w for index, w in enumerate(a) if index%2==0])
    total_weight_2 = sum(a)-total_weight_1
    return [total_weight_1,total_weight_2]

def alternatingSums2(a):

    return [sum(a[::2]),sum(a[1::2])]

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
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]


