# Track: Bioinformatics Stronghold
# Problem: Transcribing DNA into RNA
# ID: RNA

# Input: A DNA string 't' having length at most 1000 nt
# Output: The transcribed RNA string of 't'

# --- Program --- #
with open('./datasets/rosalind_rna.txt', 'r') as f:
    dataset = f.read().splitlines()[0]

with open('./outputs/rosalind_rna_1_output.txt', 'w') as f:
    f.write(dataset.replace('T', 'U'))
