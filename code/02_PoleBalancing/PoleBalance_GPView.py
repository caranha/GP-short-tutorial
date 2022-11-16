# Simple Implementation of Genetic Programming
# Solves several problems, and uses different kinds of operators.

import operator, math, random
import numpy

from deap import algorithms, base, creator, tools, gp

import pygraphviz as pgv
import gym

# increasing the number of steps in the environment
env = gym.make("CartPole-v1", render_mode="human")

def eval_cartpole(func):
    observation, info = env.reset()
    fitness = 0

    terminated = False
    truncated = False

    while not (terminated or truncated):
        try:
            if func(*observation) > 0: # action is 0 or 1
                action = 0
            else:
                action = 1
        except Exception as e:
            # Sometimes math domain errors happen
            # print(observation)
            # print(e)
            action = 0

        observation, reward, terminated, truncated, info = env.step(action)
        fitness += reward

    env.close()
    return fitness,

def random_action(i1, i2, i3, i4):
    return random.random()*2 -1


####################################################
# Defining GP Operators / Terminals
## Symbolic Regression Operators
def operators_symbreg():
    def protectedDiv(left, right):
        try:
            return left / right
        except ZeroDivisionError:
            return 1

    pset = gp.PrimitiveSet("MAIN", 4, "IN")
    # Four inputs (Position, Velocity, Angle, Angular velocity)
    pset.addPrimitive(operator.add, 2) # standard operators
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)
    pset.addPrimitive(protectedDiv, 2) # protected division

    # random constant terminal
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))

    return pset


# Creating a tree from a string
def GP_from_string(string):
    pset = operators_symbreg()
    gp_tree = gp.PrimitiveTree.from_string(string, pset)
    func = gp.compile(gp_tree, pset)
    return func

if __name__ == "__main__":
    # TODO: Load from commandline parameter
    # best0 = "neg(add(IN3, sin(IN2)))"
    best0 = "neg(1)"
    tree0 = GP_from_string(best0)


    # print(eval_cartpole(random_action))
    print(eval_cartpole(tree0))
