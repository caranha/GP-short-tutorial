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
## Mini Intro to Evolutionary Computation

Evolutionary Computation (EC) is the idea of **using the mechanism of
Natural Evolution to create computational systems.**

In nature, living creatures adapt to their environment through **natural
selection**, **genetic inheritance**, and **mutation**. These mechanisms
resulted in the large diversity of living beings that we have today.

Could we use a similar idea to create interesting and powerful computer programs?



.boxyellow[
.boxlabel[Many Techniques based in Evolutionary Computation have been developed since 1980s]

.cols[
.c50[
- Genetic Algorithms (GA)
- Evolution Strategies (ES)

]
.c50[
- Differencial Evolution (DE)
- Genetic Programming (GP)
]
]
]
---
# 1. What is Genetic Programming?
## When do we want to use Evolutionary Computation?

EC Methods have found to be useful for solving real problems with the following characteristics:

- It is difficult to calculate a solution, but it is easy to evaluate a solution.  
(NP-hard problems)

- The solution space is discontinuous, and/or very high dimensional.

- We are interested in creative and unusual solutions.

.boxyellow[
.boxlabel[Creating Programs with Evolutionary Computation]

Creating computer programs has all these characteristics: It is hard to create
a program, but it is easier to test an existing program. The task is
symbolic / discontinuous, and usually requires a lot of human creativity.

Because of this, there is a lot of interest in using Evolutionary Computation for
creating computer code.
]

---
# 1. What is Genetic Programming?
## Outline of an EC Method

.cols[
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
.c50[
Evolutionary Computation methods follow the algorithm to the left.

To implement an EC, it is necessary to define:
- How to generate a random solution (Encoding)

- How to evaluate a solution (Fitness)

- How to generate new solutions (mutation/crossover)

]
]

---
# 1. What is Genetic Programming?
## EC for creating Programs

> **Genetic Programming** is an Evolutionary Computation Method that is used to generate computer programs.

### Questions in Genetic Programming:

1. How to represent a program as a genome:  
.redtext[The choice of data structure is important. Can we create valid random programs in this data structure? Is the data structure flexible? How to represent loops/conditionals/subroutines?]

2. How to mutate/crossover a program:  
.redtext[How to deal with programs of different lengths. Will mutation/crossover break a program? Can we extract "functions" for mutation/crossover?]

3. How to evaluate a program:  
.redtext[Comparison of input/output. However, multiple, possibly infinite, input/output pairs. Stochastic input/output pairs]

---
# 1. What is Genetic Programming?
## Simple GP

The "traditional" GP (Simple GP) represents programs as a .redtext[Tree], where
the **leaf nodes are the input** and the **root node is the output**.

.cols[
.c70[
The tree to the right is equivalent to the following program:

`mul(neg(add(mul(X, mul(X, X)), X)), sub(-1, X))`

Which we can simplify as:

`y = (-1 * (X + X^3)) * (-1 - X)`

or, equivalently:

`y = X + X^2 + X^3 + X^4 `

**Note that any subtree is a valid GP tree!**

]
.c30[
![:scale 80%](img/symbreg_tree1.png)


]
]

---
# 1. What is Genetic Programming?
## Creating the Simple GP Tree

To create the Simple GP tree, we need to define the **Operators** and the **Terminals**.


- Arity
- Inputs
- Constants

---
# 1. What is Genetic Programming
## Evolutionary Loop:
- Generate the Initial Population
- Evaluate the Population
- Select by Fitness
- Crossover and Mutation
- Repeat

---
# 1. What is Genetic Programming
## Summary of Simple GP:
- We want to create tree

Any questions so far?

---
# 2. Implementation of Simple GP
## Let's get Coding!

In this section, I will show how to program a Simple GP.

You can follow the code here:
https://github.com/caranha/GP-short-tutorial

![:scale 30%](img/repository.png)

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
