import math

from utils import create_test_directed_weighted_graph
from queue import PriorityQueue


def dijkstra(graph):
  n = len(graph)
  visited = [False] * n
  dist = [math.inf] * n
  prev = [-1] * n
  pq = PriorityQueue()

  start_node_index = 0
  dist[start_node_index] = 0
  pq.put((dist[start_node_index], start_node_index))

  while not pq.empty():
    current_node_dist, current_node_index = pq.get()
    visited[current_node_index] = True

    if dist[current_node_index] < current_node_dist:
      continue

    neighbours = graph[current_node_index]
    for [next_node_index, next_node_weight] in neighbours:
      if not visited[next_node_index]:
        if dist[next_node_index] > dist[current_node_index] + next_node_weight:
          dist[next_node_index] = dist[current_node_index] + next_node_weight
          pq.put((dist[next_node_index], next_node_index))
          prev[next_node_index] = current_node_index

  return dist, prev


def main():
  graph = create_test_directed_weighted_graph()
  print(get_shortest_path(graph, 7))


def get_shortest_path(graph, to_node):
  dist, prev = dijkstra(graph)
  path = []

  if dist[to_node] == math.inf:
    return path

  at = to_node
  while at != -1:
    path.append(at)
    at = prev[at]

  path.reverse()

  return path


if __name__ == '__main__':
    main()