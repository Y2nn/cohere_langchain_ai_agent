# Import the necessary Python package with the functions.
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.utilities import PythonREPL
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere.chat_models import ChatCohere
from langchain.agents import AgentExecutor
# The class `TavilySearchResults` was deprecated in LangChain 0.3.25 and will be removed in 1.0.
# An updated version of the class exists in the :class:`~langchain-tavily package and should be used instead.
# To use it run `pip install -U :class:`~langchain-tavily` and import as
# `from :class:`~langchain_tavily import TavilySearch``.
# internet_search = TavilySearchResults(tavily_api_key=tavily_api_key)
# from langchain_tavily import TavilySearch
from langchain.agents import Tool

from dotenv import find_dotenv, load_dotenv

# LangChainDeprecationWarning: As of langchain-core 0.3.0, LangChain uses pydantic v2 internally.
# The langchain_core.pydantic_v1 module was a compatibility shim for pydantic v1, and should no longer be used.
# Please update the code to import from Pydantic directly.
# For example, replace imports like: `from langchain_core.pydantic_v1 import BaseModel`
# with: `from pydantic import BaseModel`
from pydantic import  BaseModel, Field

import os


_ = load_dotenv(find_dotenv())

# Get the Cohere API key.
cohere_api_key = os.environ.get('COHERE_API_KEY')

# Use the LangChain Python API to create a chat client for the AI agent.
chat = ChatCohere(
    model='command-r-plus',  # Command R+ as the language model
    temperature=0.7,
    cohere_api_key=cohere_api_key
)

# Get the Tavily API key.
tavily_api_key = os.environ.get('TAVILY_API_KEY')

# Tavily is an internet search API for LLMs and RAG pipelines.
# To create the internet search tool, provide the API key.
internet_search = TavilySearchResults(tavily_api_key=tavily_api_key)

# Update the name
internet_search.name = 'internet_search'
# Update the description
internet_search.description = 'Returns a list of relevant documents from the internet.'

class TavilySearchInput(BaseModel):
    query: str = Field(description='Internet query engine.')

# Update the args_schema
internet_search.args_schema = TavilySearchInput

# Create a Python REPL tool
python_repl = PythonREPL()

# Provide the Tool class with a Python REPL object, name, and description, and modify the argument schema.
repl_tool = Tool(
    name='python_repl',  # name
    description='Executes python code and returns the result.',  # description
    func=python_repl.run
)
repl_tool.name = 'python_interpreter'

class ToolInput(BaseModel):
    code: str = Field(description='python code execution.')

# Modify the argument schema of the Python REPL object
repl_tool.args_schema = ToolInput

# matplotlib langchain-tavily
if __name__ == '__main__':
    prompt = ChatPromptTemplate.from_template('{input}')

    # Create the multi-step AI agent using the .create_cohere_react_agent() function.
    agent = create_cohere_react_agent(
        llm=chat,  # Cohere model client
        tools=[internet_search, repl_tool],  # tools
        prompt=prompt  # prompt template
    )

    # To execute our AI agent, use the AgentExecutor class.
    agent_executor = AgentExecutor(
        agent=agent,  # agent object
        tools=[internet_search, repl_tool],  # tools
        verbose=True
    )

    # Use the agent_executor to generate a visualization.
    response = agent_executor.invoke(
        {
            'input': 'Create a pie chart of the top 5 most used programming languages in 2024.'
        }
    )

    """The result is amazing! It has successfully generated the pie chart using the latest data from the internet."""