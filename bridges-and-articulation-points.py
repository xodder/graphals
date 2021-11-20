import math

from utils import create_test_directed_unweighted_graph_with_bridges


def find_bridges(graph):
  n = len(graph)
  visited = [False] * n
  low = [math.inf] * n
  bridges = []
  ids = [-1] * n

  def dfs(current_node_index, parent_node_index, last_id):
    visited[current_node_index] = True
    ids[current_node_index] = low[current_node_index] = last_id + 1

    neighbours = graph[current_node_index]
    for next_node_index in neighbours:
      if next_node_index != parent_node_index:
        if not visited[next_node_index]:
          dfs(next_node_index, current_node_index, last_id + 1)
          low[current_node_index] = min(low[current_node_index], low[next_node_index])

          if ids[current_node_index] < low[next_node_index]:
            bridges.append((current_node_index, next_node_index))
        else:
          low[current_node_index] = min(low[current_node_index], ids[next_node_index])

  for current_node_index in range(n):
    if not visited[current_node_index]:
      dfs(current_node_index, -1, -1)

  return bridges


def find_articulation_points(graph):
  n = len(graph)
  visited = [False] * n
  is_articulation_point = [False] * n
  ids = [-1] * n
  low = [math.inf] * n

  def dfs(root_node_index, current_node_index, parent_node_index, last_id):
    visited[current_node_index] = True
    ids[current_node_index] = low[current_node_index] = last_id + 1

    out_edge_from_root_node_count = 0
    if root_node_index == parent_node_index:
      out_edge_from_root_node_count += 1

    neighbours = graph[current_node_index]
    for next_node_index in neighbours:
      if next_node_index != parent_node_index:
        if not visited[next_node_index]:
          out_edge_from_root_node_count += dfs(root_node_index, next_node_index, current_node_index, last_id + 1)
          low[current_node_index] = min(low[current_node_index], low[next_node_index])
          if ids[current_node_index] <= low[next_node_index]:
            is_articulation_point[current_node_index] = True
        else:
          low[current_node_index] = min(low[current_node_index], ids[next_node_index])

    return out_edge_from_root_node_count

  for current_node_index in range(n):
    if not visited[current_node_index]:
      out_edge_count = dfs(current_node_index, current_node_index, -1, -1)
      is_articulation_point[current_node_index] = out_edge_count > 1

  return [i for i in range(n) if is_articulation_point[i]]


def main():
  graph = create_test_directed_unweighted_graph_with_bridges()
  bridges = find_bridges(graph)
  print(bridges)
  articulation_points = find_articulation_points(graph)
  print(articulation_points)


if __name__ == '__main__':
    main()