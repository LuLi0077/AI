# Study Notes

## Sources

* Lectures   
* Artificial Intelligence A Modern Approach 3.4.4-5, 5.1 - 5.4
* [Multi-player alpha-beta pruning](http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/Korf_Multi-player-Alpha-beta-Pruning.pdf)
* [Depth-First Iterative Deepening vs Depth-First Search](http://movingai.com/dfid.html)
* [Iterative Deepening](https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf)


On a 5x5 board, the max number of nodes to visit is O(25!) == 10^25. Use the average branching factor will reduce it to 8^25 ~ 10^22, that's still too big


## Topics

**MinMax** 


**MaxN for multipler games**


**Depth limited search**

* Assume we can search 10^9 nodes per second. To play a step within 2 seconds, we can search 2*10^9 nodes. 

	- 8^x < 2*10^9 => x < 10.3 We can only search this far. 


**Evaluation function** 

* #my moves - #opp moves


**Quiescent search**


**Iterative deepening**

* exponential time n = (k^(d+1) - 1)/(k-1)
	
* search deeper or shallower depends on where the player is at 


**Horizon effect**

* try many evaluation functions and see which one works the best


**Alpha-beta pruning** 

* prune away the subtree that doesn't contribute to MinMax eval


## Tips:

1. Apply MinMax with alpha-beta pruning: reduce search space from b^d to b^(d/2) that is 8^25 to 8^12.

2. Rotate the board (0, 0), (4, 0), (4, 4) and (0, 4) have the same game tree: this is especially helpful in the beginning of the game when the braching factor is high. Player 1 has 25 possible moves, nut there are only 6 unique moves by using horizontal, vertical and diagonal symmetries. 

3. Above level 3 symmetry checking isn't worth it. 

4. As soon as there's a partition on the board, the player with longest path wins.

5. Player 2 always win. As Player 1, start at the center square then reflect (180 degree rotation of opponent's moves) player 2. Player 2 can move to where player 1 can't reflect to avoid lossing, there are 8 such moves. 

6. It's better to be player 2. If player 1 doesn't take the center square, then player 2 should.

7. Good book of openning moves -> equvilant moves and hash table to search efficiently -> limit time: minmax, iterative depening, alpha-beta pruning -> evaluation functions

