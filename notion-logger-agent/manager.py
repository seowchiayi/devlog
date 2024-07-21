import os
import instructor
from multion.client import MultiOn
from prefect import task, flow
from prefect.task_runners import ConcurrentTaskRunner
from openai import OpenAI
from type import Task, TaskList
from viz import visualize_task_list
from dotenv import load_dotenv
from worker import WorkerAgent

load_dotenv()


class ManagerAgent:
    def __init__(
        self,
        objective: str = "",
        model_name: str = "gpt-4o-mini-2024-07-18",
        use_openai=True,
    ):
        self.objective = objective
        self.model_name = model_name

        if use_openai:
            self.client = instructor.from_openai(
                OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            )
        else:
            raise NotImplementedError

    def generate_tasks(self, objective: str) -> TaskList:
        # self.system_prompt = "You are an expert task manager that 
        # manages agents that each does one task. 
        # You decide how many agents is needed to do the meta-task, 
        # and what each agent's task is. The agents tasks should be done in parallel."

        self.system_prompt = "You are an expert backend engineer that want to debug problems with local development environment setup, particularly dependency installation. You should respond in a way where the solution is listed down in steps"

        self.user_prompt = f"""
                Create the tasks items for the following objective: {objective}
                """

        return self.client.chat.completions.create(
            model=self.model_name,
            response_model=Task,
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": self.user_prompt,
                },
            ],
        )

    @task
    def final_reduce(self, sessions: list) -> list:
        # Aggregate the results of the Multion sessions to get the top 10 frontend engineers.
        # For simplicity, we are returning the sessions as-is in this example.
        return sessions

    # Function to notify user (can be used to log the result or send a notification)
    @task
    def notify_user(self, action_results: list) -> None:
        for result in action_results:
            print(f"Notification to User: {result}")


@flow(name="Agent Flow", task_runner=ConcurrentTaskRunner())
def main(manager, objective: str):
    # Generate the tasks for the agents
    output_dict = manager.generate_tasks(objective)
    title = output_dict.name
    content = output_dict.cmd

    # import sys
    # sys.exit()
    # Uncomment to visualize tasks
    # visualize_task_list(tasks)

    # cmds = [task.cmd for task in tasks]
    # urls = [task.url for task in tasks]

    # Since we're running multiple tasks in parallel, we use Prefect's mapping to execute the same task with different inputs.
    # In this case, since the input is constant, we use 'unmapped' to prevent Prefect from trying to map over it.
    # Use map to execute perform_task for each cmd and url
    print(f"Title: {title}")
    print(f"Content: {content}")
    notion_link = "https://www.notion.so/4d675901b54d4bf3af7501476a109287?v=ddc1f98e0e6041b4997ec733826dffd1"
    results = WorkerAgent.perform_task(f"Create a new row with + New, Navigate to the new page, Replace Untitled in new page with {title}", notion_link)
    #results = WorkerAgent.perform_task(f"Create a new row with + New, Navigate to the new page and put {content} in the body", notion_link)
    # results = WorkerAgent.perform_task("Enter the title of the page as test and create a bulleted list with 2 items, hello and bye", notion_link)
    # results = WorkerAgent.perform_task("For the content of the page, create a codeblock  enter the title of the page as test and for the content of the page, create a codeblock and inside the codeblock create a bulleted list with 2 items, hello and bye", notion_link)
    # results = WorkerAgent.perform_task("inside the codeblock create a bulleted list with 2 items, hello and bye", notion_link)
    

    #print("Results: ", results)
    # Reduce phase: process results as needed
    #final_result = manager.final_reduce(manager, results)

    # Notify the user; this could also be sending an email, logging the result, etc.
    #notification = manager.notify_user(manager, final_result)
    return results
