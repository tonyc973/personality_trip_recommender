from crewai import CrewBase, Agent, Task, Crew, Process, LLM, agent, task, crew
from crewai_tools import SerperDevTool

@CrewBase
class PersonalityTripRecommenderCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def user_profiler(self) -> Agent:
        return Agent(config=self.agents_config["user_profiler"], verbose=True, llm=LLM(model="claude-sonnet-4-6"))

    @agent
    def trip_researcher(self) -> Agent:
        return Agent(config=self.agents_config["trip_researcher"], verbose=True, llm=LLM(model="claude-sonnet-4-6"), tools=[SerperDevTool(api_key="SERPER_API_KEY")])

    @agent
    def report_writer(self) -> Agent:
        return Agent(config=self.agents_config["report_writer"], verbose=True, llm=LLM(model="claude-sonnet-4-6"))

    @task
    def analyze_personality(self) -> Task:
        return Task(config=self.tasks_config["analyze_personality"])

    @task
    def search_destinations(self) -> Task:
        return Task(config=self.tasks_config["search_destinations"])

    @task
    def generate_report(self) -> Task:
        return Task(config=self.tasks_config["generate_report"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
