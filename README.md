**Automated Game Player using Heuristic Evaluation and Genetic Algorithm**

**Objective**:
- Developed an automated game player for a classic block placement game (e.g., Tetris), which autonomously places game pieces to maximize the score using heuristic evaluation and genetic algorithms.
**Note**
  - game not devolped py me i am just edit on it
  - game belong to https://www.pygame.org/contribute.html
**Key Contributions**:
1. **Code Modification**:
   - Edited the original game code to enable automatic play instead of manual play.

2. **Heuristic Evaluation Function**:
   - Created a function to evaluate all possible positions and rotations for each game piece, rating them based on six heuristic values:
     - **Complete Line**: Counts the number of complete lines in the grid.
     - **Hole**: Counts the number of empty spaces with at least one tile above them in the same column.
     - **Bumpiness**: Measures the variation in column heights by summing the absolute differences between adjacent columns.
     - **Aggregate Height**: Calculates the sum of the heights of all columns.
     - **Total Blocking Blocks**: Counts the total number of blocks that block the movement of other blocks.
     - **Maximum Height**: Determines the maximum height of the columns on the game board.

3. **Application of Genetic Algorithm**:
   - Defined the genetic algorithm parameters: objective function, population size, chromosome size, generation size, crossover rate, and mutation rate.
     - Objective Function: Maximize the game score.
     - Population Size: 20
     - Chromosome Size: 6
     - Generation Size: 50
     - Crossover Rate: 0.25
     - Mutation Rate: 0.1
     - Heuristic List: {Complete Line, Hole, Bumpiness, Aggregate Height, Total Blocking Blocks, Maximum Height}
   
   - **Steps to Apply Genetic Algorithm**:
     1. **Initialization**: Initialized chromosomes for the population with random values within a specific range (0.0, 3.0).
     2. **Fitness Evaluation**: Evaluated the fitness value of each chromosome by multiplying it with the six heuristic values.
     3. **Selection Process**: Implemented roulette wheel selection and computed cumulative probability values.
     4. **Crossover Function**: Implemented single-point crossover function to combine chromosomes.
     5. **Mutation Function**: Implemented mutation function to introduce variations.
     6. **Training**: Trained the algorithm with 500 iterations.
     7. **Optimal Solution**: Identified the best solutions from the training.
     8. **Testing**: Tested the algorithm with 600 iterations.
   
4. **Results**:
   - Achieved a game score exceeding 10,000.
   - Utilized a random seed of 7 for game consistency during testing.

This project demonstrates the integration of heuristic evaluation and genetic algorithms to solve complex problems in an automated gaming context, showcasing skills in programming, algorithm design, and problem-solving.
