class: center, middle
# Introduction to Genetic Programming
Claus Aranha, 2022-11-15

![:scale 50%](img/GP_tree_big.png)

---
# Lecture Outline

In this lecture we study the concept of .redtext[Genetic Programming (GP)].

First we will learn the basic concepts of GP, and some simple code examples.

Then, we study modern implementations of GP, which are used to design
the architecture of Neural Networks.

Finally, we will see a example of contemporary research using GP.

## Topics for Today:

- What is Genetic Programming?
- Implementation of Simple GP
- Simple GP and the Pole Balancing Problem
- GP for Neural Networks
- Neuro Evolution of Augmenting Topologies (NEAT)
- Robot Morphology using Neuro Evolution

---
# 1. What is Genetic Programming?
## Evolutionary Computation

.boxyellow[
.boxlabel[Evolutionary Computation]

Evolutionary Computation (EC) is a family of techniques inspired by the natural process of evolution. The first EC techniques were developed around 1980.
]

Traditional Algorithms in the EC family include:
- Genetic Algorithms (GA)
- Evolution Strategies (ES)
- Differencial Evolution (DE)
- Genetic Programming (GP)

---
# 1. What is Genetic Programming?
## Outline of an EC Method

.cols[
.c50[
Evolutionary Computation methods follow the algorithm to the right.

To implement an EC, it is necessary to define:
- How to generate a random solution (Encoding)

- How to evaluate a solution (Fitness)

- How to generate new solutions (mutation/crossover)

]
.c50[
**General Evolutionary Computation Algorithm:**
.boxyellow[
.boxlabel[General EC Algorithm]

1) Generate a random set of solutions;

2) Evaluate the Fitness of those solutions;

3) Select the Solutions with highest Fitness;

4) Generate a new set of solutions, by mutation and crossover of the solutions selected in (3);

5) Return to (2)
]
]
]

---
# 1. What is Genetic Programming?
## When are EC Useful?

EC Methods have found to be useful for solving real problems with the following characteristics:

- It is difficult to calculate a solution, but it is easy to evaluate a solution.  
(NP-hard problems)

- The solution space is discontinuous, and/or very high dimensional.

- We are interested in creative and unusual solutions.

.redtext[Creating Programs has all the characteristics above].  
Because of this, many people have studied **Genetic Programming** in the last 30 years.

---
# 1. What is Genetic Programming?
## EC for creating Programs

> **Genetic Programming** is an Evolutionary Computation Method that is used to generate computer programs.

### Difficulties in Genetic Programming

- How to generate a random solution (Encoding): .redtext[How do we represent a program?]

- How to evaluate a solution (Fitness): .redtext[This one is relatively easy]

- How to generate new solutions (mutation/crossover) .redtext[How do we "mutate" programs?]

---
# 1. What is Genetic Programming?
## Simple GP

The "traditional" GP (Simple GP) uses a .redtext[Tree Representation] of
programs.

This represents a computer program as a tree structure, with the inputs as
the leaf nodes, and the output as the root note.

For example, the tree below represents the program XXXXX

TODO

---
# 1. What is Genetic Programming?
## Simple GP Operators
- Arity
- Inputs
- Constants

---
# 1. What is Genetic Programming
## Crossover and Mutation

---
# 1. What is Genetic Programming

---
# 2. Implementation of Simple GP
## Let's get Coding!

TODO:

We will create a code for simple GP to solve a regression problem.

You can download the code here:

---
# 2. Implementation of Simple GP
## The DEAP Library

---
# 2. Implementation of Simple GP
## GP Operators

---
# 2. Implementation of Simple GP
## Tree Generation

---
# 2. Implementation of Simple GP
## Evolutionary Loop

---
# 2. Implementation of Simple GP
## Symbolic Regression Example

---
# 2. Implementation of Simple GP
## Binary Parity Example

# 2. Implementation of Simple GP
## Bloat

---
# 3. Simple GP and the Pole Balancing Problem
## The AIGym Simple Controller Library

---
# 3. Simple GP and the Pole Balancing Problem
## Description of Pole Balancing V1

---
# 3. Simple GP and the Pole Balancing Problem
## Stochastic Fitness for Pole Balancing

We need to take several runs

---
# 3. Simple GP and the Pole Balancing Problem
## Setting up the GP for Pole Balancing

---
# 3. Simple GP and the Pole Balancing Problem
## Running and Analyzing the Results

---
# 4. GP for Neural Networks

---
# 5. Neuro Evolution of Augmenting Topologies

NEAT Paper

NEAT implementation for Pole Balancing

CPPN and Hyperneat

---
# 6. Robot Morphology using Neuro Evolution

Fabio Paper

---
# 7. Summary
- Things we learned:
- Things you should try to do:

---
# A. References

- [DEAP library for simple GP](https://deap.readthedocs.io/en/master/tutorials/advanced/gp.html)
- [OpenAI Gym Classic Control Problems](https://www.gymlibrary.dev/environments/classic_control/)
- [NEAT Library](https://neat-python.readthedocs.io/en/latest/neat_overview.html)
- [NEAT Paper](http://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf)
- [Soft Robot Morphology Code](https://github.com/fhtanaka/SGR)
