""" Please see readme.md included in the same folder."""

import cProfile
import time
from unittest import TestCase

import numpy as np

# ToDo: OPTIONAL - Try to optimize the performance of your solution, enable the unit test by this switch
INCLUDE_OPTIONAL_ASSIGNMENT = True


def graph_traversal_sum(values_in, connections_in, nodes_start, nodes_end):
    """ ToDo: Write a docstring
    :param values_in:
    :param connections_in:
    :param nodes_start:
    :param nodes_end:
    :return:
    """
    # Make sure that original objects are not changed
    values = values_in.copy()
    connections = connections_in.copy()

    # ToDo: Write your code here, calculating the graph traversal sum

    # This function calculates the path from a given sink to the source
    def sink_path(connections_in, node_start, nodes_start, node_end, path=None, last_junction=None):
        path = path if path else [node_start]
        nodes_length = len(connections_in[node_start])
        next_node = [x for x in range(0, nodes_length) if connections_in[path[-1], x] == 1 and x not in nodes_start and x not in path]
        if len(next_node) > 1:
            last_junction = path[-1]
        for node in next_node:
            if node not in path:
                path.append(node)
                if node == node_end:
                    return path
                path = sink_path(connections_in, node_start, nodes_start, node_end, path, last_junction)
        if not next_node:
            index = len(path) - 1
            if last_junction is not None:
                index = path.index(last_junction) + 1
            path = path[0:index]
        return path

    paths = []
    for node in nodes_start:
        paths.append(sink_path(connections, node, nodes_start, node_end))

    def path_sum(connections_in, paths, values_in):
        nodes_length = len(connections_in[0])
        connections_out = np.zeros(shape=(nodes_length, nodes_length))
        for x in range(0, nodes_length):
            for y in range(0, nodes_length):
                if connections_in[x, y] > 0:
                    for path_index in range(0, len(paths)):
                        path = paths[path_index]
                        for i in range(0, len(path) - 2):
                            if path[i] == x and path[i + 1] == y:
                                connections_out[x, y] += values_in[path_index]
                        for i in range(len(path) - 1, 1, -1):
                            if path[i] == x and path[i - 1] == y:
                                connections_out[x, y] += values_in[path_index]
        return connections_out

    return values


class ExampleNetwork1:
    """ Definition of the first example network containing 10 nodes, of which 1 source (9) and 4 sinks (0, 1, 2, 3).

    Schematic overview:

              9
              |
              8
              |
      3 - 6 - 7
              |
              5
              |
              4
            / | \
           0  1  2

    """
    nodes = set(range(0, 10))
    nodes_start = {0, 1, 2, 3}
    nodes_end = {9}
    values_in = {0: 1, 1: 5, 2: 3, 3: 2}
    connections = np.array([
       # 0  1  2  3  4  5  6  7  8  9
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
    ])


class ExampleNetwork2:
    """ A second example network containing 10 nodes, of which 1 source (6) and 4 sinks (0, 1, 4, 9).

    Schematic overview:

              6
              |
              8
              |
          5 - 7 - 9
          |   |
          4   3
              |
              2
            / |
           0  1

    """
    nodes = set(range(0, 10))
    nodes_start = {0, 1, 4, 9}
    nodes_end = {6}
    connections = np.array([
       # 0  1  2  3  4  5  6  7  8  9
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 2
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 3
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 6
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],  # 7
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 9
    ])


