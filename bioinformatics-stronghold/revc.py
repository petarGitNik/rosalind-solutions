# Track: Bioinformatics Stronghold
# Problem: Complementing a Strand of DNA
# ID: REVC

# Input: A DNA string 's' having length at most 1000 nt
# Output: The reverse complement of 's^c' of 's'

# --- Funcitons --- #
def reverse_strand(strand):
    return strand[::-1]

def complement_strand(strand):
    reverse = ''
    # Name implies a function, alternative name could be: base_complement
    # or use replace() string method
    give_me_a_complement_of = { 'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G' }
    for nucleotide in reverse_strand(strand):
        reverse += give_me_a_complement_of[nucleotide]
    return reverse

# --- Main program --- #
with open('./datasets/rosalind_revc.txt', 'r') as f:
    dataset = f.read().splitlines()[0]

with open('./outputs/rosalind_revc_1_output.txt', 'w') as f:
    f.write(complement_strand(dataset))
