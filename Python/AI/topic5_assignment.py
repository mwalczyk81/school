"""
Planning and Decision Making in AI Assignment

This assignment explores planning and decision-making strategies in AI. It includes understanding
AI planning techniques, decision trees, and Markov Decision Processes (MDPs), along with their implementation in Python.

Please ensure you have the following libraries installed:
- matplotlib
- scikit-learn
- numpy

You can install them using pip:
pip install matplotlib scikit-learn numpy
"""

import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

def create_decision_tree_classifier(features, labels):
    """
    Create and train a decision tree classifier.

    Parameters:
    features (numpy.ndarray): 2D array of training data, where each row is a sample and each column is a feature.
    labels (numpy.ndarray): 1D array of labels corresponding to the training data.

    Returns:
    classifier (DecisionTreeClassifier): The trained decision tree classifier.
    """
    # Your code here
    return tree.DecisionTreeClassifier().fit(features, labels)

def plot_decision_tree(classifier, feature_names, class_names):
    """
    Plot the decision tree using matplotlib.

    Parameters:
    classifier (DecisionTreeClassifier): The trained decision tree classifier.
    feature_names (list): A list of names for the features.
    class_names (list): A list of names for the output classes.

    Returns:
    fig (matplotlib.figure.Figure): A matplotlib figure illustrating the decision tree.
    """
    # Your code here
    plt.figure(figsize=(12, 8))
    tree.plot_tree(classifier, feature_names=feature_names, class_names=class_names, filled=True)
    plt.show()
    return plt.gcf()

def simulate_markov_decision_process(transition_matrix, reward_matrix, gamma, initial_state, n_steps):
    """
    Simulate a Markov Decision Process (MDP) for a given number of steps.

    Parameters:
    transition_matrix (numpy.ndarray): 2D array representing the transition probabilities between states.
    reward_matrix (numpy.ndarray): 2D array representing the rewards for transitions between states.
    gamma (float): Discount factor for future rewards.
    initial_state (int): The initial state index.
    n_steps (int): The number of steps to simulate.

    Returns:
    total_reward (float): The total accumulated reward.
    """
    # Your code here
    current_state = initial_state
    total_reward = 0.0

    for step in range(n_steps):
        next_state = np.random.choice(len(transition_matrix), p=transition_matrix[current_state])
        reward = reward_matrix[current_state, next_state]
        total_reward += (gamma ** step) * reward 
        current_state = next_state

    return total_reward