class TestGraphTraversal(TestCase):

    def test_graph_traversal_sum(self):
        """ Runs the unit test for the graph traversal sum using a given graph traversal method. """
        # Run the test case for the given example network
        values_out1, _ = self._run_test_case_for_method(ExampleNetwork1, graph_traversal_sum,
                                                        number_of_executions=1, length=1000)
        # 'Node 4 should be sum of 0, 1, and 2'
        np.testing.assert_array_almost_equal(
            list(values_out1[:, 4]),
            list(values_out1[:, 0] + values_out1[:, 1] + values_out1[:, 2]),
            decimal=10,
            err_msg='Network1: Node 4 should be sum of 0, 1, and 2')
        # 'Node 6 should be same as 4'
        np.testing.assert_array_almost_equal(
            list(values_out1[:, 6]),
            list(values_out1[:, 3]),
            decimal=10,
            err_msg ='Network1: Node 6 should be same as 3')
        # 'Node 9 should be sum of 3 and 4'
        np.testing.assert_array_almost_equal(
            list(values_out1[:, 9]),
            list((values_out1[:, 3] + values_out1[:, 4])),
            decimal=10,
            err_msg='Network1: Node 9 should be sum of 3 and 4')

        # Run the test case for the second example network
        values_out2, _ = self._run_test_case_for_method(ExampleNetwork2, graph_traversal_sum,
                                                        number_of_executions=1, length=1000)
        # 'Node 7 should be sum of 5, 3, 9'
        np.testing.assert_array_almost_equal(
            list(values_out2[:, 7]),
            list(values_out2[:, 5] + values_out2[:, 3] + values_out2[:, 9]),
            decimal=10,
            err_msg='Network1: Node 7 should be sum of 5, 3, 9')
        # 'Node 6 should be same as 8'
        np.testing.assert_array_almost_equal(
            list(values_out2[:, 6]),
            list(values_out2[:, 8]),
            decimal=10,
            err_msg='Network1: Node 6 should be same as 8')
        # 'Node 6 should be sum of 4, 0, 1, 9'
        np.testing.assert_array_almost_equal(
            list(values_out2[:, 6]),
            list((values_out2[:, 4] + values_out2[:, 9] + values_out2[:, 0] + values_out2[:, 1])),
            decimal=10,
            err_msg='Network1: Node 9 should be sum of 3 and 4')

    def test_graph_traversal_sum_performance(self):
        """ Evaluates the performance of a given graph traversal method if the optional assignment is included. """
        if INCLUDE_OPTIONAL_ASSIGNMENT:
            # The goal in seconds of the average runtime
            average_run_time_goal = 0.001

            # Start the profiler
            pr = cProfile.Profile()
            pr.enable()

            # Run the test case for the given example network (a large number of times)
            values_out, average_run_time = self._run_test_case_for_method(ExampleNetwork1, graph_traversal_sum,
                                                                          number_of_executions=1000, length=10000)

            # Stop and print the profiling information
            pr.disable()
            pr.print_stats(sort="calls")

            # Try to get the run time below this value
            self.assertLess(average_run_time, average_run_time_goal,
                            msg=f'OPTIONAL: Try to get the average runtime to below {average_run_time_goal}.')
        else:
            # Do not test anything when the optional assignment is not included
            self.assertFalse(INCLUDE_OPTIONAL_ASSIGNMENT,
                             msg='The optional assignment is turned off, '
                                 'put "INCLUDE_OPTIONAL_ASSIGNMENT" to True to include it.')

    @staticmethod
    def _run_test_case_for_method(network_to_use, method_to_use, number_of_executions=1, length=10000):
        # Initialize the values for all nodes and the given length
        values = np.zeros((length, len(network_to_use.nodes)))
        # Create random values for all starting nodes
        values[:, list(network_to_use.nodes_start)] = np.random.random((length, len(network_to_use.nodes_start)))

        # Run an x-amount of times and note down the total execution time
        # NOTE: This is only relevant for the optional assignment, where you are optimizing the performance
        start = time.time()
        values_out = values.copy()
        for i in range(0, number_of_executions):
            values_out = method_to_use(values, network_to_use.connections,
                                       network_to_use.nodes_start,  network_to_use.nodes_end)
        end = time.time()
        run_time = end - start
        average_run_time = run_time / number_of_executions
        print(f'Execution time for {number_of_executions} run(s): {run_time}')

        return values_out, average_run_time
