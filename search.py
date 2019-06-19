# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
#    "*** YOUR CODE HERE ***"
    from util import Stack
    from game import Directions

    stack=Stack()
    visited=[]

    stack.push((problem.getStartState(),[]))
    solution=search(stack,problem,visited)#search is another function implemented
    return solution

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # "*** YOUR CODE HERE ***"
    from util import Queue
    from game import Directions

    queue = Queue()
    visited = []
    queue.push((problem.getStartState(), []))
    solution=search(queue, problem, visited)#search is another function implemented
    return solution

    util.raiseNotDefined()

def search(queueOrStack,problem,visited):
    while not queueOrStack.isEmpty():
        cur_cdn, cur_actions = queueOrStack.pop()
        #print actions
        if problem.isGoalState(cur_cdn):
            return cur_actions
        if cur_cdn not in visited:
            visited.append(cur_cdn)
            succ = problem.getSuccessors(cur_cdn)
            i=0
            while i<len(succ):
                coordinate=succ[i][0]
                nextStep=succ[i][1]
                if (coordinate not in visited):
                    allStep=cur_actions+[nextStep]
                    queueOrStack.push((coordinate,allStep))
                i=i+1

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import  PriorityQueue

    pQueue = util.PriorityQueue()
    visited = []
    pQueue.push((problem.getStartState(), []),0)
    temAction=[]
    while not pQueue.isEmpty():
        cur_cdn,cur_actions = pQueue.pop()
        actions = cur_actions
        if problem.isGoalState(cur_cdn):
            return cur_actions
        if cur_cdn not in visited:
            succ = problem.getSuccessors(cur_cdn)
            visited.append(cur_cdn)
            i = 0
            while i < len(succ):
                state=succ[i]
                temAction = cur_actions + [state[1]]
                toCost = problem.getCostOfActions(temAction)
                if (state[0] not in visited):
                    pQueue.push((state[0], actions + [state[1]]), toCost)
                else:
                    if (state[2] > toCost):
                        pQueue.update(
                            (state[0], actions + [state[1]], state[2] + problem.getCostOfActions(state[1])))
                i = i + 1

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #"*** YOUR CODE HERE ***"
    pQueue=util.PriorityQueue()
    actions=[]
    pQueue.push((problem.getStartState(),actions),0)
    visited=[]

    while not pQueue.isEmpty():
        cur_cdn, cur_actions = pQueue.pop()
        if problem.isGoalState(cur_cdn):
            return cur_actions
        if cur_cdn not in visited:
            visited.append(cur_cdn)
            succ = problem.getSuccessors(cur_cdn)
            i=0
            while i<len(succ):
                coordinate=succ[i][0]
                nextStep=succ[i][1]
                gn=problem.getCostOfActions(cur_actions + [nextStep])
                hn= heuristic(coordinate, problem)
                next_cost = gn+hn
                if (coordinate not in visited):
                    allStep=cur_actions+[nextStep]
                    pQueue.push((coordinate,allStep),next_cost)
                i=i+1

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
