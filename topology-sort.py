from utils import create_test_directed_unweighted_graph


def top_sort(graph):
  n = len(graph)
  visited = [False] * n
  ordering = [None] * n
  last_ordering_index = n - 1

  for at in range(0, n):
    if not visited[at]:
      last_ordering_index = dfs(graph, at, visited, ordering, last_ordering_index)

  return ordering


def dfs(graph, at, visited, ordering, last_ordering_index):
  visited[at] = True
  neighbours = graph[at]

  for to in neighbours:
    next_node = to

    # caters for weighted graphs
    if isinstance(to, list):
      next_node = to[0]

    if not visited[next_node]:
      last_ordering_index = dfs(graph, next_node, visited, ordering, last_ordering_index)

  ordering[last_ordering_index] = at
  return last_ordering_index - 1


def main():
  graph = create_test_directed_unweighted_graph()
  ordering = top_sort(graph)
  print(ordering)


if __name__ == "__main__":
  main()
