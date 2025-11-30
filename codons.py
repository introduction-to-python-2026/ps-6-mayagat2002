def create_codon_dict(file_path):
    codon_dict = {}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines or comment lines
            if not line or line.startswith("#"):
                continue

            parts = line.split()

            # Expect at least 2 parts: codon and amino acid
            codon = parts[0]
            amino_acid = " ".join(parts[1:])  # handles multi-word amino acids

            codon_dict[codon] = amino_acid

    return codon_dict


