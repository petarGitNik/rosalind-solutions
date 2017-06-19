# Input: String of length of at most 200 letters, and four intexers: i, j, q, r
# Output: The slice of the string from indices 'i' through 'j' and 'q' through 'r'
#         (with space in between) inclusively.

# =================
# Prepare functions
# =================
def check_length(text):
    if len(text) <= 200:
        return True
    else:
        return False

# Convert list of strings to list of ints
def convert_str_to_int(list_of_strings):
    return [int(num) for num in list_of_strings]

# Take the upper and lower boundaries i.e. i, j, q, r
def give_me_boundaries(text):
    boundaries = text.split()
    boundaries_int = convert_str_to_int(boundaries)
    return [
        boundaries_int[0],
        boundaries_int[1],
        boundaries_int[2],
        boundaries_int[3]
    ]

def give_me_slice(text, lower, upper):
    return text[lower:upper+1]

# =================
# Start the program
# =================

# Open a file and split it by lines
# dataset[0] - the text string
# dataset[1] - upper and lower boundaries
dataset_raw = open("./datasets/rosalind_ini3.txt", 'r')
dataset = dataset_raw.read().splitlines()
dataset_raw.close

if check_length(dataset[0]):
    i, j, q, r = give_me_boundaries(dataset[1])
    print give_me_slice(dataset[0], i, j), give_me_slice(dataset[0], q, r)
else:
    print "The input string should not have length greater than 200 letters."
