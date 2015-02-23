import sys
sys.path.append("../../pygraph")
from pygraph.dgraph import PyGraph

g = PyGraph()
g.add_relation('A likes B')
g.add_relation('A dislikes C')

g.draw_graph('graph1')

g.add_relation('B loves C')
g.add_relation('C likes B')

g.draw_graph('graph2')