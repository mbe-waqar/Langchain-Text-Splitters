from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
    separator="",
)

result = text_splitter.split_documents(docs)

print(result[0].page_content)