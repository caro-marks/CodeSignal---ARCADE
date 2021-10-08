# # # The Journey Begins

# CENTURY FROM YEAR
# # Given a year, return the century it is in.

def centuryFromYear1(year):
    cent=year/100
    if cent.is_integer()==True:
        return int(cent)
    else:
        return int(cent)+1

def centuryFromYear2(year):
    return (year + 99) // 100


# CHECK PALINDROME
# # Given the string, check ir it is a palindrome.

def checkPalindrome1(inputString):
    revStrin=inputString[::-1]
    if inputString==revStrin:
        return True
    else:
        return False

def checkPalindrome2(inputString):
    return inputString == inputString[::-1]

# # # The Edge of the Ocean

# ADJACENT ELEMENTS PRODUCT
# # Given an array of integers,
# # find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct1(inputArray):
    v_max = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        act_value = inputArray[i] * inputArray[i+1]
        if act_value > v_max:
            v_max = act_value
        else:
            continue
    return v_max

def adjacentElementsProduct2(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])


# SHAPE AREA
# # Find the area of a n-interesting polygon for a given n.

def shapeArea1(n):
    return (n**2)+((n-1)**2)

def shapeArea2(n):
    return 2*n*(n-1)+1


# MAKE ARRAY CONSECUTIVE 2
# # Figure out

def makeArrayConsecutive21(statues):    
    needed_statues=[]
    for i in range(min(statues),max(statues)):
        if i not in statues:
            needed_statues.append(i)
    return len(needed_statues)

def makeArrayConsecutive22(statues):
    return max(statues) - min(statues) - len(statues) + 1


# ALMOST INCREASING SEQUENCE
# # Given an array of integers,
# # Determine if it's possible to obtain an increasing sequence by removing only one element.

def almostIncreasingSequence1(sequence):    
    q=sequence[:-1]; w=sequence[1:]; e=sequence[:-2]; r=sequence[2:]
    a=list(zip(q,w)); s=list(zip(e,r))
    d=[1 for i,j in a if i>=j]; f=[1 for i,j in s if i>=j]
    x=sum(d) <=1; y=sum(f) <=1
    return x and y

def almostIncreasingSequence2(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


# MATRIX ELEMENTS SUM
# # Given a matrix of integers,
# # add up all the values that don't appear below a 0.

def matrixElementsSum1(matrix):
    forb_ls=[]; all_lst=[]
    for floor in matrix:        
        for room,value in enumerate(floor):
            if value == 0:
                forb_ls.append(room)
            elif room in forb_ls:
                continue
            else:
                all_lst.append(value)
    return sum(all_lst)

def matrixElementsSum2(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total

# All Longest Strings
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
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r

# common Character Count
# # Given two strings, find the number of common characters between them.

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


