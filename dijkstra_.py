def get_information(path):
    #
    #
    return firstLine, edges_weight

def create_matrixes(edges):
    dict_edges = {}
    for edge in edges:
        aux_tuple = (int(edge[0]), int(edge[1]))
        dict_edges[aux_tuple] = int(edge[2])
    return dict_edges

def minimum(dict):
    min_key = list(dict.keys())[0]
    for i in list(dict.keys())[1:]:
        if dict[i] < dict[min_key]:
            min_key = i
    return(min_key)

def dijkstra(nodes, edges, start, end):
    unexplored = {node : float('inf') for node in nodes}
    unexplored[start] = 0
    while len(unexplored) != 0:
        explore = minimum(unexplored)
        if explore == end:
            break
        else:
            for path in edges.items():
                if path[0][0] == explore:
                    if path[0][1] in unexplored.keys():
                        check_weight = unexplored[path[0][0]] + path[1]
                        if check_weight < unexplored[path[0][1]]:
                            unexplored[path[0][1]] = check_weight
                elif path[0][1] == explore:
                    if path[0][0] in unexplored.keys():
                        check_weight = unexplored[path[0][1]] + path[1]
                        if check_weight < unexplored[path[0][0]]:
                            unexplored[path[0][0]] = check_weight
            print(unexplored)
            del unexplored[explore]
    return(unexplored[explore])

def main():
    path = ""
    nodes, edges = get_information(path)
    new_edges = []
    for edge in edges:
        edge = " ".join(edge.split())
        edge = edge.split(" ")
        new_edges.append(edge)

    dict_edges = create_matrixes(new_edges)
    start = 0
    end = 14
    print(dijkstra(nodes, dict_edges, start, end))

main()
