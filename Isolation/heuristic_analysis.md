# Heuristic Analysis

Artificial Intelligence A Modern Approach 5.4 - 

An evaluation function returns an estimate of the expected utility of the game from a given position.

- First, the evaluation function should order the terminal states in the same way as the true utility function: states that are wins must evaluate better than draws, which in turn must be better than losses.
- Second, the computation must not take too long!
- Third, for nonterminal states, the evaluation function should be strongly correlated with the actual chances of winning.


analysis should conclude with a comparison of the different heuristics and your reasoning for choosing the heuristic you ultimately use in your submitted agent.

For each of your three custom heuristic functions, evaluate the performance of the heuristic using the included tournament.py script. Then write up a brief summary of your results, describing the performance of the agent using the different heuristic functions verbally and using appropriate visualizations.

The report makes a recommendation about which evaluation function should be used and justifies the recommendation with at least three reasons supported by the data.

A brief report lists (using a table and any appropriate visualizations) and verbally describes the performance of agents using the implemented evaluation functions. Performance data includes results from tournament.py comparing (at a minimum) the best performing student heuristic against the ID_Improved agent.

In other words, the suggestion is to alter minimax or alpha–beta in two ways: replace the utility function by a heuristic evaluation function EVAL, which estimates the position’s utility, and replace the terminal test by a cutoff test that decides when to apply EVAL.