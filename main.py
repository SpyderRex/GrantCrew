import os
from crewai import Crew
from textwrap import dedent
from grant_agents import GrantAgents
from grant_tasks import GrantTasks

from dotenv import load_dotenv
load_dotenv()

class GrantCrew:

    def __init__(self, state, field):
        self.state = state
        self.field = field

    def run(self):
        agents = GrantAgents()
        tasks = GrantTasks()

        fed_grant_agent = agents.fed_grant_agent()
        state_grant_agent = agents.state_grant_agent()
        fed_grant_report_agent = agents.fed_grant_report_agent()
        state_grant_report_agent = agents.state_grant_report_agent()

        fed_grant_task = tasks.fed_grant_task(fed_grant_agent, self.field)
        state_grant_task = tasks.state_grant_task(state_grant_agent, self.state, self.field)
        fed_grant_report_task = tasks.federal_grant_report_task(fed_grant_report_agent, self.field)
        state_grant_report_task = tasks.state_grant_report_task(state_grant_report_agent, self.field, self.state)

        crew = Crew(
            agents=[fed_grant_agent, fed_grant_report_agent, state_grant_agent, state_grant_report_agent],
            tasks=[fed_grant_task, fed_grant_report_task, state_grant_task, state_grant_report_task],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to the Grant Search Crew")
    print('-----------------------------------')
    
    state = input(
        dedent("""
            Which state are you looking for grants in?
        """))
    field = input(
        dedent("""
            What is the field of interest for the grants?
        """))

    grant_crew = GrantCrew(state, field)
    result = grant_crew.run()
    
    print("\n\n#############################")
    print("## Here is your Grant Report")
    print("#############################\n")
    print(result)
