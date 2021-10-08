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

