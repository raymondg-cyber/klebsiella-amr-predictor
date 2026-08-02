import time
from google import genai

def engineer_counter_peptide(mutation_profile, targeted_antibiotic, diagnostic_metrics=None):
    """
    Acts as a clinical utility interface with an integrated retry mechanism 
    to automatically break through temporary Google Cloud server congestion.
    """
    client = genai.Client()
    
    prompt = f"""
    [CLINICAL UTILITY IN SILICO PROTOCOL]
    TARGET PATHOGEN: Klebsiella pneumoniae (Comparative Strain Cohort)
    COHORT DIAGNOSTICS LOG: {mutation_profile}
    TARGETED THERAPY FAILING: {targeted_antibiotic}
    
    [LOCAL MACHINE LEARNING DIAGNOSTICS]
    - XGBoost Optimization Engine: Apple Silicon M1 Thread Array
    - Cohort Balanced F1-Score: {diagnostic_metrics.get('F1-Score', 0.5714):.4f}
    
    TASK:
    Act as an expert clinical computational biologist. Synthesize a unified, resilient 
    broad-spectrum Antimicrobial Peptide (AMP) sequence designed to overcome the variations 
    detected across this clinical cohort. Output the candidate designation, single-letter 
    amino acid sequence, biophysical charge layout, and clinical synergy schematic.
    """

    # Retry loop configuration (Attempts 5 times with increasing pauses)
    max_retries = 5
    initial_delay = 3 

    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
            )
            # If the request succeeds, instantly return the real biological response text!
            return response.text
            
        except Exception as e:
            # Check if it is a temporary server traffic error
            if "503" in str(e) and attempt < max_retries:
                print(f"[RETRY ALERT] Google servers are busy. Attempt {attempt}/{max_retries} failed. Retrying in {initial_delay * attempt} seconds...")
                time.sleep(initial_delay * attempt)
                continue
            else:
                # If it's a non-503 error or we ran out of retries, fall back safely
                return f"[MOCK RESILIENCE CORE] Ala-Leu-Trp-Cys-Arg (Offline Backup Profile Active). Cloud detail: {str(e)}"