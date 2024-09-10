import os
import json
import requests
from bs4 import BeautifulSoup
from crewai import Agent, Task, Crew
from langchain.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-70b-versatile")

class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(website):
        """Useful to scrape and summarize website content."""
        
        # Fetch the website content
        response = requests.get(website)
        if response.status_code != 200:
            return f"Failed to retrieve content from {website}"
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text(separator='\n')
        
        # Split the content into chunks if it's too long
        content_chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        summaries = []
        
        for chunk in content_chunks:
            # Define the agent and task
            agent = Agent(
                role='Principal Researcher',
                goal='Do amazing research and summaries based on the content you are working with',
                backstory="You're a Principal Researcher at a big company and you need to do research about a given topic.",
                allow_delegation=False,
                llm=llm
            )
            task = Task(
                agent=agent,
                description=f'Analyze and summarize the content below, make sure to include the most relevant information in the summary. Return only the summary, nothing else.\n\nCONTENT\n----------\n{chunk}',
                expected_output="Analysis and summary of scraped web content."
            )
            # Execute the task and get the summary
            crew = Crew(
                    agents=[agent],
                    tasks=[task],
                    verbose=False
                    )
            summary = str(crew.kickoff())
            summaries.append(summary)
        
        return "\n\n".join(summaries)
