# Build a Game-playing Agent

Develop an adversarial search agent to play the game "Isolation".  


## Synopsis

Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.


## Implementation

### Adversarial Search

* minimax algorithm

* alpha-beta pruning for minimax

* iterative deepening 


### Evaluation Functions

Develop heuristic functions to inform the value judgements the AI agent will make when choosing moves.  


## Testing

### Test Players

`sample_players.py` contains 3 player classes to test against locally:

- `RandomPlayer` - randomly selects a move from among the available legal moves
- `GreedyPlayer` - selects the next legal move with the highest heuristic value
- `HumanPlayer`  - allows *YOU* to play against the AI through the terminal


### Unit Tests

The `agent_test.py` script contains unittest test cases to evaluate the implementations.  


### Tournament

The `tournament.py` script will run a round-robin tournament between CustomPlayer agent with itertive deepening and custom heuristic function against several calibrated agent configurations using fixed-depth minimax and alpha-beta search with the example heuristics provided in `sample_players.py`.

The tournament opponents are listed below. 

- Random: An agent that randomly chooses a move each turn.
- MM_Null: CustomPlayer agent using fixed-depth minimax search and the null_score heuristic
- MM_Open: CustomPlayer agent using fixed-depth minimax search and the open_move_score heuristic
- MM_Improved: CustomPlayer agent using fixed-depth minimax search and the improved_score heuristic
- AB_Null: CustomPlayer agent using fixed-depth alpha-beta search and the null_score heuristic
- AB_Open: CustomPlayer agent using fixed-depth alpha-beta search and the open_move_score heuristic
- AB_Improved: CustomPlayer agent using fixed-depth alpha-beta search and the improved_score heuristic
