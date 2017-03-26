# Build a Game-playing Agent

Develop an adversarial search agent to play the game "Isolation".  

![Isolation](viz.gif)

## Synopsis

Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

These rules are implemented in the `isolation.Board` class.


## Implementation 

**`game_agent.py`**:

* Minimax algorithm - `CustomPlayer.minimax()`
* Alpha-beta pruning for minimax - `CustomPlayer.alphabeta()`
* Iterative deepening - `CustomPlayer.get_move()`
* Heuristic functions - `custom_score()`

Here's a brief summary of the performance of the agent using the different heuristic functions **heuristic_analysis.pdf**. 


## Testing

#### - Unit Tests

The `agent_test.py` script contains unittest test cases to evaluate the implementations.  


#### - Test Players

`sample_players.py` contains 3 player classes to test against locally:

- `RandomPlayer` - randomly selects a move from among the available legal moves
- `GreedyPlayer` - selects the next legal move with the highest heuristic value
- `HumanPlayer`  - allows *YOU* to play against the AI through the terminal


#### - Tournament

The `tournament.py` script will run a round-robin tournament between CustomPlayer agent with itertive deepening and custom heuristic function against several calibrated agents.

The tournament opponents are listed below: 

- Random: An agent that randomly chooses a move each turn.
- MM_Null: CustomPlayer agent using fixed-depth minimax search and the null_score heuristic
- MM_Open: CustomPlayer agent using fixed-depth minimax search and the open_move_score heuristic
- MM_Improved: CustomPlayer agent using fixed-depth minimax search and the improved_score heuristic
- AB_Null: CustomPlayer agent using fixed-depth alpha-beta search and the null_score heuristic
- AB_Open: CustomPlayer agent using fixed-depth alpha-beta search and the open_move_score heuristic
- AB_Improved: CustomPlayer agent using fixed-depth alpha-beta search and the improved_score heuristic


## Research Review

* [Game Tree Searching by Min / Max Approximation](https://people.csail.mit.edu/rivest/pubs/Riv87c.pdf) by Ron Rivest, MIT 
* [Deep Blue](https://pdfs.semanticscholar.org/ad2c/1efffcd7c3b7106e507396bdaa5fe00fa597.pdf) by the IBM Watson Team 
* [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/pdf/1701.08734.pdf) by the DeepMind Team
* [AlphaGo](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf) by the DeepMind Team - a brief summary of this paper's goals and results is included in **research_review.pdf**.


## Sources

* Udacity AIND lectures   
* Artificial Intelligence A Modern Approach (3.4.4, 3.4.5, 5.1 - 5.4)
* [Multi-player alpha-beta pruning](http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/Korf_Multi-player-Alpha-beta-Pruning.pdf)
* [Depth-First Iterative Deepening vs Depth-First Search](http://movingai.com/dfid.html)
* [Iterative Deepening](https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf)
* [Minimax with Alpha Beta Pruning](http://web.cs.ucla.edu/~rosen/161/notes/alphabeta.html)
* [Google DeepMind's AlphaGo: How it works](https://www.tastehit.com/blog/google-deepmind-alphago-how-it-works/)
