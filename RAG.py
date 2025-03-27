from langchain.text_splitter import RecursiveCharacterTextSplitter
"""DATA_PATH = "docs/"
print(DATA_PATH)"""

with open("docs/doc.txt", "r") as a:
    documentaion = a.read()

# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Max size of each chunk
    chunk_overlap=20  # Overlap to preserve context
)

# Split the text into chunks
chunks = text_splitter.split_text(documentaion)

print(chunks)