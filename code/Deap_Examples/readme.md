Deap Examples

Programs with GP examples from the DEAP library

# Symbolic Regression:
Using GP to find a hidden function from the set of input and output values.
Uses a simple GP to find the hidden function `x^4 + x^3 + x^2 + x` on 10 points in the [-1, 1] domain.

- `symbreg.py`: Base code.
- `symbreg_numpy.py`: numpy is used for the GP operators and evaluation. Maybe faster for larger examples?
- `symbreg_harm.py`:  HARM (Gardner 2015) is used to control bloat. The tree size is the same as symbreg.py, and running time is increased. Maybe this shows the difference better in a larger example?
- `symbreg_epsilon_lexicase.py`: Uses Epsilon Lexicase (how is lexicase used in this case, since we only have one problem?)
- `adf_symbreg.py`: Uses Automatically Defined Functions (ADF) - it is not clear how these work in the code.

# Parity
Using GP to find the parity of a bitstring (1 if the number of 1s is even, 0 otherwise). Program can sometimes find the optimum, sometimes get stuck in a local optima with size 6, gen 40. (maximum fitness = 2**size)

Interesting to see that bloat quickly takes hold if we increase gen to 80.

- `parity.py`: Base code.

# Multiplexer
Using GP to develop a multiplexer of 3+8 bits. A multiplexer reads the value of the first 3 bits, and uses it to select the output from the 8 other bits. For example, if first three bits of the multiplexer are 100, then selects bit 1 out of the 8 next (0-7). Maximum fitness is 2048 (2**11), however, standard GP (same as parity, 40 gen, 100 pop) can only get up to fitness ~1400. More difficult problem.

# Ant
Using GP to develop the controller for a "simulated ant". The simulated ant must walk over all food points in the board. It can move forward, turn left and turn right. It can sense if the square in front of it has food or not. The included ant file (santa fe trail) has 89 food, resulting in a maximum fitness of 89.

Note that because of the static nature of the map, the best possible individual does not use the input at all.

# Spambase
Uses the UCI Machine Learning Spam Dataset (1999). Fitness is 400 messages chosen randomly (noisy fitness function). Inputs are data signals already extracted from each message. Must mix boolean and float operators.

Actually performs pretty well.
