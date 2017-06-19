# Input: Two positive integers 'a' and 'b', where 'a' < 'b' < 10000
# Output: The sum of all odd integers from 'a' through 'b', inclusively

# ==================
# Initiate functions
# ==================
def is_it_less(a, b):
    if a < b:
        return True
    else:
        return False

def split_and_give_me_ints(text):
    return [int(num) for num in text.split()]

# =================
# Start the program
# =================
dataset_raw = open("./datasets/rosalind_ini4.txt", 'r')
dataset = dataset_raw.read().splitlines()
dataset_raw.close()

a, b = split_and_give_me_ints(dataset[0])

# The easier way to check this without a custom function is:
# if a < b < 10000:
if is_it_less(a, b) and is_it_less(b, 10000):
    # Alternatively: print sum([num for num in range(a,b+1) if num % 2])
    print sum([num for num in range(a,b+1) if num % 2 != 0])
else:
    print "Given integers should satisfy a < b < 10000"
