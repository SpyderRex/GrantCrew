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

    def federal_grant_report_task(self, agent, field):
        return Task(
            description=dedent(f"""
                Compile a comprehensive report summarizing federal grant opportunities for the specified field.
                
                The report should include a clear details for the available federal grants, highlighting unique opportunities. It should also cover insights into eligibility, application deadlines, grant amounts, and any other critical details to consider when applying for these grants.
                
                The final answer must be a well-structured document, formatted as markdown, providing a complete overview of the grant landscape for the field.

                Field: {field}

                {self.__tip_section()}
            """),
            agent=agent,
            expected_output="Comprehensive markdown report summarizing federal grant opportunities, with detailed insights.",
            output_file="federal_grant_report.md"
        )

    def state_grant_report_task(self, agent, state, field):
        return Task(
            description=dedent(f"""
                Compile a comprehensive report summarizing state grant opportunities for the specified field.
                
                The report should include a clear details for the available state grants, highlighting any unique opportunities. It should also cover insights into eligibility, application deadlines, grant amounts, and any other critical details to consider when applying for these grants.
                
                The final answer must be a well-structured document, formatted as markdown, providing a complete overview of the grant landscape for the field.

                State: {state}
                Field: {field}

                {self.__tip_section()}
            """),
            agent=agent,
            expected_output="Comprehensive markdown report summarizing state grant opportunities, with detailed insights.",
            output_file="state_grant_report.md"
        )


    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $1000!"
