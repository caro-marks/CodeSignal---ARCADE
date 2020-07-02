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