import networkx as nx
import matplotlib.pyplot as plt 
from networkx.utils import is_string_like, open_file, make_str
def divide(G1):
    RandomG=nx.Graph()#creating an empty graph
    ScalefreeG=nx.Graph()#creating an empty graph
    G=nx.Graph()#creating an empty graph
    G.add_nodes_from(G1)
    G.add_edges_from(G1.edges)
    ScalefreeG.add_nodes_from(G1)
    ScalefreeG.add_edges_from(G1.edges)
    i=0
    
    for node in G.nodes():
        j=0
        v=node
        for node in G.nodes():
            u=node
            t1=G.neighbors(u)
            t2=G.neighbors(v)
            
            
            if(v!=u and t1==t2):
                    #RandomG.add_nodes_from(G.neighbors(u))
                    ScalefreeG.add_node(u)
                    ScalefreeG.add_node(v)
                    ScalefreeG.add_edge(v,u)
           
    RandomG.remove_nodes_from(ScalefreeG.nodes)
    nx.write_pajek(RandomG, "RandomG2.net", encoding='UTF-8')
    nx.write_pajek(ScalefreeG, "ScalefreeG2.net", encoding='UTF-8')
                                 
    
    
# How to use:
def main():
    N=1048#the number of nodes in the network
    N=int(N/2)
    RandomG= nx.erdos_renyi_graph(N,0.01)
    edges=int(RandomG.number_of_edges()/4)
    nx.write_pajek(RandomG, "RandomG.net", encoding='UTF-8')

    #nx.draw(RandomG, with_labels=False) 
    
    ScaleFree= nx.barabasi_albert_graph(N,edges)
    #nx.draw(ScaleFree, with_labels=False) 
    nx.write_pajek(ScaleFree, "ScaleFree.net", encoding='UTF-8')

   
    G=nx.compose(ScaleFree,RandomG)#merge the clusters
    #nx.draw(G, with_labels=False) 
    #plt.show()
    nx.write_pajek(G, "mixed.net", encoding='UTF-8')
    divide(G)#divide the graph into scale free model and random model

    
if __name__ == '__main__':
    main()