# Depth first traversal
starting_graph = { "A": ["B", "C", "D"],
          "B": ["A", "E"],
          "C": ["A", "D"],
          "D": ["A", "C", "F"],
          "E": ["B", "G"],
          "F": ["D"],
          "G": ["E"]
          }

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, new_item):
        self.stack_list.append(new_item)

    def stack_pop(self):
        return self.stack_list.pop(-1)

    def peek(self):
        if len(self.stack_list) > 0:
            return self.stack_list[-1]
        else:
            return None

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def print_stack(self):
        print("stack: ", self.stack_list)

class Queue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, new_item):
        self.queue_list.append(new_item)

    def dequeue(self):
        return self.queue_list.pop(0)

    def print_queue(self):
        print("Queue: ", self.queue_list)

    def is_empty(self):
        if len(self.queue_list) == 0:
            return True
        else:
            return False

def dft(graph, start_node):
    stack = Stack()
    visited = []

    current_node = start_node
    stack.push(current_node)
    visited.append(current_node)

    while not stack.is_empty():
        neighbor_found = False
        for node in graph[current_node]:
            if node not in visited:
                print(node, visited)
                neighbor_found = True
                current_node = node
                input()
        if not neighbor_found:
            stack.stack_pop()
            current_node = stack.peek()
        print(visited)

        stack.push(current_node)
        visited.append(current_node)
    print(visited)


dft(starting_graph, "A")