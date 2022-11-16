# Simple Implementation of Genetic Programming
# Solves several problems, and uses different kinds of operators.

import operator, math, random
import numpy

from deap import algorithms, base, creator, tools, gp

import pygraphviz as pgv


################################################
# Function to Plot the tree
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
# Functions for the toy problems:

## Symbolic Regression (one input, one output)
symbreg_input = [ x/10. for x in range(-10, 10) ]
def symbreg(x):
    return x**4 + x**3 + x**2 + x

def eval_symbreg(func):
    sq_errors = ((func(x) - symbreg(x))**2 for x in symbreg_input)
    return sum(sq_errors) / len(symbreg_input),


## Fibonacci (One input, one output)
fib_input = [ x for x in range (0, 25) ]
def fibonacci(x):
    if x == 0 or x == 1:
        return x
    return fibonacci(x-1) + fibonacci(x-2)
fib_output = [ fibonacci(x) for x in fib_input] # precalculation

def eval_fibonacci(func):
    sq_errors = ((func(n) - fib_output[n])**2 for n in range(0, 25))
    return sum(sq_errors) / len(fib_output),

## Parity Function (N inputs, one output)
parity_N = 6
def bitarray(k):
    return [(k & 2**x) and 1 for x in range(parity_N)]
parity_input = [bitarray(x) for x in range(2**6)]
def parity(*bitarr):
    return 1 - sum(bitarr)%2
parity_output = [ parity(*x) for x in parity_input] # precalculation

def eval_parity(func):
    result = [func(*x) for x in parity_input]
    errors = sum([ x != y for x, y in zip (result, parity_output) ])
    return(errors),


####################################################
# Defining GP Operators / Terminals
## Operators for Symbolic Regression (fibonacci, symbreg)
def operators_symbreg():
    def protectedDiv(left, right):
        try:
            return left / right
        except ZeroDivisionError:
            return 1

    pset = gp.PrimitiveSet("MAIN", 1, "IN") # One Input
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

## Operators for Binary Logic (Parity)
def operators_logical():
    pset = gp.PrimitiveSet("MAIN", parity_N, "IN") # Parity_N inputs
    pset.addPrimitive(operator.and_, 2)
    pset.addPrimitive(operator.or_, 2)
    pset.addPrimitive(operator.xor, 2)
    pset.addPrimitive(operator.not_, 1)

    pset.addTerminal(1)
    pset.addTerminal(0)

    return pset

##############################################################
# Setting up DEAP

## Select the problem to solve:

# fitness_func = eval_symbreg
fitness_func = eval_fibonacci
# fitness_func = eval_parity

operator_set = operators_symbreg()
# operator_set = operators_logical()


## Define Generators (Object is PrimitiveTree, Goal is Minimization)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

## DEAP toolbox: (define functions for selection, mutation, crossover, etc)
toolbox = base.Toolbox()
toolbox.register("expr",
                 gp.genHalfAndHalf, pset=operator_set, min_=1, max_=2)
toolbox.register("individual",
                 tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population",
                 tools.initRepeat, list, toolbox.individual)
toolbox.register("compile",
                 gp.compile, pset=operator_set)

def eval(individual):
    return fitness_func(toolbox.compile(expr=individual))
toolbox.register("evaluate",
                 eval)

toolbox.register("select",
                 tools.selTournament, tournsize=3)
toolbox.register("mate",
                 gp.cxOnePoint)
toolbox.register("expr_mut",
                 gp.genFull, min_=0, max_=2)
toolbox.register("mutate",
                 gp.mutUniform, expr=toolbox.expr_mut, pset=operator_set)

# Set up tree size limits
toolbox.decorate("mate",
                 gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate",
                 gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# Running the GP
def run_GP():
    POP_SIZE = 300
    GEN_SIZE = 80
    CROSSOVER_RATE = 0.5
    MUTATION_RATE = 0.1

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
    end_pop, log = algorithms.eaSimple(init_pop, toolbox,
                                       CROSSOVER_RATE,
                                       MUTATION_RATE,
                                       GEN_SIZE, stats=mstats,
                                       halloffame=hof, verbose=True)

    print("\nInformation about the best individual:")
    print("Expression: {}".format(hof[0]))
    print("Fitness: {:.5}".format(hof[0].fitness.values[0]))

    drawtree(hof[0], "besttree.png")

    # Fibonacci analysis:
    hof_func = gp.compile(hof[0], operator_set)
    for i in range(10):
        print("{}, {}".format(fibonacci(i), hof_func(i)))


    # TODO: Analyze the first generation and last generation separately
    # TODO: Graph the minimum and mean fitness and tree size

if __name__ == "__main__":
    run_GP()
