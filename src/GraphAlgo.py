from typing import List
import json as Js
import math
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import random as r


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):

        self.tags = {}
        self.g = None if graph is None else graph
        self.mc = 0 if graph is None else graph.get_mc()
        self.nodeSize = 0 if graph is None else graph.v_size()
        self.edgeSize = 0 if graph is None else graph.e_size()
        self.transposed_graph = None if graph is None else self.createTransposedGraph(graph)

    def createTransposedGraph(self, graph) -> DiGraph:

        if self.g is None:
            return
        new_graph = DiGraph()
        for x in self.g.get_all_values():
            new_graph.add_node(x.getKey())
        for x in self.g.get_all_values():
            for e in self.g.all_out_edges_of_node(x.getKey()):
                new_graph.add_edge(e, x.getKey(), self.g.all_out_edges_of_node(x.getKey())[e])
        return new_graph

    def setAllTags(self, t: float):

        if self.g is None:
            return
        for x in self.g.get_all_values():
            self.tags[x] = t

    def getAllTags(self):
        return self.tags

    def setAllWeightAndInfo(self, t: float):
        """
        Sets the weight and info of all vertices in the graph to 't' and and empty string.
        :param t: the weight to set.
        """
        if self.g is None:
            return
        for x in self.g.get_all_values():
            x.setWeight(t)
            x.setInfo("")

    def printAllTags(self):
        if self.g is None:
            return
        for x in self.tags.items():
            print(x)

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        if self.g is None:
            return None
        return self.g

    def get_transposed_graph(self) -> GraphInterface:

        if self.transposed_graph is None:
            return None
        return self.transposed_graph

    def load_from_json(self, file_name: str) -> bool:

        try:
            new_graph = DiGraph()
            with open(file_name, 'r') as reader:
                json_graph = Js.load(reader)
                reader.close()
                edges = json_graph["Edges"]
                nodes = json_graph["Nodes"]
                for x in nodes:
                    pos = None
                    if 'pos' in x:
                        posString = x["pos"].split(",")
                        pos = (float(posString[0]), float(posString[1]), float(posString[2]))
                    new_graph.add_node(int(x["id"]), pos)
                for x in edges:
                    new_graph.add_edge(int(x["src"]), int(x["dest"]), float(x["w"])) # adding the edges
                self.g = new_graph
                return True
        except:
            # raise FileExistsError
            return False

    def save_to_json(self, file_name: str) -> bool:

        if self.g is None:
            return False
        my_dict = {}
        my_dict["Edges"] = []
        my_dict["Nodes"] = []
        for x in self.g.get_all_values():
            node_dict = {}
            node_dict["id"] = x.getKey()
            if len(x.getPosAsString()) > 0:
                node_dict["pos"] = x.getPosAsString()
            my_dict["Nodes"].append(node_dict)
            for e in self.g.all_out_edges_of_node(x.getKey()):
                edges_dict = {}
                edges_dict["src"] = x.getKey()
                edges_dict["w"] = self.g.all_out_edges_of_node(x.getKey())[e]
                edges_dict["dest"] = e
                my_dict["Edges"].append(edges_dict)
        try:
            with open(file_name, 'w') as writer:
                writer.write(Js.dumps(my_dict))
                return True
        except:
            # raise FileExistsError
            return False
        finally:
            writer.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        if self.g is None:
            return (-1,[])
        if id1 in self.g.get_v_keys() and id1 == id2:
            # only the node id
            my_tuple = (0, [self.g.get_all_v()[id1].getKey()])
            return my_tuple
        if id1 not in self.g.get_all_v().keys() or id2 not in self.g.get_all_v().keys():
            my_tuple = (-1, [])
            return my_tuple
        queue = [id1]
        self.setAllWeightAndInfo(-1)
        self.g.get_all_v()[id1].setWeight(0)
        info = "{}".format(id1)
        self.g.get_all_v()[id1].setInfo(info)
        while queue:
            node = queue.pop(0)
            for x in self.g.all_out_edges_of_node(node).keys():
                if self.g.get_all_v()[x].getWeight() == -1 or self.g.get_all_v()[x].getWeight() > self.g.get_all_v()[
                    node].getWeight() + self.g.all_out_edges_of_node(node)[x]:
                    self.g.get_all_v()[x].setWeight(
                        self.g.get_all_v()[node].getWeight() + self.g.all_out_edges_of_node(node)[x])
                    queue.append(x)
                    info = "{},{}".format(self.g.get_all_v()[node].getInfo(), x)
                    self.g.get_all_v()[x].setInfo(info)
        if self.g.get_all_v()[id2].getWeight() == -1:
            my_tuple = (math.inf, [])
            return my_tuple
        else:  # there's a path
            my_list = []
            for x in self.g.get_all_v()[id2].getInfo().split(','):
                my_list.append(int(x))
            my_tuple = (self.g.get_all_v()[id2].getWeight(), my_list)
            return my_tuple

    def connected_component(self, id1: int) -> list:

        if self.g is None or id1 not in self.g.get_all_v():
            return []
        my_list = self.connected_components()
        if my_list:
            for x in my_list:
                if id1 in x:
                    return x
        return []

    def connected_components(self) -> List[list]:

        if self.g is not None:
            result = []
            p = {}
            l = {}
            f = {}
            my_list = []
            i = 0
            keys = self.g.get_all_v().keys()
            for id in keys:
                if id not in f:
                    queue = [id]
                    while len(queue) > 0:
                        vertex = queue[-1]
                        if vertex not in p:
                            i = i + 1
                            p[vertex] = i
                        done = 1
                        niById = self.g.all_out_edges_of_node(vertex)
                        for w in niById:
                            if w not in p:
                                queue.append(w)
                                done = 0
                                break
                        if done == 1:
                            l[vertex] = p[vertex]
                            for w in niById:
                                if w not in f:
                                    if p[w] <= p[vertex]:
                                        l[vertex] = min([l[vertex], p[w]])
                                    else:
                                        l[vertex] = min([l[vertex], l[w]])
                            queue.pop()
                            if l[vertex] != p[vertex]:
                                my_list.append(vertex)
                            else:
                                f[vertex] = True
                                scc = [vertex]
                                while my_list and p[my_list[-1]] > p[vertex]:
                                    k = my_list.pop()
                                    f[k] = True
                                    scc.append(k)
                                result.append(scc)
            self.components = result
            return result

    def plot_graph(self) -> None:

        list_X = []
        list_Y = []
        for x in self.g.get_all_v().keys():
            for e in self.g.all_out_edges_of_node(x).keys():
                # print(self.g.get_all_v()[x].getPosAsString())
                listOfVector = self.splitPos(self.g.get_all_v()[x].getPosAsString())
                if listOfVector is not None:
                    list_X.append(listOfVector[0])
                    list_Y.append(listOfVector[1])

                listOfEdgesByX = self.splitPos(self.g.get_all_v()[e].getPosAsString())
                if listOfEdgesByX is not None:
                    list_X.append(listOfEdgesByX[0])
                    list_Y.append(listOfEdgesByX[1])

                plt.plot(list_X, list_Y, "*-b")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        return None

    def checkValue(self, checkList) -> list:
        if checkList[0] < 0:
            checkList[0] += 0.04
        else:
            checkList[0] -= 0.04

        if checkList[1] < 0:
            checkList[1] += 0.04
        else:
            checkList[1] -= 0.04
        return checkList

    def splitPos(self, pos: str) -> list:
        if pos == "":
            x = float((r.random() * 10) + 4)
            y = float((r.random() * 10) + 4)
            return [x, y]
        else:
            x = float(pos.split(",")[0])
            y = float(pos.split(",")[1])
            return [x, y]