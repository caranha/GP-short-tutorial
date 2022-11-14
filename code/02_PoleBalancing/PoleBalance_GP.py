# Simple Implementation of Genetic Programming
# Solves several problems, and uses different kinds of operators.

import operator, math, random
import numpy

from deap import algorithms, base, creator, tools, gp

import pygraphviz as pgv
import gym


################################################
# Tree plotting
def drawtree(t, filename):
    nodes, edges, labels = gp.graph(t)
    g = pgv.AGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    g.layout(prog="dot")

    for i in nodes:
        n = g.get_node(i)
        n.attr["label"] = labels[i]

    g.draw(filename)

###################################################
# Defining the problem to solve:
# AIGym Cartpole
# https://www.gymlibrary.dev/environments/classic_control/cart_pole/

# increasing the number of steps in the environment
env = gym.make("CartPole-v1")
reps = 10

def eval_cartpole(func):
    fitness = 0
    for i in range(reps):
        fitness += eval_cartpole_inside(func)

    return fitness,

def eval_cartpole_inside(func):
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
    return fitness



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


# Setting up DEAP

# GP tree with maximization Goal:
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

# DEAP toolbox:
## Change this for the problem you want to solve
fitness_func = eval_cartpole
operator_set = operators_symbreg()

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=operator_set, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=operator_set)

def eval(individual):
    return fitness_func(toolbox.compile(expr=individual))

toolbox.register("evaluate", eval)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=operator_set)

# Set up tree size limits
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# Running the GP
def run_GP():
    POP_SIZE = 300
    GEN_SIZE = 15


    init_pop = toolbox.population(n=POP_SIZE)
    hof = tools.HallOfFame(1)

    # Set up logging of statistics of the evolution
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", numpy.mean)
    mstats.register("std", numpy.std)
    mstats.register("min", numpy.min)
    mstats.register("max", numpy.max)

    # Perform the evolution all at once
    end_pop, log = algorithms.eaSimple(init_pop, toolbox, 0.5, 0.1,
                                       GEN_SIZE, stats=mstats,
                                       halloffame=hof, verbose=True)

    # TODO: Change the evolution loop to stop when maximum fitness is found

    print("\nInformation about the best individual:")
    print("Expression: {}".format(hof[0]))
    print("Fitness: {:.5}".format(hof[0].fitness.values[0]))

    drawtree(hof[0], "besttree.png")


    # TODO: Analyze the first generation and last generation separately
    # TODO: Graph the minimum and mean fitness and tree size

if __name__ == "__main__":
    run_GP()
