
import os, sys, pathlib
from graphviz import Digraph

def bootstrap_graphviz():
    if hasattr(sys, "_MEIPASS"):
        root = pathlib.Path(sys._MEIPASS)
    else:
        root = pathlib.Path(__file__).parent / "resources"
    
    gv_bin = root / "graphviz" / "bin"
    os.environ["PATH"] = str(gv_bin) + os.pathsep + os.environ.get("PATH", "")
    os.environ["GRAPHVIZ_DOT"] = str(gv_bin / "dot.exe")

bootstrap_graphviz()

def main ():
    dot = Digraph()

    dot.node('A', 'Inicio')
    dot.node('B', 'Proceso')
    dot.node('C','Fin')

    dot.edges(['AB', 'BC'])

    dot.render('mi_grafo', view=True)


if __name__ == '__main__':
    main()