# Short Talk: Introduction to Genetic Programming

This talk is a short (~ 1:00 hour), code-focused introduction to Genetic
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
- Code for running NEAT
  - AIGym -- OK

- Lecture Materials
  - Work on Outline a bit more
  - Prepare Slide outline
  - Add code/image to slides

- Improve code
  - Put all DEAP code in the same directory?
    - Output tree with .txt, output image with correct name
  - Make a module for operators/terminal sets in DEAP code
  - Make parameters explicit in DEAP code
  - Break AIGym code's evolution loop in DEAP code
  - Make Run images for DEAP code

- Code for running Softbots
