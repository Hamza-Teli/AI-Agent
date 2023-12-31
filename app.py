import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()

# To get the absolute path of current script
script_dr = os.path.abspath(os.getcwd())

# To get absolute path of the parent directory
parent_dir = os.path.join(script_dr, os.pardir)

dotenv_path = os.path.join(parent_dir, '.env')

# Load the .env file from parent directory
load_dotenv(dotenv_path)


# ALL GPT BELOW ----------------------------------------------------
llm = OpenAI(temperature=0)

# Below is GPT 3.5 turbo
chat_llm = ChatOpenAI(temperature=0)
print(chat_llm.model_name)

# If you want to use a specific model use the code below!
# modelYouWant = ChatOpenAI(model="gpt-4", temperature=0)

# Below is the langchain model
print(llm.model_name)
get_user_input = input("[LANGCHAIN] Enter a prompt: ")
prediction = llm.predict(get_user_input)
print(prediction)

# ChatGPT 3.5 Model
get_user_input_for_gpt3 = input("[GPT3.5 Turbo] Enter a prompt: ")
print(chat_llm.predict(get_user_input_for_gpt3))


# The AI Agent!
tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent_executor = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

get_user_input_for_agent_executor = input("[Agent Executor] Enter a prompt: ")
agent_executor.invoke({f"input: {get_user_input_for_agent_executor}"})