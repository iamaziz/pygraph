import sys
sys.path.append("../../pygraph")
from pygraph.dgraph import *

# input file path
fpath = "dataset/kb-body.csv"

# graph the relations
g = PyGraph()
g.file_relations(fpath)
g.draw_graph('body-ontology')
