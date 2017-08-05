#!/usr/bin/python

import sys


class Vertex():
    def __init__(self, name):
        self.name = name
        self.edges = []
        
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def __str__(self):
        return self.name

class Edge():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def __str__(self):
        return str(self.v1) + " to " + str(self.v2)

class WeightedEdge(Edge):
    def __init__(self, v1, v2, weight):
        Edge.__init__(self, v1, v2)
        self.weight = weight

    def __str__(self):
        return str(self.v1) + " to " + str(self.v2) + " = " + str(self.weight)

class Graph():
    def __init__(self):
        self.edges = []
        self.nodes = set()
        self.edge_dict = {}
    
    def add_edge(self, edge):
        self.edges.append(edge)
        self.edge_dict[edge.v1.name + "-" + edge.v2.name] = edge
        self.edge_dict[edge.v2.name + "-" + edge.v1.name] = edge
        self.nodes.add(edge.v1)
        self.nodes.add(edge.v2)
        edge.v1.add_edge(edge)
        edge.v2.add_edge(edge)
        
    def add_weighted_edge(self, v1, v2, weight):
        edge = WeightedEdge(v1, v2, weight)
        self.add_edge(edge)
      
    def get_edge(self, v1, v2):
        key_name = v1.name + "-" + v2.name
        if key_name not in self.edge_dict:
            key_name = v2.name + "-" + v1.name
        return self.edge_dict[key_name]
    
    def get_node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
    def __str__(self):
        s = ""
        for edge in self.edges:
            s = s + str(edge) + "\n"
        return s

    
class TreeNode():
    def __init__(self, name, graph_node=None):
        self.name = name
        self.children = []
        self.parent = None
        self.cost_to_parent = 0
        self.level = 0
        self.graph_node = graph_node
        
    def add_child(self, tree_node, cost):
        self.children.append(tree_node)
        tree_node.parent = self
        tree_node.cost_to_parent = cost
        tree_node.level = self.level + 1
        
    def __str__(self):
        s = "\t" * self.level + self.name + "\n"
        for tree_node in self.children:
            s = s + str(tree_node) + " "
        return s
    
def main():
    # A TSP tour in the graph is A -> B -> C -> D -> B -> A. 
    # The cost of the tour is 10 + 25 + 40 + 25 + 10 = 100.
    distances = [
        #  A   B   C   D 
        [  0, 10, 50, 45 ], # A
        [ 10,  0, 25, 25 ], # B
        [ 50, 25,  0, 40 ], # C
        [ 45, 25, 40,  0 ]  # D
        ]    
        
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    graph = Graph()
    graph.add_weighted_edge(a, b, 10)
    graph.add_weighted_edge(a, c, 50)
    graph.add_weighted_edge(a, d, 45)
    graph.add_weighted_edge(b, c, 25)
    graph.add_weighted_edge(b, d, 25)
    graph.add_weighted_edge(c, d, 40)
    #print graph

    visit_all(graph, a)
    
def visit_all(graph, starting_node):
    visited = []
        
    visit(graph, starting_node, starting_node, visited)
    #visited = visit_by_tree(graph, starting_node)
    print_tour(graph, starting_node, visited)
    
    
        
    
def visit(graph, starting_node, current_node, visited):
    visited_set = set(visited)
    min_weight = None
    selected_node = None
    for node in (graph.nodes - visited_set):
        if node.name != current_node.name and node.name != starting_node.name:
            edge = graph.get_edge(node, current_node)
            if min_weight == None or edge.weight < min_weight:
                min_weight = edge.weight
                selected_node = node
        elif len(graph.nodes - visited_set) == 1:
            selected_node = node
    visited.append(selected_node)
    
    if len(graph.nodes - visited_set) > 1:
        visit(graph, starting_node, selected_node, visited)
  
def print_tour(graph, starting_node, visited):
    print starting_node.name
    previous_node = starting_node
    total = 0
    for node in visited:
        if node.name == previous_node.name:
            previous_node = node
            continue
        edge = graph.get_edge(previous_node, node)
        print node, ": ", edge
        total = total + edge.weight
        previous_node = node
    print "              " + str(total)
    

def visit_by_tree(graph, starting_node):
    nodes_in_tree = set()
    root_tree_node = TreeNode(starting_node.name)
    nodes_in_tree.add(starting_node)
    build_tree_from_graph(graph, root_tree_node, nodes_in_tree)
    shortest_path = []
    visit_in_tree(root_tree_node, root_tree_node, 0, [ root_tree_node ], shortest_path)

    graph_visited = []
    for tree_node in shortest_path[0]:
        vertex = graph.get_node_by_name(tree_node.name)
        graph_visited.append(vertex)
    starting_node = graph.get_node_by_name(root_tree_node.name)
    
    return graph_visited
    #print_tour(graph, starting_node, graph_visited)
    
    

def visit_in_tree(starting_node, tree_node, total, visited, shortest_path):
    for node in tree_node.children:
        new_total = total
        new_visited = list(visited)
        new_visited.append(node)
        new_total = new_total + node.cost_to_parent
        if len(node.children) > 0:
            visit_in_tree(starting_node, node, new_total, new_visited, shortest_path)
        else:
            for node_to_find in starting_node.children:
                if node_to_find.name == node.name:
                    new_total = new_total + node_to_find.cost_to_parent
            new_visited.append(starting_node)
            if len(shortest_path) == 0:
                shortest_path.append(new_visited)
                shortest_path.append(new_total)
            elif new_total < shortest_path[1]:
                shortest_path[0] = new_visited
                shortest_path[1] = new_total

            

def build_tree_from_graph(graph, current_node, nodes_in_tree, level=0):
    nodes_in_tree.add(current_node)
    for node in (graph.nodes - nodes_in_tree):
        temp_nodes_in_tree = set(nodes_in_tree)
        # print '\t' * level, current_node.name, node.name
        edge = graph.get_edge(node, current_node)
        child_node = TreeNode(node.name)
        current_node.add_child(child_node, edge.weight)
        temp_nodes_in_tree.add(node)
        
        build_tree_from_graph(graph, child_node, temp_nodes_in_tree, level+1)

    
if __name__ == "__main__":
    main()
    
    