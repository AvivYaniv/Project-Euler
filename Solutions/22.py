FILE_NAME = 'names.txt'

DELIMITER = ','
STRING_DELIMITERS =  '"'

def ReadListFile(name):
    names = []
    with open(name) as f:
        lines = f.readlines()
    for line in lines:        
        for n in line.strip().replace(STRING_DELIMITERS, '').split(DELIMITER):
            names.append(n)        
    return names

def WordToAlphabetPositions(word):
    return [(ord(c) - ord('A') + 1) for c in word.upper()]

# Main
def main():
        
    names = ReadListFile(FILE_NAME)
    sorted_names = sorted(names)
    total_name_scores = 0
    for i in xrange(len(sorted_names)):
        name = sorted_names[i]
        sum_name_alphabet_position = \
            sum(WordToAlphabetPositions(name))
        name_score = (i + 1) * sum_name_alphabet_position
        total_name_scores += name_score

    # 871198282
    print total_name_scores
    
if __name__ == "__main__":
    main()
