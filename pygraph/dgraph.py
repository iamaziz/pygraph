__author__ = "Aziz Alto"
__email__ = "iamaziz.alto@gmail.com"
__date__ = "Feb. 2015"
__version__ = "0.1"

# repo: http://github.com/iamaziz/pygraph

# for pydot guide and attribute list, see:
# http://www.graphviz.org/doc/info/attrs.html


class PyGraph(object):
    """Create simple and quick Directed Graphs using relational statements (knowledge base)."""

    def __init__(self, graph_dict={}):
        self.graph_dict = graph_dict

    def draw_graph(self, output_image="pygraph-test", open_image=True, orientation="BT", label=True):
        """
        input:
            output_image: string name for the output graph
            open_image: optional boolean to open image after saving it.
            orientation: of the graph ["TB", "LR", "BT", "RL"] TobBottom, LeftRight, BottomTop, RightLeft
        return:
            the generated graph model (from the input relations) and save it.
        """

        try:
            import pydot
        except ImportError:
            print("pydot is not installed!")
            exit(0)

        graph = pydot.Dot(graph_type='digraph', rankdir=orientation)  # g_type=['graph', digraph],

        # build the graph
        if not self.graph_dict:
            print("Empyt graph, no realtions found!")
            raise ValueError

        for relation in self.graph_dict.items():
            concept, childs = relation
            if len(childs) > 0:
                for c in childs:
                    relation, child = c
                    src = pydot.Node(child)
                    dst = pydot.Node(concept)
                    if not label:
                        relation = ''
                    edge = pydot.Edge(dst, src, label=relation)

                    graph.add_edge(edge)

        # create output dir and save graph
        import os

        fig_dir = "pygraph-output/"
        if not os.path.exists(fig_dir):
            os.makedirs(fig_dir)

        output_image = output_image.replace(' ', '-')
        fig_name = fig_dir + output_image
        if not fig_name.lower().endswith('.png'):
            fig_name += ".png"

        # plot and save png
        graph.write_png(fig_name)

        # open png
        if open_image:
            os.system('open {}'.format(fig_name))

        return fig_name

    # input from a file
    def file_relations(self, file_name, delimiter=' ', reset=False):
        """
        Read knowledge base statements (relation between two nodes) from a file.

        input: 
            file_name: name of the file input (relational statements).
            delimiter: of the words, default a space.
            reset: start new instance of relations dictionary.
        return: a dictionary of the input relations.
        """

        if reset:
            self.graph_dict = {}
        relations = open(file_name, 'r').readlines()

        for r in relations:
            self.add_relation(r.strip(), delimiter)

        return self.graph_dict

    # module level relation entry
    def add_relation(self, statement, delimiter=' '):
        """add new relation into the graph dictionary
        
        delimiter: of the words, default a space.
        """
        # TODO: move assert to a unit test
        fragments = statement.split(delimiter)
        assert len(fragments) == 3, "wrong structure of the statement: {}".format(statement)

        if not self.find_relation(statement, delimiter):
            e1, r, e2 = fragments
            self.graph_dict.setdefault(e1, [])
            self.graph_dict.setdefault(e2, [])
            self.graph_dict[e1].append((r, e2))

    def find_relation(self, statement, delimiter):
        """make sure the relationship is not inserted previously"""
        node, r, relative = statement.split(delimiter)
        if node in self.graph_dict.keys() and (r, relative) in self.graph_dict[node]:
            print("relation exists! {} {} {} ".format(node, r, relative))
            return True
        else:
            return False


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser('pygraph')
    parser.add_argument("kb", help="file name of the relation sentences e.g. A is-a B", type=str)
    parser.add_argument("-d", help="print out the graph's dictionary")
    parser.add_argument("-n", help="name of the output graph file", type=str, default="test-file-graph")
    args = parser.parse_args()

    # Terminal args
    f = args.kb
    d = args.d
    gname = args.n

    g = PyGraph()

    # read relation statements from file
    g.file_relations(f)

    # show or draw the input graph
    if d:
        if d == 'show':
            print("current graph:\n {}".format(g.graph_dict))
        else:
            print("invalid args value!")
    else:
        g.draw_graph(gname)
