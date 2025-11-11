from .GrammarVisitor import GrammarVisitor
from .GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    # Definimos la memoria o el entorno
    def __init__(self):
        self.memory = {}

    # Definimos la asignacion
    def visitAssign(self,ctx):
        # Se obtiene el id o nombre de la variable
        name=ctx.ID().getText()
        # Se obtiene el valor, ya sea un valor numerico o una expresion
        value=self.visit(ctx.expr())
        # Se almacena en memoria a partir del nombre y el valor
        self.memory[name] = value

    # Definimos la impresion
    def visitPrint(self,ctx):
        # Definimos la expresion que se desea mostrar
        value=self.visit(ctx.expr())
        # Imprime el valor
        print(value)

    # Definimos las expresion
    def visitExpr(self,ctx):
        # Busca si existe IDs
        if ctx.ID():
            # Obtiene en el contexto el nombre de la variable
            name=ctx.ID().getText()
            # Si el nombre de la variable no esta, lanza un error    
            if name not in self.memory:
                raise NameError(f"Variable '{name}' no definida")
            # Si existe el nombre retorna la variable
            return self.memory[name]
            # busca el operador
        elif ctx.op:
            # Visita y optiene lado izquierdo
            left=self.visit(ctx.expr(0))
            # Visita y optiene lado derecho
            right=self.visit(ctx.expr(1))
            # Evalua la operacion a realizar
            if ctx.op.text == "+":
                return left + right
            if ctx.op.text == "-":
                return left - right
            if ctx.op.text == "*":
                return left * right
            if ctx.op.text == "/":
                # Verifica la division de cero
                if right == 0:
                    raise ValueError("Division por cero")
                return left / right