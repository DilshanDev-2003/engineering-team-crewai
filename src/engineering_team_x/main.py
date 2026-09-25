from platform import architecture
import sys
import warnings

from datetime import datetime

from engineering_team_x.crew import EngineeringTeamX

from crewai import Crew, Task
from engineering_team_x.crew import EngineeringTeamX

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    requirements = """
    A simple account management system for a trading simulation platform.
    Allow users to create an account, deposit funds, withdraw funds, and record buy/sell transactions.
    Calculate portfolio value, holdings, profit/loss, and list transaction history.
    """

    team = EngineeringTeamX()

    # Dynamic Architecture
    design_crew = Crew(
        agents=[team.engineering_lead()],
        tasks=[team.design_task()]
    )

    architecture_results = design_crew.kickoff(inputs={"requirements": requirements})
    plan = architecture_results.pydantic

    # Dynamic Tasks for each module
    dynamic_tasks = []

    for module in plan.modules:
        code_task = Task(
            description=f"Write module '{module.module_name}' with class '{module.class_name}'. Specs: {module.description}",
            expected_output="Raw Python code without markdown.",
            agent=team.backend_engineer(),
            output_file=f"output/{module.module_name}"
        )
        
        # Dynamic Test Task
        test_task = Task(
            description=f"Write unit tests for '{module.module_name}' using class '{module.class_name}'.",
            expected_output="Raw Python test code without markdown.",
            agent=team.test_engineer(),
            context=[code_task],
            output_file=f"output/test_{module.module_name}"
        )

        dynamic_tasks.extend([code_task, test_task])

    frontend_task = Task(
        description="Create a Gradio UI in app.py integrating all created backend modules.",
        expected_output="Raw Python code for Gradio app.",
        agent=team.frontend_engineer(),
        context=dynamic_tasks,
        output_file="output/app.py"
    )

    dynamic_tasks.append(frontend_task) 

    execution_crew = Crew(
        agents=[team.backend_engineer(), team.test_engineer(), team.frontend_engineer()],
        tasks=dynamic_tasks,
        code_execution_mode="safe"  # Uses Docker / WSL2!
    )
    
    execution_crew.kickoff()   

if __name__ == "__main__":
    run()