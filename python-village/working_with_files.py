# Input: A file containing at most 1000 lines.
# Output: A file containing all the even-numbered lines from the original file.
#         Assume 1-based number of lines.

# ==================
# Initiate functions
# ==================
def lte_1000(text):
    if len(text) <= 1000:
        return True
    else:
        return False

# The text uses 1-based index, not 0-based!
def even_numbered_lines(text):
    return [line for index, line in enumerate(text) if index % 2]

# =================
# Start the program
# =================
dataset = dataset_raw.read().splitlines()
dataset_raw = open('./datasets/rosalind_ini5.txt', 'r')
dataset_raw.close()

# Alternative solution:
# Read lines read's string *with* escape characters, and puts them in a list
# with open('./datasets/rosalind_ini5.txt', 'r') as file:
#       print ''.join(file.readlines()[1::2])

if lte_1000(dataset):
    for line in even_numbered_lines(dataset):
        print line
else:
    print "Your input file should have less than 1000 lines."
