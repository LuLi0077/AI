# Build a Game-playing Agent

Develop an adversarial search agent to play the game "Isolation".  


### Synopsis ###

Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

These rules are implemented in the `isolation.Board` class.


### Implementation (`game_agent.py`) ###

* Minimax algorithm - `CustomPlayer.minimax()`
* Alpha-beta pruning for minimax - `CustomPlayer.alphabeta()`
* Iterative deepening - `CustomPlayer.get_move()`
* Heuristic functions - `custom_score()`

Here's a brief summary of the performance of the agent using the different heuristic functions **heuristic_analysis.md**. 


### Testing ###

#### Unit Tests

The `agent_test.py` script contains unittest test cases to evaluate the implementations.  


#### Test Players

`sample_players.py` contains 3 player classes to test against locally:

- `RandomPlayer` - randomly selects a move from among the available legal moves
- `GreedyPlayer` - selects the next legal move with the highest heuristic value
- `HumanPlayer`  - allows *YOU* to play against the AI through the terminal


#### Tournament

The `tournament.py` script will run a round-robin tournament between CustomPlayer agent with itertive deepening and custom heuristic function against several calibrated agents.

The tournament opponents are listed below: 

- Random: An agent that randomly chooses a move each turn.
- MM_Null: CustomPlayer agent using fixed-depth minimax search and the null_score heuristic
- MM_Open: CustomPlayer agent using fixed-depth minimax search and the open_move_score heuristic
- MM_Improved: CustomPlayer agent using fixed-depth minimax search and the improved_score heuristic
- AB_Null: CustomPlayer agent using fixed-depth alpha-beta search and the null_score heuristic
- AB_Open: CustomPlayer agent using fixed-depth alpha-beta search and the open_move_score heuristic
- AB_Improved: CustomPlayer agent using fixed-depth alpha-beta search and the improved_score heuristic


### Research Review ###

A brief summary of the following papers' goals and results are included in **research_review.md**.

* [Game Tree Searching by Min / Max Approximation](https://people.csail.mit.edu/rivest/pubs/Riv87c.pdf) by Ron Rivest, MIT 
* [Deep Blue](https://pdfs.semanticscholar.org/ad2c/1efffcd7c3b7106e507396bdaa5fe00fa597.pdf) by the IBM Watson Team 
* [AlphaGo](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf) by the DeepMind Team
* [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/pdf/1701.08734.pdf) by the DeepMind Team


### Study Notes ###

#### Sources

* Udacity AIND lectures   
* Artificial Intelligence A Modern Approach (3.4.4, 3.4.5, 5.1 - 5.4)
* [Multi-player alpha-beta pruning](http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/Korf_Multi-player-Alpha-beta-Pruning.pdf)
* [Depth-First Iterative Deepening vs Depth-First Search](http://movingai.com/dfid.html)
* [Iterative Deepening](https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf)
* [Minimax with Alpha Beta Pruning](http://web.cs.ucla.edu/~rosen/161/notes/alphabeta.html)
* [Google DeepMind's AlphaGo: How it works](https://www.tastehit.com/blog/google-deepmind-alphago-how-it-works/)


#### Topics

###### MinMax

###### MaxN for multipler games

###### Depth limited search

* Assume we can search 10^9 nodes per second. To play a step within 2 seconds, we can search 2*10^9 nodes. 
	- 8^x < 2*10^9 => x < 10.3 We can only search this far. 

###### Evaluation function

* #my moves - #opp moves

###### A* search

Finds lowest cost path if:
* h(s) < true cost - h never overestimate, h is optimistic and admissable

###### Quiescent search

###### Iterative deepening

* exponential time n = (k^(d+1) - 1)/(k-1)	
* search deeper or shallower depends on where the player is at 

###### Horizon effect

* try many evaluation functions and see which one works the best

###### Alpha-beta pruning

* prune away the subtree that doesn't contribute to MinMax eval


#### Tips:

1. Apply MinMax with alpha-beta pruning: reduce search space from b^d to b^(d/2) that is 8^25 to 8^12.
2. Rotate the board (0, 0), (4, 0), (4, 4) and (0, 4) have the same game tree: this is especially helpful in the beginning of the game when the braching factor is high. Player 1 has 25 possible moves, nut there are only 6 unique moves by using horizontal, vertical and diagonal symmetries. 
3. Above level 3 symmetry checking isn't worth it. 
4. As soon as there's a partition on the board, the player with longest path wins.
5. Player 2 always win. As Player 1, start at the center square then reflect (180 degree rotation of opponent's moves) player 2. Player 2 can move to where player 1 can't reflect to avoid lossing, there are 8 such moves. 
6. It's better to be player 2. If player 1 doesn't take the center square, then player 2 should.S
7. Good book of openning moves -> equvilant moves and hash table to search efficiently -> limit time: minmax, iterative depening, alpha-beta pruning -> evaluation functions

