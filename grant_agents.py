import os

from crewai import Agent
from langchain_groq import ChatGroq

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-70b-versatile")

class GrantAgents():

  def fed_grant_agent(self):
    return Agent(
        role='Federal Grant Expert',
        goal='Find available federal grants for the given field.',
        backstory=
        'An expert in searching out federal grants by field',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        llm=llm)

  def state_grant_agent(self):
    return Agent(
        role='State Grant Expert',
        goal='Find the BEST available grants for the selected state and the specified field',
        backstory="""A knowledgeable grant expert with extensive information
        about grants available in the given state and for the given field
        """,
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        llm=llm)

  def report_agent(self):
    return Agent(
        role=' Report Writer',
        goal="""Write a detailed analysis of the available federal and state grants for the given city and in the given field""",
        backstory="""Specialist writing detailed analyses with 
        decades of experience.""",
        verbose=True,
        llm=llm)
