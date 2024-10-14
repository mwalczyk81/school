"""
Multi-Agent Systems Assignment

This assignment explores the fundamentals of agent-based models, implementing multi-agent systems in Python,
and simulating and analyzing agent interactions.

For this assignment, we will use the 'mesa' library for agent-based modeling.
Make sure to install it using pip:
pip install mesa
"""

from mesa import Agent, Model
from mesa.time import RandomActivation

class MyAgent(Agent):
    """
    An agent with fixed initial wealth.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        # Your code here: Define what the agent does in a single step
        try:
            if len(self.model.schedule.agents) == 0:
                raise ValueError("No agents available for interaction.")
            
            # Not sure if there is a better way than this but it works and the tests pass
            other_agent = self.random.choice(self.model.schedule.agents)

            if self.wealth > 0:
                self.wealth -= 1
                other_agent.wealth += 1
            
            if self.wealth < 0:
                    raise ValueError(f"Agent {self.unique_id} has negative wealth.")
            
        except Exception as e:
            print(f"Error in agent {self.unique_id} step: {e}")

class MyModel(Model):
    """
    A model with some number of agents.
    """
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        # Your code here: Define how the model steps
        self.schedule.step()

def run_simulation(N, steps):
    """
    Run the simulation of the multi-agent system.

    Parameters:
    N (int): Number of agents.
    steps (int): Number of steps the simulation should run.

    Returns:
    agent_wealth (list): A list containing the wealth of each agent at the end of the simulation.
    """
    # Your code here: Initialize the model, run the simulation, and return the final wealth of each agent
    try:
        model = MyModel(N)
        for _ in range(steps):
            model.step()
        agent_wealth = [agent.wealth for agent in model.schedule.agents]
        return agent_wealth

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
        return []