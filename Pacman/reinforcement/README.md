# P3 - [Reinforcement Learning](http://inst.eecs.berkeley.edu/~cs188/pacman/reinforcement.html)

![pacman_reinforcement](pacman_reinforcement.png)

Pacman seeks reward. Should he eat or should he run? When in doubt, Q-learn. Implement model-based and model-free reinforcement learning algorithms, applied to the AIMA textbook's Gridworld, Pacman, and a simulated crawling robot.

'valueIterationAgents.py' -	a value iteration agent for solving known MDPs
'qlearningAgents.py' - Q-learning agents for Gridworld, Crawler and Pacman
'analysis.py' -	a file to put answers to questions given in the project
'mdp.py' - defines methods on general MDPs
'learningAgents.py' - defines the base classes ValueEstimationAgent and QLearningAgent
'util.py' - utilities, including util.Counter, which is particularly useful for Q-learners
'gridworld.py' - the Gridworld implementation
'featureExtractors.py' - classes for extracting features on (state,action) pairs used for the approximate Q-learning agent (in 'qlearningAgents.py')

* Q1: Value Iteration (`valueIterationAgents.py` - `ValueIterationAgent`) 
* Q2: Bridge Crossing Analysis
* Q3: Policies
* Q4: Q-Learning
* Q5: Epsilon Greedy
* Q6: Bridge Crossing Revisited
* Q7: Q-Learning and Pacman
* Q8: Approximate Q-Learning