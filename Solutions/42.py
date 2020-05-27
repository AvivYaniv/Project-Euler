
import math

FILE_NAME = 'words.txt'

DELIMITER = ','
STRING_DELIMITERS =  '"'

def ReadListFile(name):
    words = []
    with open(name) as f:
        lines = f.readlines()
    for line in lines:        
        for n in line.strip().replace(STRING_DELIMITERS, '').split(DELIMITER):
            words.append(n)        
    return words

def IsInteger(f):
    return int(f) == f

def GetTriangleNumberIndex(x):
    return (-1 + math.sqrt(1 + 8*x)) / 2

def IsTriangleNumber(x):
    return IsInteger(GetTriangleNumberIndex(x))
    
def GetTriangleNumber(n):
    return int((n * (n + 1)) / 2)

def IsTriangleWord(word):
    letter_triangle_sum = 0
    for l in word.upper():
        letter_triangle_sum += ord(l) - ord('A') + 1
    return IsTriangleNumber(letter_triangle_sum)

def GetTriangleWords(words):
    triangle_words = []
    for word in words:
        if IsTriangleWord(word):
            triangle_words.append(word)
    return triangle_words

# Main
def main():
    
    # 162
    print len(GetTriangleWords(ReadListFile(FILE_NAME)))
    
if __name__ == "__main__":
    main()
