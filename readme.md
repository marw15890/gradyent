# Gradyent Python assignment

## About
This assignment is used to assess the Python capabilities of potential new Gradyent employees

## Theoretical background
Gradyent optimizes district energy networks. One import topic in network calculations is graph theory.
In this assignment you will program a bottom-up graph traversal algorithm. The purpose of this algorithm
is to calculate the sum of the values in all nodes by the given values in the starting nodes.
* It is a bottom-up traversal, which means that we have given values, and traverse up the graph
* We only take into account tree-like graphs, which means that there are no cycles
* Starting nodes are referred to as 'sinks'
* End nodes are referred to as 'sources'
* Nodes can be in any order (ExampleNetwork2 is an unordered example)

## Network details:
The following describes Example Network 1. The assignment also includes Example Network 2, 
which is a similar but differently ordered.

### Description:
Example network 1 contains 1 end node (node 9) and 3 starting nodes (node 0, 1, 2, and 3). The network is
specified by its starting nodes and an adjacency matrix, which tells to which nodes each node is connected.

### Schematic overview and example of traversal sum
    Starting nodes: {0, 1, 2, 3}                        Starting values: {0: [5], 1: [8], 2: [2], 3: [5]}
              9                                                        9: [20]
              |                                                           |
              8                                                        8: [20]
              |                                                           |
      3 - 6 - 7                                   3: [5] - 6: [5] - 7: [5+15=20]
              |                                                           |
              5                                                        5: [15]
              |                                                           |
              4                                                     4: [5+8+3=15]
            / | \                                                  /      |      \
           0  1  2                                            0: [5]   1: [8]   2: [2]

### The adjacency matrix:
In the following matrix you can see that node 0 is connected to node 4 by the 1 in row 0. You can also
see that node 4 is connected to node 0, 1, 2 and 5 by the 1's in row 4.

     0  1  2  3  4  5  6  7  8  9
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 3
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],  # 5
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],  # 6
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 9


## Assignment:
Write a method that can calculate the graph traversal sum for any network with {n} sinks and 1 source.
0. PREFERRED: This part might be skipped, it will be discussed with you when introducing the assignment
	Create a personal github repository with the initial files, commit your progress on github (preferably multiple commits to show your progress)
1. Write your code in the method "graph_traversal_sum"
    * Your method should work for the two simple example networks
    * Your method should be general enough that it runs for any other single-source tree-like network
    * Both the inputs and outputs are vectorized (should calculate {m} sets of values at the same time)
2. Validate your results with the given unit test "TestGraphTraversal.test_graph_traversal_sum"
3. Write a docstring for your method and add line comment in such a way that the code is understandable for others
4. OPTIONAL: Optimize the performance by profiling your method
5. Send us an email when finished, answering the following questions:
    * Did you manage to finish the assignments? (And if not, why not)
    * What did you find the most challenging?
    * What (internet) resources did you use?

## Rules:
* IMPORTANT: Only add or change code around the ToDo's. 
* Do not change anything in ExampleNetwork1, ExampleNetwork2 or TestGraphTraversal 
* You are allowed to use stackoverflow / google / etc. for reading about similar problems
* However, you are not allowed to copy full code snippets
* For the optional assignment: please commit your code BEFORE and AFTER the performance improvements

## Advice / hints:
* First spend some time reading information about graphs and graph traversal algorithms
* Read through the test code and try to understand the lay-out of the example network and test case
* Use the debugger and put a breakpoint in graph_traversal_sum to check which inputs you have to work with
* Only start optimizing your performance after you got an initial working version
* For the optional performance improvements: try using deque from collections