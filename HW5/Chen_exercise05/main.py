# Main
# A demonstration of the MinimaxTicTacToeAgent.
# Cindy Chen


# main.py

from tic_tac_toe_game import TicTacToeGame
from minimax_tic_tac_toe_agent import MinimaxTicTacToeAgent
from human_tic_tac_toe_agent import HumanTicTacToeAgent
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer

def print_board(state):
    """
    Helper function to print the tic-tac-toe board in a readable format.
    """
    board = [state[i:i + 3] for i in range(0, len(state), 3)]
    for row in board:
        print(' | '.join([str(cell) if cell is not None else ' ' for cell in row]))
        print('-' * 5)

def main():
    initial_state = (None, None, None, None, None, None, None, None, None)

    renderer = TicTacToeBoardRenderer()
    game = TicTacToeGame(initial_state, renderer)
    human_agent = HumanTicTacToeAgent('X', game)
    ai_agent = MinimaxTicTacToeAgent(game, 'O')

    while not game.is_terminal(game.state):
        if game.to_move(game.state) == 'X':
            print("Your turn (X):")
            human_move = human_agent.action(game.state)
            game.state = game.result(game.state, human_move)
        else:
            print("AI's turn (O):")
            _, ai_move = ai_agent.action(game.state)
            game.state = game.result(game.state, ai_move)
        print(game)
        
        if game.is_terminal(game.state):
            if game.is_win(game.state, 'X'):
                print("Congratulations! You won!")
            elif game.is_win(game.state, 'O'):
                print("AI wins! Better luck next time.")
            else:
                print("It's a draw!")
            break

if __name__ == "__main__":
    main()

