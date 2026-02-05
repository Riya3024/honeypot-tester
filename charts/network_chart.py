import matplotlib.pyplot as plt
import networkx as nx

def draw_scam_network(graph: nx.Graph):
    plt.figure(figsize=(10, 7))
    
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=900, font_size=8)
    plt.title("Scam Network: Bank → UPI → URL")
    plt.show()
