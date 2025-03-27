from sentence_transformers import SentenceTransformer
from google_gemini import generate
# Load a pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


with open("docs/doc.txt", "r") as documentation:
    # Sample text data (your API documentation or knowledge base)
    documents = documentation.read()

documents = [para.strip() for para in documents.split('\n') if para.strip()]

# Convert documents into embeddings (vectors)
embeddings = model.encode(documents)

import faiss
import numpy as np

# Convert embeddings into a NumPy array
embeddings_array = np.array(embeddings).astype("float32")

# Create a FAISS index (L2 distance search)
index = faiss.IndexFlatL2(embeddings_array.shape[1])

# Add embeddings to the FAISS index
index.add(embeddings_array)

query = "Can users above 50 get a policy?"
query_embedding = model.encode([query]).astype("float32")

# Search FAISS index for the closest match
k = 2  # Number of closest results to retrieve
distances, indices = index.search(query_embedding, k)

# Display the most relevant documents
#print("Top results:")
#for i in range(k):
#    print(f"{i+1}. {documents[indices[0][i]]} (Score: {distances[0][i]})")

# Get the matching documents
retrieved_texts = [documents[i] for i in indices[0]]



def format_prompt(query, retrieved_texts):

    #Combines the user query with retrieved text chunks.

    context = "\n".join(retrieved_texts)  # Merge retrieved chunks
    prompt = f"Use the following information to answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    return prompt



"""query = input("Enter query\n")
final_prompt = format_prompt(query, retrieved_texts)
generate(final_prompt)"""