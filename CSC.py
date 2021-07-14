import os
import re
import ast
import argparse

# main code
def main():
    
    '''讀參數'''
    arg_parse = argparse.ArgumentParser(description='A static Big-O analysis tool base on Big-O AST.')
    arg_parse.format_help()
    arg_parse.add_argument('filename', type=str, help='target code filename')
    args = arg_parse.parse_args()

    '''讀檔案'''
    source_file_name = args.filename
    f = open(source_file_name, "r",encoding="utf-8")
    code = ast.parse(f.read())
    pythonCodeSmell().visit(code)

class pythonCodeSmell(ast.NodeVisitor):

    # 走訪程式碼
    def visit_Module(self, node):

        self.LOC = 1 # class line of code
        self.LOC_if = False 

        self.MLOC = 1 # method line of code
        self.MLOC_if = False 

        self.PAR = 0 # method arg count

        self.LMC = 0 # length of message chain

        self.DOC = 0 # depth of closure

        self.NBC = 0 # number of base classes

        self.NEC = 0 # number of except clauses
        self.NGEC = 0 # number of general exception clauses
        self.NEEC = 0 # number of empty except clauses
        self.ge = ['SyntaxError', 'NameError', 'TypeError', 'ZeroDivisionError', 'IndexError'] # general exception example

        self.NOA = 0 # number of ast node in one expression
        
        self.NOL = 0 # number of loops
        self.NOCC = 0 # number of control conditions

        self.LEC = 0 # length of element chain

        self.generic_visit(node)

    # class line of code
    def visit_ClassDef(self, node):
        for child in ast.walk(node):
            if \
                isinstance(child, ast.Assign) or \
                isinstance(child, ast.AugAssign) or \
                isinstance(child, ast.Expr) or \
                isinstance(child, ast.For) or \
                isinstance(child, ast.While) or \
                isinstance(child, ast.Try) or \
                isinstance(child, ast.Global) or \
                isinstance(child, ast.Nonlocal) or \
                isinstance(child, ast.Return) or \
                isinstance(child, ast.Pass) or \
                isinstance(child, ast.Break) or \
                isinstance(child, ast.Continue):
                self.LOC += 1
            elif isinstance(child, ast.If):
                self.LOC += 1 
                for else_node in child.orelse:
                    if isinstance(else_node, ast.If):
                        self.LOC_if = True
                        break
                if not self.LOC_if and len(child.orelse)!=0:
                    self.LOC += 1
                self.LOC_if = False
            elif isinstance(child, ast.FunctionDef):
                self.LOC += 1
                for base in node.bases:
                    if isinstance(base ,ast.Name):
                        self.NBC += 1
        self.generic_visit(node)

    # method line of code
    def visit_FunctionDef(self, node):
        self.PAR = len(node.args.args)
        for child in ast.walk(node):
            if \
                isinstance(child, ast.Assign) or \
                isinstance(child, ast.AugAssign) or \
                isinstance(child, ast.Expr) or \
                isinstance(child, ast.For) or \
                isinstance(child, ast.While) or \
                isinstance(child, ast.Try) or \
                isinstance(child, ast.Global) or \
                isinstance(child, ast.Nonlocal) or \
                isinstance(child, ast.Return) or \
                isinstance(child, ast.Pass) or \
                isinstance(child, ast.Break) or \
                isinstance(child, ast.Continue):
                self.MLOC += 1
            elif isinstance(child, ast.If):
                self.MLOC += 1 
                for else_node in child.orelse:
                    if isinstance(else_node, ast.If):
                        self.MLOC_if = True
                        break
                if not self.MLOC_if and len(child.orelse)!=0:
                    self.MLOC += 1
                self.MLOC_if = False 
            elif isinstance(child, ast.FunctionDef):
                self.DOC += 1
        self.generic_visit(node)

    # long message chain
    def visit_Call(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                self.LMC += 1
        self.generic_visit(node)

    # try...except 
    def visit_Try(self, node):
        for handler in node.handlers:
            if isinstance(handler, ast.ExceptHandler):
                self.NEC += 1
                if handler.type.id in self.ge:
                    self.NGEC += 1;
                if len(handler.body):
                    self.NEEC += 1
        self.generic_visit(node)
    
    # lambda
    def visit_Lambda(self, node):
        for child in ast.walk(node):
            self.NOA += 1
        self.generic_visit(node)

    # complex list comprehension
    def visit_ListComp(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.comprehension):
                self.NOL += 1 
                for list_ifs in child.ifs:
                    if isinstance(list_ifs, ast.Compare):
                        self.NOCC += 1
        self.generic_visit(node)
    
    # long element chain
    def visit_Expr(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.Subscript):
                self.LEC += 1 
        self.generic_visit(node)

    # long ternary conditional expression
    def visit_IfExp(self, node):
        for child in ast.walk(node):
            self.NOA += 1
        self.generic_visit(node)


if __name__ == "__main__":
    main()     