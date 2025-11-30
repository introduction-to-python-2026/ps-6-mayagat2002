def create_codon_dict(file_path):
    codon_dict = {}

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            # דילוג על שורות ריקות או הערות
            if not line or line.startswith("#"):
                continue

            # פיצול לשדות
            parts = line.split()

            # נוודא שיש לפחות קודון ואמין-אסיד
            if len(parts) < 2:
                continue

            codon = parts[0].upper()
            amino_acid = parts[1]

            codon_dict[codon] = amino_acid

    return codon_dict
