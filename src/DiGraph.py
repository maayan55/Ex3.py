from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    V = {}
    N_in = {}
    N_out = {}
    total_E = {}
    key = int()
    nodeSize = int()
    edgeSize = int()
    mc = int()

    def __init__(self):
        self.V = {}
        self.N_in = {}
        self.N_out = {}
        self.total_E = {}
        self.key = 0
        self.nodeSize = 0
        self.edgeSize = 0
        self.mc = 0

    def v_size(self) -> int:

        return self.nodeSize

    def e_size(self) -> int:

        return self.edgeSize

    def e_size_by_id(self,id1) -> int:

        if id1 in self.total_E.keys():
            return self.total_E[id1]
        return 0

    def get_all_v(self) -> dict:

        return self.V

    def get_all_values(self) -> dict:

        return self.V.values()

    def get_items(self) -> dict:

        return self.V.items()

    def get_v_keys(self) -> dict:

        return self.V.keys()

    def all_in_edges_of_node(self, id1: int) -> dict:

        return self.N_in[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:

        return self.N_out[id1]

    def get_mc(self) -> int:

        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if id1 != id2 and id1 in self.V and id2 in self.V and id1 in self.N_in \
                and id2 in self.N_in and id1 in self.N_out and id2 in self.N_out \
                and id1 not in self.N_in[id2] and id2 not in self.N_out[id1]:
            self.N_out[id1][id2] = float(weight)
            self.N_in[id2][id1] = float(weight)
            self.mc += 1
            self.total_E[id1] += 1
            self.total_E[id2] += 1
            self.edgeSize += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:

        if node_id not in self.V and node_id not in self.N_in and node_id not in self.N_out:
            node = Node(node_id, "", 0, 0, pos)
            self.V[node_id] = node
            self.N_out[node_id] = {}
            self.N_in[node_id] = {}
            self.key += 1
            self.total_E[node_id] = 0
            self.nodeSize += 1
            self.mc += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:

        if node_id in self.V:
            inComingEdges = self.all_in_edges_of_node(node_id).keys()
            outGoingEdges = self.all_out_edges_of_node(node_id).keys()
            removedEdges = 0
            for x in inComingEdges:
                del self.N_out[x][node_id]
                removedEdges += 1
            for x in outGoingEdges:
                del self.N_in[x][node_id]
                removedEdges += 1

            del self.N_in[node_id]
            del self.N_out[node_id]
            del self.V[node_id]
            del self.total_E[node_id]
            self.edgeSize -= removedEdges
            self.nodeSize -= 1
            self.mc += 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if node_id1 != node_id2 and node_id1 in self.V and node_id2 in self.V and node_id2 in self.N_out[node_id1] and node_id1 in self.N_in[node_id2]:

            self.N_in[node_id2].pop(node_id1)
            self.N_out[node_id1].pop(node_id2)
            self.mc += 1
            self.edgeSize -= 1
            return True
        else:
            return False

    def __str__(self) -> str:
        str = "Vertices: {}, Edges: {}, MC: {}\n".format(self.nodeSize , self.edgeSize, self.mc)
        for element in self.V.values():
            for ni in self.N_out[element.getKey()].keys():
                str += "({0} -> {1}) w = {2}, \n".format(element.getKey(), ni, self.N_out[element.getKey()][ni])
        return str