import os
from dotenv import load_dotenv

from pymilvus import connections, DataType, Collection, FieldSchema, CollectionSchema, utility
from supabase.client import Client, create_client
from langchain import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.vectorstores import SupabaseVectorStore
from langchain.schema import (
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()

# supabase_url = os.environ.get("SUPABASE_URL")
# supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")
# supabase: Client = create_client(supabase_url, supabase_key)
MILVUS_HOST = os.environ.get("MILVUS_HOST", "localhost")
MILVUS_PORT = os.environ.get("MILVUS_PORT", 19530)
connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)

# Define the collection schema for Milvus
collection_name = os.environ.get("COLLECTION_NAME", "codebase_collection")
dimension = 768  # Assuming embeddings have a dimension of 768
collection_schema = CollectionSchema(
    fields=[
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dimension)
    ],
    description="Codebase Embeddings Collection"
)

# Create the collection in Milvus
if not utility.has_collection(collection_name):
    collection = Collection(name=collection_name, schema=collection_schema)

embeddings = OpenAIEmbeddings()

def clone_repository(github_link, local_dir):
    """Clone a GitHub repository to a local directory."""
    git.Repo.clone_from(github_link, local_dir)

def parse_repository(local_dir):
    """Parse the cloned repository and return a list of code snippets or files."""
    code_snippets = []
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            if file.endswith(".py"):  # focusing on Python files for this example
                with open(os.path.join(root, file), 'r') as f:
                    code_snippets.append(f.read())
    return code_snippets

def store_embeddings_in_milvus(code_snippets):
    """Convert code snippets to embeddings and store in Milvus."""
    for code in code_snippets:
        embedding = embeddings.embed(code)
        collection.insert([embedding])

# Assuming you have a function to convert codebase to embeddings and store in Milvus
# This function will replace the SupabaseVectorStore in your original code
def store_embeddings_in_milvus(codebase):
    # Convert codebase to embeddings
    embedding = embeddings.embed(codebase)
    # Store embeddings in Milvus
    collection.insert([embedding])


# Assuming you have a function to convert codebase to embeddings and store in Milvus
# This function will replace the SupabaseVectorStore in your original code
def store_embeddings_in_milvus(codebase):
    # Convert codebase to embeddings
    embedding = embeddings.embed(codebase)
    # Store embeddings in Milvus
    collection.insert([embedding])

# Clone the repository
github_link = os.environ.get("GITHUB_LINK")
local_dir = "cloned_repo"
clone_repository(github_link, local_dir)

# Parse the repository
code_snippets = parse_repository(local_dir)

# Store embeddings in Milvus
store_embeddings_in_milvus(code_snippets)


# vector_store = SupabaseVectorStore(
#     supabase, 
#     embeddings, 
#     table_name=os.environ.get("TABLE_NAME"),
#     query_name="repo_chat_search"
# )

while True:
    query = input("\033[34mWhat question do you have about your repo?\n\033[0m")

    if query.lower().strip() == "exit":
        print("\033[31mGoodbye!\n\033[0m")
        break

    matched_docs = vector_store.similarity_search(query)
    code_str = ""

    for doc in matched_docs:
        code_str += doc.page_content + "\n\n"
        
    print("\n\033[35m" + code_str + "\n\033[32m")

    
    template="""
    You are Codebase AI. You are a superintelligent AI that answers questions about codebases.

    You are:
    - helpful & friendly
    - good at answering complex questions in simple language
    - an expert in all programming languages
    - able to infer the intent of the user's question

    The user will ask a question about their codebase, and you will answer it.

    When the user asks their question, you will answer it by searching the codebase for the answer.

    Here is the user's question and code file(s) you found to answer the question:

    Question:
    {query}

    Code file(s):
    {code}
    
    [END OF CODE FILE(S)]

    Now answer the question using the code file(s) above.
    """

    chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature = 0.5)
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    chain.run(code=code_str, query=query)

    print("\n\n")


  