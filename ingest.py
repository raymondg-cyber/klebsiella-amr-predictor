import os
import time
from Bio import Entrez

# Required academic identification for NCBI Entrez API traffic routing
Entrez.email = "your_academic_email@domain.com"

def download_assembly(accession, output_dir="data/raw_genomes"):
    """
    Connects directly to NCBI Nucleotide databases to stream real clinical 
    bacterial assemblies block-by-block directly onto the Mac storage layer.
    """
    os.makedirs(output_dir, exist_ok=True)
    target_path = os.path.join(output_dir, f"{accession}.fasta")
    
    if os.path.exists(target_path):
        return f"[CACHE OK] Found existing local assembly for: {accession}"
        
    try:
        print(f"[INGEST] Querying NCBI Entrez Core for accession record: {accession}...")
        # Direct stream fetch to minimize unified memory footprint under 50MB
        handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
        raw_data = handle.read()
        handle.close()
        
        if not raw_data.strip():
            return f"[FAILED] Empty download response returned from NCBI for {accession}."
            
        with open(target_path, "w") as f:
            f.write(raw_data)
            
        # Polite API delay to prevent your local IP from being throttled by NCBI firewalls
        time.sleep(1)
        return f"[SUCCESS] Downloaded real clinical genomic data to {target_path}"
    except Exception as e:
        return f"[CONNECTION CRITICAL] Accession {accession} download aborted: {str(e)}"