import math

from _pytest.python_api import RaisesContext

class Graph:
    def __init__(self):
        """Graph class constructor
        creates empty dictionary to store keys and values
        for the graph"""
        self.graph_dict = {}

    def add_vertex(self, label):
        """Adds a vertex to the graph
        vertex is an empty key"""
        if isinstance(label, str):
            self.graph_dict[label] = {} #vertex isn't connected to anything
            return self.graph_dict
        else:
            raise ValueError

    def add_edge(self, src, dest, w):
        """Connects two vertexes together and
        gives a weight for the distance between the
        two"""
        if src not in self.graph_dict or dest not in self.graph_dict: #checking that both src and dest are vertexes in graph
            raise ValueError
        if not isinstance(w, int):
            raise ValueError
        self.graph_dict[src][dest] = w #setting weight
        return self.graph_dict

    def get_weight(self, src, dest):
        if src not in self.graph_dict or dest not in self.graph_dict: #checking that both src and dest are vertexes in graph
            raise ValueError
        try:
            weight = self.graph_dict[src][dest]
            return weight
        except:
            return math.inf

    def dfs(self, starting_vertex):
        """Return a generator for traversing the graph in depth-first order
        starting from the specified vertex"""
        if starting_vertex not in self.graph_dict: #checking that starting_vertex is in graph
            raise ValueError

    def bfs(self, starting_vertex):
        """: Return a generator for traversing the graph in breadth-first order
        starting from the specified vertex"""
        if starting_vertex not in self.graph_dict: #checking that starting_vertex is in graph
            raise ValueError

    def dsp(self, src, dest):
        """: Return a tuple (path length , the list of vertices on the path from dest
        back to src), shortest path"""
        if src not in self.graph_dict or dest not in self.graph_dict: #checking that both src and dest are vertexes in graph
            raise ValueError

        if src == dest:
            return math.inf
        value = None
        def recursion(dict, address):
            if address == dest:
                return address       
            for value in self.graph_dict[src][address]:
                pass

        recursion(self.graph_dict[src], value)


        

    def dsp_all(self, src):
        """Return a dictionary of the shortest weighted path between src and all
        other vertices"""
        if src not in self.graph_dict: #checking that src vertex is in graph
            raise ValueError

    def __str__(self):
        """return string representation of graph"""
        pass

def main():
    test = Graph()
    test.add_vertex('A')
    test.add_vertex('B')
    test.add_vertex('C')
    test.add_vertex('D')
    test.add_vertex('E')

    test.add_edge('D', 'C', 5)
    # test.add_edge('D', 'A', 3)
    test.add_edge('E', 'B', 20)
    test.add_edge('E', 'D', 10)
    test.add_edge('A', 'C', 7)
    test.add_edge('C', 'B', 9)
    test.add_edge('B', 'A', 12)
    test.add_edge('C', 'E', 8)
    


    print(test.graph_dict)

    print("Distance to destination: ", test.dsp('D', 'A'), "miles.")

if __name__ == "__main__":
    main()