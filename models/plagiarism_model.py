from sentence_transformers import SentenceTransformer
import numpy as np
from scipy.spatial.distance import cosine

# Load the SBERT model (you can choose other pre-trained models)
model = SentenceTransformer('all-MiniLM-L6-v2')

def check_plagiarism_with_sbert(text1, text2):
    # Get embeddings for both texts
    embeddings = model.encode([text1, text2])
    # Calculate cosine similarity between the embeddings
    similarity = 1 - cosine(embeddings[0], embeddings[1])
    
    # You can set a threshold value for plagiarism detection
    threshold = 0.85  # Example threshold
    if similarity >= threshold:
        return 1  # Plagiarism detected
    else:
        return 0  # No plagiarism detected

