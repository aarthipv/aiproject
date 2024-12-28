from transformers import pipeline

# Load the text2text-generation pipeline with the Grammarly model
corrector = pipeline("text2text-generation", model="grammarly/coedit-large")

def correct_grammar(text):
    # Prepare the input text with a clear instruction for grammar correction
    input_text = f"Correct this text: {text}"

    # Generate corrected text using the Grammarly model
    corrected_text = corrector(input_text, max_length=512)

    # Return the corrected text
    return corrected_text[0]['generated_text']
