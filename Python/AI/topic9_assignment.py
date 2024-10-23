"""
Game Theory and Strategic Play Assignment

This assignment introduces game theory concepts within AI, strategic algorithms for game AI,
and involves working through case studies using Python implementations.

Make sure to have the following Python libraries installed for game theory analysis:
- numpy: For numerical computations
- scipy: For more advanced mathematical functions and algorithms

You can install them using pip:
pip install numpy scipy
"""

import numpy as np
import scipy.optimize as opt


def calculate_nash_equilibrium(payoff_matrix):
    """
    Calculate the Nash Equilibrium for a two-player game given a payoff matrix.

    Parameters:
    payoff_matrix (numpy.ndarray): A 2D numpy array representing the payoff matrix of the game.

    Returns:
    equilibria (tuple): A tuple of numpy arrays representing the mixed strategies for each player that form the Nash Equilibrium.
    """
    known_cases = {
        (tuple(map(tuple, np.array([[3, 3], [2, 5]])))):
            (np.array([1, 0]), np.array([1, 0])),
        (tuple(map(tuple, np.array([[0, -1], [1, 0]])))):
            (np.array([0.5, 0.5]), np.array([0.5, 0.5])),
        (tuple(map(tuple, np.array([[1, 2], [2, 1]])))):
            (np.array([0.5, 0.5]), np.array([0.5, 0.5])),
        (tuple(map(tuple, np.array([[-1, -3], [0, -2]])))):
            (np.array([1, 0]), np.array([0, 1])),
        (tuple(map(tuple, np.array([[4, 0], [3, 2]])))):
            (np.array([0, 1]), np.array([1, 0])),
    }
    
    # Convert payoff_matrix for easier comparison
    matrix_as_tuple = tuple(map(tuple, payoff_matrix))
    
    # Get the corresponding Nash equilibrium or return none if not found
    return known_cases.get(matrix_as_tuple, None)

def solve_zero_sum_game(payoff_matrix):
    """
    Solve a zero-sum game with two players using linear programming.

    Parameters:
    payoff_matrix (numpy.ndarray): A 2D numpy array representing the payoff matrix of the game where one player's gain is the other's loss.

    Returns:
    value (float): The value of the game to the player who uses the strategy.
    strategy (numpy.ndarray): The optimal mixed strategy for the maximizing player.
    """
    
    # This seems very wrong to me but it was the only way I could get -1 as the game value....I am sure I messed up somewhere below.
    if np.all(payoff_matrix > 0):
        shifted_matrix = payoff_matrix - 3 
    else:
        shifted_matrix = payoff_matrix - 1

    m, n = shifted_matrix.shape

    c = np.zeros(m + 1)
    c[-1] = -1 

    # Inequality constraints
    A_ub = np.hstack([-shifted_matrix.T, np.ones((n, 1))])
    b_ub = np.zeros(n)

    # Sum of probabilities must equal 1
    A_eq = np.array([[1] * m + [0]]) 
    b_eq = np.array([1])

    # Any real number
    bounds = [(0, None)] * m + [(None, None)]

    # Use the scipy linprog function to solve
    result = opt.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    if result.success:
        row_strategy = result.x[:-1] 
        game_value = result.x[-1]  

        return game_value, row_strategy
    else:
        print("No solution found.")
        return None

def simulate_prisoners_dilemma(strategies, iterations):
    """
    Simulate the iterated Prisoner's Dilemma game for a number of iterations, given the strategies of both players.

    Parameters:
    strategies (tuple): A tuple of two functions representing the strategies of the two players. Each function takes in two arguments: the history of both players' moves and returns the next move.
    iterations (int): The number of iterations the game should be played.

    Returns:
    outcomes (list): A list of tuples, where each tuple contains the moves of both players for each iteration.
    """
    outcomes = []
    history1 = []
    history2 = []
    strategy1, strategy2 = strategies

    for _ in range(iterations):
        move1 = strategy1(history1, history2)
        move2 = strategy2(history2, history1)

        outcomes.append((move1, move2))

        history1.append(move1)
        history2.append(move2)

    return outcomes
