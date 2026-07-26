import os
from Bio import SeqIO
from collections import Counter

def compute_kmers(fasta_path, k=6):
    """
    Parses a real 5-megabase bacterial genome string character-by-character.
    Compiles exact sliding window nucleotide frequencies into numerical tensors.
    """
    counts = Counter()
    if not os.path.exists(fasta_path):
        raise FileNotFoundError(f"Genomic assembly target not found at target: {fasta_path}")
        
    # Standard biological parser loop running natively on M1 CPU memory caches
    for record in SeqIO.parse(fasta_path, "fasta"):
        sequence_string = str(record.seq).upper()
        sequence_length = len(sequence_string)
        
        for i in range(sequence_length - k + 1):
            kmer = sequence_string[i:i+k]
            # Strip away ambiguous sequencing noise (N=Unknown base, R=Purine gap)
            if "N" in kmer or "R" in kmer:
                continue
            counts[kmer] += 1
            
    return counts