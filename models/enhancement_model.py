from transformers import pipeline

# Load a pre-trained model for content refinement (e.g., T5)
enhancement_model = pipeline('text2text-generation', model='t5-base')

def preprocess_text(text):
    # Remove duplicate sentences and excessive punctuation
    sentences = text.split('. ')
    unique_sentences = list(dict.fromkeys(sentences))  # Keep only unique sentences
    cleaned_text = '. '.join(unique_sentences).strip()
    
    # Remove trailing punctuation if any
    cleaned_text = cleaned_text.rstrip('.')
    
    return cleaned_text

def enhance_content(text):
    # Preprocess the text to remove redundancy
    cleaned_text = preprocess_text(text)
    
    # Refining the content by providing a task-specific prompt
    enhanced_text = enhancement_model(
        f"Refine the following text to improve clarity, remove redundancy, and enhance the flow:\n\n{cleaned_text}",
        max_length=800,  # Allow for a longer output
        min_length=300,  # Set a reasonable minimum length
        do_sample=False   # Disable sampling to get more controlled output
    )
    
    return enhanced_text[0]['generated_text']

# Example usage
sample_text = (
    "Time management is really important for success in both personal and work life. "
    "Using tools like calendars, to-do lists, and apps that track time can help with managing time. "
    "If you’re not sure what to do, you can always ask for help. "
    "If you’re not sure what to do, you can always ask for help. "
    "A good time management strategy can help you get more done. "
    "And you can also learn how to say no to tasks that aren’t necessary."
)

enhanced_content = enhance_content(sample_text)
print(enhanced_content)
