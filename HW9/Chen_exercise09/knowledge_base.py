# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

import time

class KnowledgeBase:
    def __init__(self):
        self.knowledge = []

    def tell(self, sentence):
        self.knowledge.append(sentence)
        print(f"Telling knowledge base: {sentence}")

    def ask(self, query):
        print(f"Asking knowledge base: {query}")
        return f"FAKE {time.time()}"


