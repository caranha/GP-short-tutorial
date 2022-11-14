# Introduction

# What is Evolutionary Computation and Genetic Programming?

What are Evolutionary Algorithms?

What is Genetic Programming?

What are the basic components of Genetic Programming?

What are operators? What is Arity?

What are terminals? What are Inputs and Constants?

# Implementation of Simple Genetic Programming

- We will solve a simple regression problem as an example of Genetic Programming.

- Introducting the DEAP library.

- Selecting Operators, Terminals, and the Genetic Loop.

- Observing one run.

- Analyzing the results: Observing the initial population and the final population.

- Analyzing the results: Runtime analysis -- maximum and mean fitness, tree size.

- What if we keep running the algorithm? Bloat.

- Let's solve another problem: Binary Parity. Choosing appropriate terminals and operators.

# Applying the Simple GP to the pole balancing problem.

- Introducing the pole balancing problem: Open AIGym.

- Interacting GP with simulators. Application to robotics.

- Analyzing the results. How long does it take to run?

- How can we make GP perform better:
  - Problem is stochastic, fitness must be evaluated over several repetitions
  - Operator selection
  - Parameter optimization (crossover rate, mutation rate)

# Using Genetic Programming to generate a Neural Network Architecture

- GP was developed in the 90ies, but today everyone is all about the neural networks. Can we evolve NNs? Yes!

- NNs as GP trees. Sigmoid operators. Structure vs Weights.

- How do we train the weights? We can evolve them, we can fix them (David Ha, WANNs) or we can backprop them.

# GP for neural network: NEAT

- Neat was an algorithm in the 2000s to generate neural networks using GP.

- Description of NEAT. Operators, connections. Key idea: Families for crossover of very different networks.

- Using NEAT for OpenAI pole balancing

- Go through NEAT code (parameters, parallelization, etc) (use xor example for simpler code)

- Another example: Genenating images using NEAT and CPPNs

##############################################S
# Recent Research: How to use Genetic Programming to Design Robots

- A recent paper in our laboratory: Using NEAT and CPPNs to generate the shape of a soft robot

- What is a soft robot

- How this is done: NEAT + HyperNEAT
  - Explain Hyperneat: Neat used to generate a CPPN

- Challenge: Developing the Body and the brain networks at the same time.

- Usage: Biological robots based on soft robots.

# Extra Topics
- The bibites: Alife simulation using NEAT

- PushGP: Genetic Programming using heaps. Good for more complex programs.
