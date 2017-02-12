# Research Review

A brief summary of the papers' goals and results:

## [Game Tree Searching by Min / Max Approximation](https://people.csail.mit.edu/rivest/pubs/Riv87c.pdf) by Ron Rivest, MIT 


## [Deep Blue](https://pdfs.semanticscholar.org/ad2c/1efffcd7c3b7106e507396bdaa5fe00fa597.pdf) by the IBM Watson Team 

The basic principle is that Deep Blue searched the game tree as far as possible, usually to a depth of six moves or more. It would then use an evaluation function to evaluate the quality of the nodes at that depth. Essentially, the evaluation function replaces the subtree below that node with a single value summarizing this subtree. Then, Deep Blue would proceed similarly to the minimax algorithm: The move that leads to the least bad worst-base scenario at this maximum depth is chosen. IBM put an enormous amount of effort into the design of the evaluation function. According to Wikipedia:

> The evaluation function had been split into 8,000 parts, many of them designed for special positions. In the opening book there were over 4,000 positions and 700,000 grandmaster games. The endgame database contained many six piece endgames and five or fewer piece positions. Before the second match, the chess knowledge of the program was fine tuned by grandmaster Joel Benjamin. The opening library was provided by grandmasters Miguel Illescas, John Fedorowicz, and Nick de Firmian.


## [AlphaGo](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf) by the DeepMind Team

Go cannot be tackled effectively with the same approach. Go has a wider branching factor (more possible moves at each state) than chess, and games tend to be longer. Hence, it is more difficult to search the game tree to a sufficient depth. In addition, it turns out that it is more difficult to design evaluation functions for Go than for chess. The endgame in Go is sometimes said to be especially complex. At the time of writing (March 15, 2016), Wikipedia notes:

> Thus, it is very unlikely that it will be possible to program a reasonably fast algorithm for playing the Go endgame flawlessly, let alone the whole Go game.

Monte Carlo Tree Search (MCTS) is an alternative approach to searching the game tree. The idea is to run many game simulations. Each simulation starts at the current game state and stops when the game is won by one of the two players. At first, the simulations are completely random: actions are chosen randomly at each state, for both players. At each simulation, some values are stored, such as how often each node has been visited, and how often this has led to a win. These numbers guide the later simulations in selecting actions (simulations thus become less and less random). The more simulations are executed, the more accurate these numbers become at selecting winning moves. It can be shown that as the number of simulations grows, MCTS indeed converges to optimal play.

What is interesting about MCTS is that no domain knowledge or expert input about the game is required. Whereas Deep Blue used a complex evaluation function which was designed with the help of expert chess players, MCTS merely requires traversing a tree and keeping track of some numbers. Also, it is convenient that the whole game tree does not have to be expanded, as this would be impossible. However, it is necessary to run a large number of simulations in order to achieve good results.

AlphaGo however makes extensive use of machine learning to avoid using hand-crafted rules. Three different kinds of neural networks are combined with a tree search procedure. 


AlphaGo relies on two different components: A tree search procedure, and convolutional networks that guide the tree search procedure. The convolutional networks are conceptually somewhat similar to the evaluation function in Deep Blue, except that they are learned and not designed. The tree search procedure can be regarded as a brute-force approach, whereas the convolutional networks provide a level on intuition to the game-play.

In total, three convolutional networks are trained, of two different kinds: two policy networks and one value network. Both types of networks take as input the current game state, represented as an image (with some additional input features, which are not important to our discussion).

The policy networks provide guidance regarding which action to choose, given the current state of the game. The output is a probability value for each possible legal move (i.e. the output of the network is as large as the board). Actions (moves) with higher probability values correspond to actions that have a higher chance of leading to a win.


## [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/pdf/1701.08734.pdf) by the DeepMind Team

