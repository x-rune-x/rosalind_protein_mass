def get_masses():
    # Create dictionary of amino acid masses from text file.
    mass_file = open("monoisotopic_masses.txt", "r")

    mass_dict = {}

    # Import amino acid and corresponding mass value from each line in text file.
    for line in mass_file:
        amino_acid = line[0]
        mass = float(line[4:])

        mass_dict[amino_acid] = mass

    return mass_dict


def calc_peptide_mass(file_name):
    # Open text file with peptide string and calculate the summed masses of residues.

    mass_dict = get_masses()
    print(mass_dict)

    peptide_file = open(file_name, "r")
    peptide_string = peptide_file.read()
    peptide_string = peptide_string.strip("\n")
    # print(peptide_string)
    # print(len(peptide_string))

    peptide_mass = 0

    # Loop through each residue in the peptide and add its mass to the total.
    for position in peptide_string:
        peptide_mass += mass_dict[position]
        #print(mass_dict[position])

    return peptide_mass


total_mass = calc_peptide_mass("rosalind_prtm.txt")
print(total_mass)
print(round(total_mass, 3))
