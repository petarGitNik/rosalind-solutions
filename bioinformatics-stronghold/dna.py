# Track: Bioinformatics Stronghold
# Problem: Counting DNA Nucleotides
# ID: DNA

# Input: A DNA string 's' of length at most 1000 nt
# Output: Four integers (separated by spaces) counting the respective number of
#         times that the symbols 'A', 'C', 'G', and 'T' occur in dataset.

# --- Functions --- #
def count_nucleotides(strand):
    ACGT_sum = [0, 0, 0, 0]
    for nucleotide in strand:
        if nucleotide == 'A':
            ACGT_sum[0] += 1
        elif nucleotide == 'C':
            ACGT_sum[1] += 1
        elif nucleotide == 'G':
            ACGT_sum[2] += 1
        else:
            ACGT_sum[3] += 1
    return ACGT_sum

# --- Start program --- #
with open('./datasets/rosalind_dna.txt', 'r') as f:
    dataset = f.read().splitlines()

# Alternatively: text.count('a_nucleotide')

A, C, G, T = count_nucleotides(dataset[0])
print A, C, G, T
