starting_graph = { "A": ["B", "C", "D"],
          "B": ["A", "E"],
          "C": ["A", "D"],
          "D": ["A", "C", "F"],
          "E": ["B", "G"],
          "F": ["D"],
          "G": ["E"]
          }

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


def bft(graph, start_node):
    bft_queue = Queue()
    visited = []
    bft_queue.enqueue(start_node)

    while not bft_queue.is_empty():
        current_node = bft_queue.dequeue()
        if current_node not in visited:
            visited.append(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                bft_queue.enqueue(neighbour)

    print(visited)

bft(starting_graph, "A")