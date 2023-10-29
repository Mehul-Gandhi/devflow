import os
from dotenv import load_dotenv
from langchain import LLMChain
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

def get_flowchart_data_from_code(code):
    """Query LangChain LLM to interpret code and provide a breakdown for flowchart generation."""
    
    # Define the template for the LLM
    template = f"""
    You are Codebase AI. Your task is to convert the following code into a structured breakdown suitable for generating a flowchart:

    The flowchart's format is supposed to follow the format that is possible for future pipelining:
    Mermaid flowchart text form of the flowchart.

    example is here:


    {code}

    Breakdown:
    """
    
    # Initialize the ChatOpenAI model
    # replace with an open source LLM 
    chat = ChatOpenAI(streaming=True, temperature=0.5)
    
    # Create the prompt template
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])
    
    # Create the LLMChain
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    
    # Run the chain and get the response
    response = chain.run(code=code)
    
    # Extract the breakdown from the response
    breakdown = response.text.strip()
    
    return breakdown

# Sample code for testing
code_sample = """
def add_numbers(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return None
"""

# Get the breakdown for flowchart generation
flowchart_data = get_flowchart_data_from_code(code_sample)
print(flowchart_data)