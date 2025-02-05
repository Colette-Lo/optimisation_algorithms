starting_graph = {"A": {"B": 4, "C": 3, "D": 2},
                  "B": {"A": 4, "E": 4},
                  "C": {"A": 3, "D": 5},
                  "D": {"A": 2, "C": 5, "F": 2},
                  "E": {"B": 4, "G": 2},
                  "F": {"D": 2, "G": 10},
                  "G": {"E": 2, "F": 10}
         }
##----------------------------------------------------------------------------------------------------------------------
##                                                Separate dictionaries
##----------------------------------------------------------------------------------------------------------------------

# def dijkstra(graph, start, end):
#    """
#    This is the simplest form of dijkstra's, using three separate dictionaries to store each data point, one for distance
#    to starting node, one for visited nodes, and one for the previous node. Slightly easier to program and trace through.
#    """
#    # Create separate dictionaries for all columns in table
#    node_distance = {}
#    node_visited = {}
#    previous_node = {}
#
#    # Setup default values in all columns for each node
#    for node in graph.keys():
#        node_distance[node] = None
#        node_visited[node] = False
#        previous_node[node] = ""
#
#    # Set starting node to have distance of 0
#    node_distance[start] = 0
#
#    # Loop while there are still nodes that haven't been visited
#    nodes_to_visit = True
#    while nodes_to_visit:
#
#        # 1. Find the node with the shortest distance from the start that has not been visited --------------------------
#
#        shortest = None
#        for node, distance in node_distance.items():
#            # Only check nodes that haven't been visited
#            if not node_visited[node]:
#                # If shortest is empty or shortest has no distance
#                if shortest is None or node_distance[shortest] is None:
#                    shortest = node
#                # if new distance is lower than current distance, replace node as shortest
#                elif distance is not None and distance < node_distance[shortest]:
#                    shortest = node
#
#        # 2. Calculate the total distance to the start for each connected unvisited node. If the new distance is lower
#        # than before, change it and reset the previous node ------------------------------------------------------------
#
#        # Loop through all the current node's unvisited neighbours
#        for neighbour, cost in graph[shortest].items():
#            if not node_visited[neighbour]:
#
#                if node_distance[neighbour] is None or cost + node_distance[shortest] < node_distance[neighbour]:
#
#                    # if the new distance to start is lower than current one, replace distance in distance dict
#                    node_distance[neighbour] = cost + node_distance[shortest]
#
#                    # 4. Replace previous node in previous_node dict if the distance has changed ------------------------
#                    previous_node[neighbour] = shortest
#
#
#        # 3. Set current node as visited --------------------------------------------------------------------------------
#        node_visited[shortest] = True
#
#        # 5. Check if there are still nodes to visit --------------------------------------------------------------------
#        nodes_to_visit = False
#        for node, visited in node_visited.items():
#            if not visited:
#                nodes_to_visit = True
#                break
#
#        # Debug code
#        # for node in graph.keys():
#        #     print("Node: {}, Distance: {}, Visited: {}, Previous: {}".format(node, node_distance[node], node_visited[node], previous_node[node]))
#        # input()
#
#    # 6. After distances have all been calculated, create the final path by following the trail of previous nodes -------
#    final_path = []
#    current_pos = end
#    final_path.insert(0, current_pos)
#    while current_pos != start:
#        current_pos = previous_node[current_pos]
#        final_path.insert(0, current_pos)
#
#    print(final_path)
# dijkstra(starting_graph, "A", "G")


