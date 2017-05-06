# Input: A string 's' of length at most 10000 letters.
# Output: The number of occurences of each word in 's', where words are separated
#         by spaces. Words are case-sensitive, and the lines in the output can be
#         in any order.

# ==================
# Initiate functions
# ==================
def lte_10k(text):
    if len(text) <= 10000:
        return True
    else:
        return False

def print_dict(dictionary):
    # Alternative: for key, value in dict.items(): print key, value
    for key in dictionary:
        print key, dictionary[key]

def split_words(text):
    return text.split()

def count_words(dictionary, text):
    for word in text:
        if dictionary.get(word, None):
            dictionary[word] += 1
        else:
            dictionary[word] = 1

# =================
# Start the program
# =================
dataset_raw = open("./datasets/rosalind_ini6.txt", 'r')
dataset = dataset_raw.read().splitlines()
dataset_raw.close()

if lte_10k(dataset[0]):
    word_count = {}
    text = split_words(dataset[0])
    count_words(word_count, text)
    print_dict(word_count)
else:
    print "Input string must have length of at most 10000 letters."
