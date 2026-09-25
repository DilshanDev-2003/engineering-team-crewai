from pkgutil import ModuleInfo
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from pydantic import BaseModel, Field
from typing import List

import os
from crewai import LLM

# Initialize the Gemini LLM explicitly
local_llm = LLM(
    model="ollama/llama3.2:latest", # or "gemini/gemini-2.0-flash"
    base_url="http://localhost:11434"
)

class ModuleInfo(BaseModel):
    module_name: str = Field(description="The clear and specific module name for the task e.g., example.py")
    class_name: str = Field(description="A clear and specific class names that are include in the module")
    description: str = Field(description="A clear description about the what should be happens in the module and classes")

class ModuleArchitecture(BaseModel):
    overview: str = Field(description="Descriptive overview")
    modules: List[ModuleInfo] = Field(description="The modules that are essential for the system. Each task of the system should be divided into small tasks as modules")
    
@CrewBase
class EngineeringTeamX():
    """EngineeringTeamX crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'],
            llm=local_llm,
            verbose=True,
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            llm=local_llm,
            verbose=True,
        )

    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            llm=local_llm,
            verbose=True,
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            llm=local_llm,
            verbose=True,
        )     

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'],
            output_pydantic=ModuleArchitecture,
        )           