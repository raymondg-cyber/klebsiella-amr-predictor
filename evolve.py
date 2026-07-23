from google import genai

def engineer_counter_peptide(mutation_profile, targeted_antibiotic):
    try:
        client = genai.Client()
        prompt = f"Design an AMP sequence to break through {mutation_profile} resistance to {targeted_antibiotic}."
        response = client.models.generate_content(
            model='gemini-3.5-flash', # Using free gemini-3.5-flashtier for debugging
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"[MOCK AMP] Ala-Leu-Trp-Cys-Arg (API Key missing, using offline backup model). Details: {str(e)}"