
# Encrypted File
ENCRYPTED_FILE_NAME     = "cipher.txt"
DELIMITER               = ','
STRING_DELIMITERS       = '"'

# English
A_Z_LOWERCASE           = range(ord('a'), ord('z')+1, 1)
A_Z_UPPERCASE           = range(ord('A'), ord('Z')+1, 1)
PUNCTUATION             = [ord(p) for p in '.,:- !\'()']

# General
CHAR_MAX_VALUE          = 256

# Encryption-Decryption Intelligence
KEY_LENGTH              = 3
MOST_COMMON_CHAR        = ' '
VALID_CHARS             = []
VALID_CHARS.extend(A_Z_LOWERCASE)
VALID_CHARS.extend(A_Z_UPPERCASE)
VALID_CHARS.extend(PUNCTUATION)

def ReadListFile(name, word_type):
    word = []
    with open(name) as f:
        lines = f.readlines()
    for line in lines:        
        for n in line.strip().replace(STRING_DELIMITERS, '').split(DELIMITER):
            word.append(word_type(n))
    return word

import itertools

def GetNextPremutation(chars):
    for p in itertools.permutations(chars, len(chars)):
        yield p

def FrequencyAnalysis(text):
    frequency = [(ci, 0) for ci in xrange(CHAR_MAX_VALUE)]
    for c in text:
        frequency[c] = (frequency[c][0], frequency[c][1]+1)
    return frequency

def BlockXOR(text, key):
    xored = []
    key_index = 0
    key_length = len(key)
    for p in text:
        xored.append(p ^ key[key_index])
        key_index = (key_index + 1) % key_length
    return xored

def GetDecryptionSuccessScore(decrypted, valid):
    valid_count = 0
    invalid_count = 0    
    frequency = FrequencyAnalysis(decrypted)
    for (c, o) in frequency:
        if c in valid:
            valid_count += o
        else:
            invalid_count += o
    return valid_count / float(valid_count + invalid_count)

def FrequencyAnalysisHeuristics(encrypted, key_length):
    # Setting frequency for each decrypted char
    frequency = FrequencyAnalysis(encrypted)

    # Sorting decrypted by frequency
    sorted_freq = sorted(frequency, cmp=None, key=lambda t: t[1], reverse=True)

    key_unsorted = []
    # Since space is MOST_COMMON_CHAR in any language
    # it must has been XORed most times with key chars -
    # XORing most common chars back with space,
    # hereby getting notion of key chars
    for ki in xrange(key_length):
        common_decrypted = sorted_freq[ki][0]
        common_encrypted = ord(MOST_COMMON_CHAR) ^ common_decrypted
        key_unsorted.append(common_encrypted)

    return key_unsorted

def DecryptXOR(encrypted, key_length):
    key_unsorted = FrequencyAnalysisHeuristics(encrypted, key_length)

    best_key = []
    best_score = 0
    best_decryption = []
    # Testing key premutaions, since it's unsorted
    for key_premutation in GetNextPremutation(key_unsorted):
        decrypted = BlockXOR(encrypted, key_premutation)
        score = GetDecryptionSuccessScore(decrypted, VALID_CHARS)
        if best_score < score:
            best_score = score            
            best_key = key_premutation
            best_decryption = decrypted
    return best_decryption

# Main
def main():

    encrypted = ReadListFile(ENCRYPTED_FILE_NAME, int)
    decrypted = DecryptXOR(encrypted, KEY_LENGTH)
    
    # 107359
    print sum(decrypted)
    
if __name__ == "__main__":
    main()
