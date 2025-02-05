graph = {"A": {"B": 4, "C": 3, "D": 2},
         "B": {"A": 4, "E": 4},
         "C": {"A": 3, "D": 5},
         "D": {"A": 2, "C": 5, "F": 2},
         "E": {"B": 4, "G": 2},
         "F": {"D": 2, "G": 10},
         "G": {"E": 2, "F": 10}
         }

# Pre-calculated heuristics for each node. G is the target node, so heuristic is 0.
# Heuristic in this case is calculated as Euclidean distance
heuristics = {"A": 6,
              "B": 4,
              "C": 3,
              "D": 6,
              "E": 2,
              "F": 6,
              "G": 0}


def astar(graph, h, start, end) -> None:
    """
    This a-star is implemented with a separate dictionary for each data point per node.
    :param graph: The graph to traverse
    :param h: The pre-calculated heuristic for each node in the graph
    :param start: The starting node
    :param end: The target node
    """
    # g contains the flat calculated distance from start to current node
    g = {}

    # f contains the distance + the heuristic calculated
    f = {}

    # Previous node keeps track of the previous node visited
    previous_node = {}

    # Visited keeps track of whether the node has been set to the current node
    visited = {}

    # Set up each dictionary with default values
    for node in graph.keys():
        g[node] = None
        f[node] = None
        previous_node[node] = ""
        visited[node] = False

    # Set up starting node with default values
    g[start] = 0
    f[start] = h[start]

    # A-Star implementation

    # 1. While the destination has not been found ----------------------------------------------------------------------
    destination_found = False
    while not destination_found:

        # 2. Select the unvisited node with the lowest 'f' value. Store this node in variable 'shortest'
        shortest = None
        for node in graph.keys():
            if not visited[node]:
                if shortest is None or f[shortest] is None:
                    shortest = node
                elif f[node] is not None and f[node] < f[shortest]:
                    shortest = node

        # 2a. For each connetction to the current shortest node, calculate 'g' as in dijkstra's
        for neighbour, cost in graph[shortest].items():
            if not visited[neighbour] and (f[neighbour] is None or cost + g[shortest] + h[neighbour] < f[neighbour]):
                # 2b. If the result is lower than the neighbours current 'f' value (or there is no 'f' value)

                # 2bi. Set the selected neighbour node's 'g' value to be the newly calculated 'g' value
                g[neighbour] = cost + g[shortest]

                # 2bi (cont). Set the selected neighbour node's 'f' value to be based on new 'g' value
                f[neighbour] = cost + g[shortest] + h[neighbour]

                # 2bii. Set the previous node for the selected neighbour to be the current node
                previous_node[neighbour] = shortest

                # 1 (cont). Stop loop if the selected neighbour is the target node
                if neighbour == end:
                    destination_found = True

        # 2c. Set current node's visited tracker to True
        visited[shortest] = True

    # Debug line for printing every row in table after loop has completed
    for node in graph.keys():
        print("Node: {}, G: {}, H: {}, F: {}, Visited: {}, Previous: {}".format(node, g[node], h[node], f[node],
                                                                                visited[node], previous_node[node]))

    input()

    # 3. Retrace path from target node to start node to display calculated route
    final_path = [end]
    current_node = end
    while current_node != start:
        current_node = previous_node[current_node]
        final_path.insert(0, current_node)

    print(final_path)


astar(graph, heuristics, "C", "G")

astar
algorithm.py
Displaying
astar
algorithm.py.