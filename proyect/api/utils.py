from antlr4 import *
from lenguage.GrammarLexer import GrammarLexer
from lenguage.GrammarParser import GrammarParser

import io
import sys
import lenguage.MyVisitor as MyVisitor

def run_code(code:str):
    input_stream = InputStream(code)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.program()

    # Captura la salida
    old_stdout = sys.stdout
    buf=io.StringIO()
    sys.stdout = buf

    # Creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    # Visitamos el arbol con nuestro visitor
    visitor.visit(tree)
    # Capturamos la salida
    output = buf.getvalue()

    return output