import math

from utils import create_test_cyclic_directed_weighted_graph


def bellman_ford(graph):
  n = len(graph)
  dist = [math.inf] * n
  start_node_index = 0
  dist[start_node_index] = 0

  for i in range(0, n):
    for current_node_index in range(0, n):
      neighbours = graph[current_node_index]
      for [next_node_index, next_node_weight] in neighbours:
        if dist[next_node_index] > dist[current_node_index] + next_node_weight:
          dist[next_node_index] = dist[current_node_index] + next_node_weight

  for current_node_index in range(0, n):
    neighbours = graph[current_node_index]
    for [next_node_index, next_node_weight] in neighbours:
      if dist[next_node_index] > dist[current_node_index] + next_node_weight:
        dist[next_node_index] = -math.inf

  return dist


def main():
  graph = create_test_cyclic_directed_weighted_graph()
  print(bellman_ford(graph))


if __name__ == '__main__':
    main()