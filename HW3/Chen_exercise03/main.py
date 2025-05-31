
# Main
# Cindy Chen
# Demonstrate the use of your EightPuzzleAgent.

from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_transition_model import EightPuzzleTransitionModel


def main():
    scenarios = [
        ((7, 2, 4, 5, None, 6, 8, 3, 1), "Scenario 1"),
        ((8, None, 6, 5, 4, 7, 2, 3, 1), "Scenario 2"),
        ((8, 6, 7, 2, 5, 4, 3, None, 1), "Scenario 3"),
        ((6, 4, 7, 8, 5, None, 3, 2, 1), "Scenario 4"),
    ]
    
    solver = EightPuzzleBestFirstSearchSolver()

    for i, (initial_state, description) in enumerate(scenarios, start=1):
        print(f"\n{description}:")
        print(f"Initial State: {initial_state}")
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        actions = solver.solution(problem)
        agent = EightPuzzleAgent(initial_state,actions = actions)

        while agent.has_actions():
            action = agent.action()
            print(f"Action: {action}")
            
            action(agent)

            print(f"Updated State: {agent.current_state}")



if __name__ == "__main__":
    main()
