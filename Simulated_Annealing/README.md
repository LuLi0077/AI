# Simulated Annealing

![Simulated Annealing](SA_animation.gif)

As illustrated in the lectures, simulated annealing is a probablistic technique used for finding an approximate solution to an optimization problem. In this exercise we will implement [simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) to solve the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP) between US state capitals. Briefly, the TSP is an optimization problem that seeks to find the shortest path passing through every city exactly once. In our example the TSP path is defined to start and end in the same city (so the path is a closed loop).

Image Source: [Simulated Annealing - By Kingpin13 (Own work) [CC0], via Wikimedia Commons (Attribution not required)](https://commons.wikimedia.org/wiki/File:Hill_Climbing_with_Simulated_Annealing.gif)

### Main steps
1. Overview
2. Simulated Annealing -- Main Loop
3. Representing the Problem
4. Define the Temperature Schedule
5. Run Simulated Annealing on a Larger TSP

Initial Path (1374.28)             |  Final Path (1092.36)                   
:---------------------------------:|:---------------------------------:
<img src="https://github.com/LuLi0077/SDC/blob/master/Simulated_Annealing/InitialPath.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/SDC/blob/master/Simulated_Annealing/FinalPath.png" width="425" height="300">  