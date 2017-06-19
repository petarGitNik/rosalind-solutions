# Track: Bioinformatics Stronghold
# Problem: Calculating Protein Mass
# ID: PRTM

# Input: A protein string 'P' of length at most 1000aa
# Output: The total weight of 'P'

# --- Funcitons --- #
# This function turns the raw list into dictionary
def give_me_monoisotopic_mass_table(monoisotopic_mass_table_raw):
    monoisotopic_mass_table = {}
    for couple in monoisotopic_mass_table_raw:
        letter, mass = couple.split()
        monoisotopic_mass_table[letter] = float(mass)
    return monoisotopic_mass_table

def calculate_protein_mass(protein, table):
    mass = 0
    for amino_acid in protein:
        mass += table[amino_acid]
    return mass

# --- Main program --- #
with open('./datasets/rosalind_prtm.txt', 'r') as f:
    dataset = f.read().splitlines()[0]

with open('./other_inputs/monoisotopic_mass_table.txt', 'r') as f:
    monoisotopic_mass_table_raw = f.read().splitlines()

table = give_me_monoisotopic_mass_table(monoisotopic_mass_table_raw)

with open('./outputs/rosalind_prtm_1_output.txt', 'w') as f:
    f.write(str(calculate_protein_mass(dataset, table)))
