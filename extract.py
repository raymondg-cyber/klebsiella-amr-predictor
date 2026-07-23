from Bio import SeqIO
from collections import Counter

def compute_kmers(fasta_path, k=6):
    counts = Counter()
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq = str(record.seq).upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if "N" in kmer or "R" in kmer:
                continue
            counts[kmer] += 1
    return counts