# knowledge_base.py
# A knowledge base for a knowledge-based agent.
# Cindy Chen

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        self.facts = []

    def tell(self, fact):
        print(f"Telling KB: {fact}")
        self.facts.append(fact)

    def ask(self, _):
        print("Asking KB for action.")
        return WumpusWorldAgent.climb
