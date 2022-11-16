# Short Talk: Introduction to Genetic Programming

This talk is a short (2 modules of 1 hour each), code-focused introduction to Genetic
Programming (GP). The intended audience are students in a Computer
Science-like program that have some coding experience, and some general
awareness of Artificial Intelligence and Evolutionary Computation.

Originally, this talk was an invited lecture for the course "Introduction to
Artificial Intelligence" at the University of Tsukuba.

# Outline
- What is Evolutionary Computation and Genetic Programming
- Implementation of Simple Genetic Programming (Examples: Regression, Parity)
- Applying the Simple GP to the pole balancing problem.
- Using Genetic Programming to generate a Neural Network Architecture
- A super short introduction to NEAT and HyperNEAT
- Recent Research: How to use Genetic Programming to design robots

- Extra1: The Bibites
- Extra2: PushGP

# References
- DEAP library for traditional GP: https://deap.readthedocs.io/en/master/tutorials/advanced/gp.html
- OpenAI Gym (Cart Pole Balancing): https://www.gymlibrary.dev/environments/classic_control/
- Fabio Github for softrobots: https://github.com/fhtanaka/SGR
- NEAT-python: https://neat-python.readthedocs.io/en/latest/neat_overview.html
- Original NEAT Paper: http://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf
- Kenneth Stanley's papers (NEAT): http://www.cs.ucf.edu/~kstanley/#publications
- Fabio's papers:
- PushGP:


# TODO
## Lecture Notes:
- Break the lecture in two parts:
  - Part 1: Until NEAT (GP Basics)
  - Part 2: From NEAT on (Modern GP?)
- Extend section on Fabio's work
- Add section on PushGP
- Add reference to GP Handbook
- Prepare a long form script, and rework slides based on script.

## Code Improvement
- Add softbot code from Fabio
- Merge directories 01 and 02
- 01_SimpleGP: create a .txt file with the best tree found
- 01_SimpleGP: Create a module for operator/terminal set selection
- 01_SimpleGP: Break evolution loop in the DEAP/AIGym example
- 01_SimpleGP: Make Evolutionary Run Dynamics images (check NEAT for how)
- Move all output generated by all code to an "outputs" directory (and add that to .gitignore)
- Remove `Deap_Examples`
- Minimize `requirements.txt` and other requirements.
