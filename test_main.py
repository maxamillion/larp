import unittest
from unittest.mock import patch
from main import retrieve_info, Agent, Task, Crew
from langchain_community.llms import Ollama
from typing import Any

class TestMain(unittest.TestCase):

    def test_retrieve_info(self) -> None:
        query: str = "What is CrewAI?"
        expected_output: str = f"This is a placeholder response from the retriever. Query: {query}"
        self.assertEqual(retrieve_info(query), expected_output)

    def test_agent_initialization(self) -> None:
        llm: Ollama = Ollama(model="llama3")
        agent: Agent = Agent(
            role="Document Analyst",
            goal="To analyze documents",
            backstory="You are a document analyst",
            llm=llm,
            # tools=[] #remove the tools
        )
        self.assertEqual(agent.role, "Document Analyst")
        self.assertEqual(agent.goal, "To analyze documents")
        self.assertEqual(agent.backstory, "You are a document analyst")
        #self.assertEqual(agent.tools, []) #remove the tools

    def test_task_initialization(self) -> None:
        llm: Ollama = Ollama(model="llama3")
        agent: Agent = Agent(
            role="Document Analyst",
            goal="To analyze documents",
            backstory="You are a document analyst",
            llm=llm,
            #tools=[] #remove the tools
        )
        task: Task = Task(
            description="Answer a question",
            agent=agent,
            expected_output="A comprehensive answer"
        )
        self.assertEqual(task.description, "Answer a question")
        self.assertEqual(task.expected_output, "A comprehensive answer")

if __name__ == '__main__':
    unittest.main()