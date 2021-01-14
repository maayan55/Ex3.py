# Ex3
חשוב לי לציין למען היושרה וההגינות שהתקשיתי ונעזרתי בקודים שראיתי באינטרנט

*This project implements algorithms in Python for developing a data structure into a directional weighted graph.
The graph contains vertices and weighted edges between each 2 vertices.

*DiGraph class algorithms

v_size()	Returns the number of vertices in this graph.
e_size()	Returns the number of edges in this graph.
e_size_by_id()	Returns the number of edges in this graph for the desired node.
get_all_v()	Returns a dictionary view of all existing vertices in the graph in format of {key: Integer, value: Node}.
get_all_values()	Returns a dictionary of all the values in the graph (Node Objects).
get_items()	Returns a dictionary view of all the items contained in the graph.
get_v_keys()	Returns a dictionary view of all the keys contained in the graph.
all_in_edges_of_node()	Returns a dictionary of the nodes connected to it (heads).
all_out_edges_of_node()	Returns a dictionary of the nodes it is connected to (tails).
get_mc()	Returns the current amount of changes made to the graph.
addEdge()-	Adds an edge to the graph when id1 is the head and id2 is the tail.
add_node()-	Adds a new node to the graph, in case the node already exists in the graph it will not be added again.
remove_node()-	Removes a node from the graph by the specified id.
removeEdge()	Removes an edge from the graph, when id1 is the head and id2 is the tail.

*GraphAlgo class algorithms

createTransposedGraph()	Generate a new DiGraph with the reversed directions of the edges of the original graph.	
setAllTags()	Resets the tags of all the Node in the graph.
getAllTags()	Returns the tags of all the Node in the graph.
setAllWeightAndInfo()	Sets the weight and info to all the Nodes.
printAllTags()	Prints all the tags.
get_graph()	Returns the DiGraph which the algorithms are operated on.
get_transposed_graph()	Returns the transposed Digraph.
load_from_json()	Loads a DiGraph from a json file format.
save_to_json()	Saves a DiGraph to a json file format.
splitPos()	Splits the string received from a json file to the pos of the Node.
shortest_path()	Finds the shortest path between two given node id.
connected_component()	Returns a List representing the SCC related to a given vertex.
connected_components()	Returns a List of lists containing all the SCC of the given graph.
plot_graph()	Display the graph in a graphics window.




