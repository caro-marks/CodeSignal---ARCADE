# ISLAND OF KNOWLEDGE

# areEquallyStrong
# # Check if 2 pairs of numbers has the same weigth

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted((yourLeft, yourRight)) == sorted((friendsLeft, friendsRight))


def areEquallyStrong(ul, ur, fl, fr):
    return max(ul, ur) == max(fl, fr) and min(ul, ur) == min(fl, fr)


# arrayMaximalAdjacentDifference
# #Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for index in range(1, len(inputArray)-1):
        diff = max(abs(inputArray[index-1]-inputArray[index]),
                   abs(inputArray[index+1]-inputArray[index]))
        if diff > max_diff:
            max_diff = diff
    return max_diff


def arrayMaximalAdjacentDifference(a):
    diffs = [abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)

# isIPv4Address
# # Fivern a string, find out if it satisfies the ipv4 address naming rules


def isIPv4Address(inputString):
    splited_string = inputString.split('.')
    if len(splited_string) != 4:
        return False
    else:
        for i in splited_string:
            if i.isnumeric():
                if i == '':
                    return False
                elif len(i) > 1 and i[0] == '0':
                    return False
                else:
                    if int(i) > 255 or int(i) < 0:
                        return False
            else:
                return False
    return True


def isIPv4Address(s):
    p = s.split('.')
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

# avoidObstacles
# # Find the minimal length of the jump enough to avoid all the obstacles


def avoidObstacles(inputArray):
    initial_position = 0
    step = 2
    position = initial_position
    while position < max(inputArray):
        position += step
        if position not in inputArray:
            continue
        else:
            step += 1
            position = initial_position
    return step


def avoidObstacles(inputArray):
    c = 2
    while True:
        if sorted([i % c for i in inputArray])[0] > 0:
            return c
        c += 1

# Box Blur
# # Return the blurred image as an integer, with the fractions rounded down.


def boxBlur(image):
    filtered_image = []
    for row_index in range(1, len(image)-1):
        row = []
        for col_index in range(1, len(image[0])-1):
            result = 0
            result += image[row_index-1][col_index-1]
            result += image[row_index-1][col_index]
            result += image[row_index-1][col_index+1]
            result += image[row_index][col_index-1]
            result += image[row_index][col_index]
            result += image[row_index][col_index+1]
            result += image[row_index+1][col_index-1]
            result += image[row_index+1][col_index]
            result += image[row_index+1][col_index+1]
            row.append(int(result/9))
        filtered_image.append(row)
    return filtered_image


def boxBlur(image):
    return [[int(sum(sum(x[i:i+3]) for x in image[j:j+3])/9) for i in range(len(image[j])-2)] for j in range(len(image)-2)]


# Minwsweeper
# # Given a matrix of booleans, return a minesweeper

def minesweeper(matrix):
    def count_mines_around(matrix, row, col):
        total_mines = 0
        total_mines += find_mines(matrix, row-1, col-1)
        total_mines += find_mines(matrix, row-1, col)
        total_mines += find_mines(matrix, row-1, col+1)
        total_mines += find_mines(matrix, row, col-1)
        total_mines += find_mines(matrix, row, col+1)
        total_mines += find_mines(matrix, row+1, col-1)
        total_mines += find_mines(matrix, row+1, col)
        total_mines += find_mines(matrix, row+1, col+1)
        return total_mines

    def find_mines(matrix, row, col):
        if row < 0 or col < 0:
            return 0
        elif col > len(matrix[0])-1 or row > len(matrix)-1:
            return 0
        elif matrix[row][col] is True:
            return 1
        else:
            return 0
    mines = []
    for i_row in range(len(matrix)):
        row = []
        for i_col in range(len(matrix[0])):
            row.append(count_mines_around(matrix, i_row, i_col))
        mines.append(row)
    return mines


def minesweeper(matrix):
    r = []
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i+x < len(matrix) and 0 <= j+y < len(matrix[0]):
                        l += matrix[i+x][j+y]
            r[i].append(l)
    return r


# # # RAINS OF REASON # # #

# Array Replace
# # Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    response = []
    for i in inputArray:
        if i == elemToReplace:
            response.append(substitutionElem)
        else:
            response.append(i)
    return response


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [i if i != elemToReplace else substitutionElem for i in inputArray]

# evenDigitsOnly
# # Check if all digits of the given integer are even.


def evenDigitsOnly(n):
    for digit in str(n):
        if int(digit) % 2 != 0:
            return False
    return True


def evenDigitsOnly(n):
    return all([int(i) % 2 == 0 for i in str(n)])

# variable name
# # Check if the string has only letters, digits and underscores, but not starting by digits


def variableName(name):
    if name[0].isdigit():
        return False
    else:
        for char in name:
            if not char.isdigit() and not char.isalpha() and char != '_':
                return False
    return True


def variableName(name):
    return name.isidentifier()

# Alphabetic Shift
# # Given a string, your task is to replace each of its characters by the next one
# # in the English alphabet; i.e. replace a with b, replace b with c, etc
# # (z would be replaced by a).


def alphabeticShift(i):
    i = list(i)
    for x in range(len(i)):
        if i[x] == 'z':
            i[x] = 'a'
        else:
            i[x] = chr(ord(i[x])+1)
    return "".join(i)


def alphabeticShift(inputString):
    return ''.join((chr(ord(i)+1) if i != "z" else "a" for i in inputString))

# chessBoardCellColor
# # Given two cells, check if they have the same color or not


def chessBoardCellColor(cell1, cell2):
    def is_colored(cell):
        if cell[0] in ('A', 'C', 'E', 'G') and cell[1] in ('1', '3', '5', '7'):
            return True
        elif cell[0] in ('B', 'D', 'F', 'H') and cell[1] in ('2', '4', '6', '8'):
            return True
        else:
            return False
    return is_colored(cell1) == is_colored(cell2)


def chessBoardCellColor(cell1, cell2):
    a, b = "ACEG", "1357"
    c, d = "BDFH", "2468"
    return (cell1[0] in a and cell1[1] in b or cell1[0] in c and cell1[1] in d) \
        == (cell2[0] in a and cell2[1] in b or cell2[0] in c and cell2[1] in d)
