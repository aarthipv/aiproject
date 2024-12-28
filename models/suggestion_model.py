from transformers import pipeline

# Load a pre-trained model for text generation (e.g., GPT-2)
suggestion_model = pipeline('text-generation', model='gpt2')

def get_suggestions(text):
    # Ensure the input is within manageable length
    max_input_length = 500  # Limiting the text length
    if len(text) > max_input_length:
        text = text[:max_input_length]  # Truncate to fit model input

    # Change prompting strategy to generate concise suggestions for the whole paragraph
    prompt = (
        f"Give writing suggestions to enhance the formality, clarity, and refine the sentence structure of the following text:\n\n"
        f"{text}\n\nSuggestions:"
    )

    # Generate suggestions with parameters that prevent repetition and improve coherence
    suggestions = suggestion_model(prompt, 
                                   max_new_tokens=150,  # Adjusted for shorter responses
                                   num_return_sequences=1, 
                                   no_repeat_ngram_size=2, 
                                   temperature=0.9,  # Higher for creativity
                                   top_p=0.95,       # Allowing more diverse outputs
                                   top_k=50)

    # Format the output as a single string with bullet points
    formatted_text = suggestions[0]['generated_text'].strip()
    
    return formatted_text