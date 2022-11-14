#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.

# Modified by caranha 2022/11/06
# - Added output of final answer at the end
# - Moved some functions around to help explanation
# - Added some more explaining comments

import operator, math, random
import numpy

from deap import algorithms, base, creator, tools, gp

###
# This program uses Genetic Programming (GP) to solve
# a simple Symbolic Regression problem. The GP must find
# a function that calculates the same values as
# y = x**4 + x**3 + x**2 + x

###
# This is the hidden function that we want to find
# Because this is an example, we write it directly inside our
# fitness function

def evalSymbReg(individual, points):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    # Evaluate the mean squared error between the expression
    # and the real function : x**4 + x**3 + x**2 + x
    sqerrors = ((func(x) - x**4 - x**3 - x**2 - x)**2 for x in points)
    return math.fsum(sqerrors) / len(points),

##
# Set up the GP (1)
# First we define the operators that the GP is allowed to use:

# Define a new protected division function
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2) # standard operators
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(operator.neg, 1)
pset.addPrimitive(math.cos, 1)
pset.addPrimitive(math.sin, 1)
pset.addPrimitive(protectedDiv, 2) # protected division
# random constant terminal
pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
pset.renameArguments(ARG0='x')     # input terminal

##
# Set up the GP (2):
# Next we register the DEAP helper functions
# Deap will call these functions while running the evolutionary computation
# We could define more specific functions for harder problems.

# Objective is to minimize the fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# Individual is of type gp.PrimitiveTree
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# Set up DEAP generators for individual, population, and function
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

# Set up evolutionary operators
toolbox.register("evaluate", evalSymbReg, points=[x/10. for x in range(-10,10)])
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Set up tree size limits
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

##
# Run the GP
def main():
    random.seed(318)

    pop = toolbox.population(n=300)
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
    pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats,
                                   halloffame=hof, verbose=True)

    # Return the results
    return pop, log, hof

if __name__ == "__main__":
    pop, log, hof = main()

    print("\nInformation about the best individual:")
    print("Expression: {}".format(hof[0]))
    print("Fitness: {:.5}".format(hof[0].fitness.values[0]))