##----------------------------------------------------------------------------------------------------------------------
##                                          Combined dictionary with popping
##----------------------------------------------------------------------------------------------------------------------
# def dijkstra(graph, start, end):
#    # Single dictionary that stores all the relevant information about a single node, including its distance and the
#    # previous node. Each item in the dictionary represents one row in the table.
#    combined_dictionary = {}
#
#    # Set each row to the default starting state: distance is infinite, and previous is empty
#    for node in graph.keys():
#        combined_dictionary[node] = {"Distance": None, "Previous": ""}
#
#     # Set starting point to have a distance of 0
#    combined_dictionary[start]["Distance"] = 0
#
#    # Since this algorithm works based on popping, there is no need to track visited nodes. After a node has been visited
#    # it is removed from the graph (NOT FROM THE DICTIONARY), therefore is effectively treated as 'visited'
#    # 5. Check if there are still nodes to visit ------------------------------------------------------------------------
#    while graph:
#        # 1. Find the node with the shortest distance from the start that has not been visited --------------------------
#        shortest = None
#        for node in graph.keys():
#            # If there is no shortest node, set current node to be shortest
#            if shortest is None:
#                shortest = node
#            # If current node has a distance lower than current shortest node, replace shortest
#            elif combined_dictionary[node]["Distance"] is not None and combined_dictionary[node]["Distance"] < combined_dictionary[shortest]["Distance"]:
#                shortest = node
#
#        # 2. Calculate the total distance to the start for each connected unvisited node. If the new distance is lower
#        # than before, change it and reset the previous node ------------------------------------------------------------
#
#        # Loop through each neighbour
#        for neighbour, cost in graph[shortest].items():
#            # If neighbour exists in the graph (hasn't been popped) and new distance is less than current cost
#            if neighbour in graph and (combined_dictionary[neighbour]["Distance"] is None or cost + combined_dictionary[shortest]["Distance"] < combined_dictionary[neighbour]["Distance"]):
#                # Set distance to be the new calculated distance
#                combined_dictionary[neighbour]["Distance"] = cost + combined_dictionary[shortest]["Distance"]
#                # 4. Set previous node to be current node only when distance has changed --------------------------------
#                combined_dictionary[neighbour]["Previous"] = shortest
#
#        # 3. Set current node to visited (in this case, remove it from the graph) ---------------------------------------
#        graph.pop(shortest)
# ##        # Debug code
# ##        for node, info in combined_dictionary.items():
# ##            print("Node: {}, Distance: {}, Previous: {}".format(node, info["Distance"], info["Previous"]))
# ##        input()
#
#    # 6. Once all nodes have been visited (no more nodes exist in graph), find final route ------------------------------
#    final_path = []
#    current_pos = end
#    final_path.insert(0, current_pos)
#    while current_pos != start:
#        current_pos = combined_dictionary[current_pos]["Previous"]
#        final_path.insert(0, current_pos)
#
#    print(final_path)
# dijkstra(starting_graph, "A", "G")


####---------------------------------------------------------------------------------------
####                                  Priority queues
####---------------------------------------------------------------------------------------
##class PriorityQueue:
##    def __init__(self):
##        self.queue_list = []
##
##    def enqueue(self, data, priority):
##        insert_position = 0
##
##        for i in range(len(self.queue_list)):
##            if priority < self.queue_list[i][1]:
##                insert_position = i
##                break
##
##        self.queue_list.insert(insert_position, [data, priority])
##
##    def dequeue(self):
##        data = self.queue_list.pop(0)
##        return data[0]
##
##    def is_empty(self):
##        if len(self.queue_list) == 0:
##            return True
##        else:
##            return False
##
##    def print_queue(self):
##        print(self.queue_list)
##
##def dijkstra(graph, start, end):
##    combined_dictionary = {}
##    prio_queue = PriorityQueue()
##
##    for node in graph.keys():
##        combined_dictionary[node] = {"Distance": None, "Previous": ""}
##
##    combined_dictionary[start]["Distance"] = 0
##    prio_queue.enqueue(start, 0)
##
##    while not prio_queue.is_empty():
##        shortest = prio_queue.dequeue()
##
##        for neighbour, cost in graph[shortest].items():
##            if neighbour in graph and (combined_dictionary[neighbour]["Distance"] is None or cost + combined_dictionary[shortest]["Distance"] < combined_dictionary[neighbour]["Distance"]):
##                combined_dictionary[neighbour]["Distance"] = cost + combined_dictionary[shortest]["Distance"]
##                combined_dictionary[neighbour]["Previous"] = shortest
##                prio_queue.enqueue(neighbour, cost + combined_dictionary[shortest]["Distance"])
##
##
####        for node, info in combined_dictionary.items():
####            print("Node: {}, Distance: {}, Previous: {}".format(node, info["Distance"], info["Previous"]))
####        input()
##
##    # After distances have all been calculated, create the final path by following the trail of previous nodes
##    final_path = []
##    current_pos = end
##    final_path.insert(0, current_pos)
##    while current_pos != start:
##        current_pos = combined_dictionary[current_pos]["Previous"]
##        final_path.insert(0, current_pos)
##    print(final_path)
##
##dijkstra(graph, "A", "G")



