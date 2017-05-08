# Track: Bioinformatics Stronghold
# Problem: Translating RNA into Protein
# ID: prot

# Input: An RNA string 's' corresponding to a strand of mRNA (of length at most 10kbp)
# Output: The protein string encoded by 's'

# --- Funcitons --- #
def genetic_code(raw_genetic_code):
    genetic_vocabulary = {}
    for line in raw_genetic_code:
        codon, amino_acid = line.split()
        genetic_vocabulary[codon] = amino_acid
    return genetic_vocabulary

def translate(text, code_book):
    protein = ''
    for i in range(0, len(text), 3):
        if code_book[text[i:i+3]] != 'Stop':
            protein += code_book[text[i:i+3]]
        else:
            return protein
    # this last line is redundant, protein should always end with Stop codon
    return protein

# --- Main program --- #
with open('./datasets/rosalind_prot.txt', 'r') as f:
    dataset = f.read().splitlines()[0]

with open('./other_inputs/genetic_code.txt', 'r') as f:
    genetic_code_raw = f.read().splitlines()

with open('./outputs/rosalind_prot_2_output.txt', 'w') as f:
    f.write(translate(dataset, genetic_code(genetic_code_raw)))
