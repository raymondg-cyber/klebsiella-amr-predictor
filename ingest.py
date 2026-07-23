import os
from Bio import Entrez

Entrez.email = "your_email@domain.com"

def download_assembly(accession, output_dir="data/raw_genomes"):
    os.makedirs(output_dir, exist_ok=True)
    target_path = os.path.join(output_dir, f"{accession}.fasta")
    if os.path.exists(target_path):
        return f"[CACHE] {accession} found."
    try:
        handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
        with open(target_path, "w") as f:
            f.write(handle.read())
        handle.close()
        return f"[SUCCESS] Downloaded {accession}"
    except Exception as e:
        return f"[ERROR] {accession} failed: {str(e)}"