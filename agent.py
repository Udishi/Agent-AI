from planner import Planner
from memory import Memory
from tools import Tools

class Agent:

    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.tools = Tools()

    def run(self, query):

        self.memory.add("user", query)

        action = self.planner.plan(query)

        response = self.tools.execute(action)

        self.memory.add("assistant", response)

        return response