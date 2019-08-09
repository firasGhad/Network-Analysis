# Network-Analysis
1)my network contains 1048 node.
I built two clusters: 
One is random model with p=0.01 using the networkx library and erdos_renyi_graph(N,p) function
Second cluster is scale free model using barabsi_albert_graph(N,edges) function
They both have similar number of nodes and edges.
I merged the two cluster using the function compose(graph1,graph2)
2)I created visualization of the network using the function write_pajek(G,"path.net") of network.
3)I wrote a program to divide the graph into two cluster and I called it divide(G) which take graph as input ,it creates two empty graphs. One for the random model and the second is for the scale free one.
It does double loop, for each node in the input graph we do loop on the other nodes of the graph. For each two nodes in the graph.
if they have the same neighbors then we estimate that it for the scaleFree model cluster and so we add it to the new scale free graph that we create it.
We do this for all nodes.
And in the random model we copy the origin input graph and then remove from it all the nodes that in the scale free which lead us to the estimation that this a random model.

Random cluster visualization using pajek
 

Scale free model
 
The graph that contains the two clusters

The scale free model cluster after the dividing
 


Thank you.
