

from graphviz import Digraph

def parser():
    dot = Digraph()

    dot.node('A', 'Inicio')
    dot.node('B', 'Proceso')
    dot.node('C','Fin')

    dot.edges(['AB', 'BC'])

    dot.render('mi_grafo', view=True)