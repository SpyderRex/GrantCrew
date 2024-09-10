from crewai import Task
from textwrap import dedent
from datetime import date

class GrantTasks:

    def fed_grant_task(self, agent, field):
        return Task(
            description=dedent(f"""
                Analyze and provide detailed information about the available federal grants for the given field.
                
                Your final answer must be a detailed report on the available federal grants, including amounts, deadlines, and eligibility requirements. Additionally, highlight any relevant stipulations or special considerations.

                {self.__tip_section()}

                Field: {field}
            """),
            agent=agent,
            expected_output="Detailed report on available federal grants, including amount, deadlines, and stipulations."
        )

    def state_grant_task(self, agent, state, field):
        return Task(
            description=dedent(f"""
                Research and provide detailed information about the available state grants for the specified field in the given state.
                
                The report should include details about the grant amounts, deadlines, and eligibility criteria. It should also note any special requirements or stipulations unique to the state’s grant programs.

                {self.__tip_section()}

                State: {state}
                Field: {field}
            """),
            agent=agent,
            expected_output="Detailed report on available state grants, including amount, deadlines, and stipulations specific to the state."
        )

    def report_task(self, agent):
        return Task(
            description=dedent(f"""
                Compile a comprehensive report summarizing both federal and state grant opportunities for the specified field.
                
                The report should include a clear comparison between federal and state grants, highlighting any overlaps or unique opportunities. It should also cover insights into eligibility, application deadlines, grant amounts, and any other critical details to consider when applying for these grants.
                
                The final answer must be a well-structured document, formatted as markdown, providing a complete overview of the grant landscape for the field.

                {self.__tip_section()}
            """),
            agent=agent,
            expected_output="Comprehensive markdown report summarizing federal and state grant opportunities, with comparison and detailed insights.",
            output_file="grant_report.md"
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $1000!"
