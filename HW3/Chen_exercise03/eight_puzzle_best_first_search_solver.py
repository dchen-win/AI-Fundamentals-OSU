# EightPuzzleBestFirstSearchSolver: A problem solver for the eight-puzzle problem
# that can apply best-first search to find a solution node. This class encapsulates
# a best-first search algorithm and an evaluation function. It encapsulates the
# application of the algorithm to the problem, and in the end can produce a
# solution, which is a list of actions.

from queue import PriorityQueue
from eight_puzzle_node import EightPuzzleNode
from eight_puzzle_agent import EightPuzzleAgent

class EightPuzzleBestFirstSearchSolver:

    def solution(self, problem):
        """
        Return a list of EightPuzzleAgent actuator methods. If the problem
        initial state is the same as the goal state, return an empty list.
        """
        solution_node = self.best_first_search(problem,
            self.cost_so_far_plus_estimated_cost_remaining)
        if solution_node:
            return self.actions_to_reach_solution_node(solution_node)
        else:
            return None


    def best_first_search(self, problem, evaluation_function):
        """
        Perform best-first search and return the solution node.
        """
        frontier = PriorityQueue()
        start_node = EightPuzzleNode(problem.initial_state, None, None, 0)
        frontier.put((evaluation_function(start_node), start_node))
        explored = {problem.initial_state: start_node}
        while not frontier.empty():
            _, current_node = frontier.get()
            if problem.is_goal(current_node.state):
                return current_node
            for child in self.expand(problem, current_node):
                if child.state not in explored.keys() or child.path_cost < explored[child.state].path_cost:
                        explored[child.state] = child
                        frontier.put((evaluation_function(child), child))
        return None


    def expand(self, problem, node):
        """
        Return a list of nodes reachable from `node` based on the available actions in the problem.
        Each child node will include the state, parent, action, and path-cost.
        """
        children = []
        for action in problem.actions(node.state):
            new_state = problem.result(node.state, action)
            cost = node.path_cost + problem.action_cost(node.state, action, new_state)
            child_node = EightPuzzleNode(state=new_state, parent=node, action=action, path_cost=cost)
            children.append(child_node)
        return children

    def manhattan_distance(self, state, goal_state=(None, 1, 2, 3, 4, 5, 6, 7, 8)):
        """
        Calculate the Manhattan distance between the current state and the goal state.
        The distance is the sum of absolute row and column differences for each tile.
        """
        distance = 0
        for i, tile in enumerate(state):
            if tile is not None:
                goal_index = goal_state.index(tile)
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(goal_index, 3)
                distance = distance + abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance


    def cost_so_far_plus_estimated_cost_remaining(self, node):
        """
        The evaluation function, f(n) = g(n) + h(n).
        """
        g_n = node.path_cost
        h_n = self.manhattan_distance(node.state)
        return g_n + h_n

    def actions_to_reach_solution_node(self, solution_node):
        """
        Given an EightPuzzleNode goal node, produce a list of in-order actions
        that lead from the initial state to the goal state.
        """
        actions = []
        current_node = solution_node
        while current_node.parent is not None:
            actions.append(current_node.action)
            current_node = current_node.parent
        actions.reverse()
        return actions
