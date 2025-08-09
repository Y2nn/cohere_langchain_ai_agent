# Cohere Command R+ & Langchain: Multiple-Step AI Agent

We will now build a multiple-step AI Agent using the LangChain ecosystem and Cohere Command R+ model.

This AI application will take the user's query to search the web using the Tavily API and generate the Python code. Then, it will use Python REPL to execute the code and return the visualization that the user requested.

### Setting up the Cohere chat model
Then, we use the LangChain Python API to create a chat client by providing the Cohere API key we created before. We will use Command R+ as the language model in the AI agent.

### Setting up Tavily for Internet search
Sign up for Tavily and copy your API key. Tavily is an internet search API for LLMs and RAG pipelines.

To create the internet search tool, provide the API key we recently generated as an environment variable in DataLab. Then, update the name, description, and args_schema.

### Setting up Python REPL

Creating a Python REPL tool is straightforward: provide the Tool class with a Python REPL object, name, and description, and modify the argument schema.

### Creating and executing the AI agent
We will combine everything to create the multi-step AI agent using the .create_cohere_react_agent() function, the Cohere model client, tools, and prompt template. To execute our AI agent, we will use the AgentExecutor class by providing it with the agent object and tools.

### Testing the agent

### Conclusion

To wrap it up, we built a proper AI agent that takes user queries, searches the internet for the latest data, and generates visualizations using Python REPL.