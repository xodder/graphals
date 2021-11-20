def create_test_directed_unweighted_graph():
  def add_edge(from_node, to_node):
    graph[from_node].append(to_node)

  n = 7
  graph = create_graph(n)
  add_edge(0, 1)
  add_edge(0, 2)
  add_edge(1, 3)
  add_edge(2, 3)
  add_edge(2, 4)
  add_edge(3, 5)
  add_edge(4, 5)
  add_edge(5, 6)

  return graph


def create_test_directed_unweighted_graph_with_bridges():
  def add_edge(from_node, to_node):
    graph[from_node].append(to_node)

  n = 9
  graph = create_graph(n)
  add_edge(0, 1)
  add_edge(1, 2)
  add_edge(2, 0)
  add_edge(2, 3)
  add_edge(2, 5)
  add_edge(3, 4)
  add_edge(5, 6)
  add_edge(6, 7)
  add_edge(7, 8)
  add_edge(8, 5)

  return graph


def create_test_directed_weighted_graph():
  def add_edge(from_node, to_node, weight):
    graph[from_node].append([to_node, weight])

  n = 8
  graph = create_graph(n)
  add_edge(0, 1, 3)
  add_edge(0, 2, 6)
  add_edge(1, 3, 4)
  add_edge(1, 4, 11)
  add_edge(2, 3, 8)
  add_edge(2, 6, 11)
  add_edge(3, 4, -4)
  add_edge(3, 5, 5)
  add_edge(3, 6, 2)
  add_edge(4, 7, 9)
  add_edge(5, 7, 1)
  add_edge(6, 7, 2)

  return graph


def create_test_cyclic_directed_weighted_graph():
  def add_edge(from_node, to_node, weight):
    graph[from_node].append([to_node, weight])

  n = 10
  graph = create_graph(n)
  add_edge(0, 1, 5)
  add_edge(1, 2, 20)
  add_edge(1, 5, 30)
  add_edge(2, 3, 10)
  add_edge(2, 4, 75)
  add_edge(3, 2, -15)
  add_edge(4, 9, 100)
  add_edge(5, 6, 5)
  add_edge(5, 8, 50)
  add_edge(5, 4, 25)
  add_edge(6, 7, -50)
  add_edge(7, 8, -10)
  add_edge(6, 7, 2)

  return graph


def create_graph(n):
  graph = []
  for i in range(0, n):
    graph.append([])
  return graph


def add_unweighted_directed_edge(graph, from_node, to_node):
  graph[from_node].append(to_node)
