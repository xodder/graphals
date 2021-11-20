from utils import create_test_directed_weighted_graph
from topology_sort import top_sort
import math


def sssp(graph):
  n = len(graph)
  visited = [False] * n
  cost = [math.inf] * n
  ordering = top_sort(graph)
  prev = [-1] * n

  cost[ordering[0]] = 0

  for at in ordering:
    if not visited[at]:
      neighbours = graph[at]

      for [to, weight] in neighbours:
        if cost[to] > cost[at] + weight:
          cost[to] = cost[at] + weight
          prev[to] = at

    visited[at] = True

  return cost, prev


def main():
  graph = create_test_directed_weighted_graph()
  print(get_shortest_path(graph, 7))


def get_shortest_path(graph, to_node):
  from_node = 0
  path = []
  _, prev = sssp(graph)

  at = to_node
  while at != -1:
    path.append(at)
    at = prev[at]

  path.reverse()

  if path[0] is not from_node:
    return []
  else:
    return path


if __name__ == '__main__':
    main()