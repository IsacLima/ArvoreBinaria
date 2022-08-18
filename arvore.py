from tkinter import Y


class nodo:
    def __init__(self, info, esq = None, dir = None):
        self.info = info
        self.esq = esq
        self.dir = dir
    
    def __repr__(self):
        return "%s <- %s -> %s" % (self.esq and self.esq.info, self.info, self.dir and self.dir.info)
    
    def prefixesq(self):
        print(self.info, end=" ")
        if(self.esq):
            self.esq.prefixesq()
        if(self.dir):
            self.dir.prefixesq()
            
    def prefixdir(self):
        print(self.info, end=" ")
        if(self.dir):
            self.dir.prefixdir()
        if(self.esq):
            self.esq.prefixdir()
            
    def posfixesq(self):
        if(self.esq):
            self.esq.posfixesq()
        if(self.dir):
            self.dir.posfixesq()
        print(self.info, end=" ")
            
    def posfixdir(self):
        if(self.dir):
            self.dir.posfixdir()
        if(self.esq):
            self.esq.posfixdir()
        print(self.info, end=" ")
        
    def infixesq(self):
        if(self.esq):
            self.esq.infixesq()
        print(self.info, end=" ")
        if(self.dir):
            self.dir.infixesq()
        
    def infixdir(self):
        if(self.dir):
            self.dir.infixdir()
        print(self.info, end=" ")
        if(self.esq):
            self.esq.infixdir()
            
    def localiza(self, valor):

        if(self.info == valor):
            return self

        if self.esq:
            return self.esq.localiza(valor) 
        
        if self.dir:
            return self.dir.localiza(valor)

    def insesq(self, pai, filho):
        nodoPai = self.localiza(pai)
        if (nodoPai != None and nodoPai.esq == None):
            nodoPai.esq = nodo(filho)


    def insdir(self, pai, filho):
        nodoPai = self.localiza(pai)
        if (nodoPai != None and nodoPai.dir == None):
            nodoPai.dir = nodo(filho)

    def localizaPai(self, valor):
        if(self.esq and self.esq.info == valor):
            return self
        if(self.dir and self.dir.info == valor):
            return self
        
        if self.esq:
            return self.esq.localizaPai(valor)

        if self.dir:
            return self.dir.localizaPai(valor)

    def folha(self):
        return (self.esq == None and self.dir == None)
    
    def remfolha(self, valor):
        if (self.info == valor):
            self.info = None
        nodoPai = self.localizaPai(valor)
        if(nodoPai):
            if(nodoPai.esq and nodoPai.esq.info == valor and nodoPai.esq.folha()):
                nodoPai.esq = None
            
            if(nodoPai.dir and nodoPai.dir.info == valor and nodoPai.dir.folha()):
                nodoPai.dir = None
        
 
t = nodo("a")
t.esq = nodo("b")
t.dir = nodo("c")
t.esq.dir = nodo("e")
t.esq.esq = nodo("d")
t.dir.esq = nodo("f")
t.dir.dir = nodo("g")


print("---------\n")
print(t.localiza("d"))
print("\ninserindo folhas\n")
t.insesq("d","z")
print(t.localiza("d"))
print("---------\n")

print("\n\n" +str(t.localizaPai("z")))
t.remfolha("z")
print("\nefetuada a remoção caso possivel\n\n" +str(t.localiza("d")) + "\n")

def menu():
    return int(input("\n\nEscolha um dos tipos de caminhamento para exibição:\n1 - pós-fixado a esquerda\n2 - pós-fixado a direita\n3 - pré-fixado a esquerda\n4 - pré-fixado a direita\n5 - central a esquerda\n6 - central a direita\n7 - Sair\nDigite sua opção: "))

def mostrar(entrada):
    if(entrada == 1):
        texto = "pós-fixado a esquerda"
    if(entrada == 2):
        texto = "pós-fixado a direita"
    if(entrada == 3):
        texto = "pré-fixado a esquerda"
    if(entrada == 4):
        texto = "pré-fixado a direita"
    if(entrada == 5):
        texto = "central a esquerda"
    if(entrada == 6):
        texto = "central a direita"
    print("\nA arvore em representação hierarquica é assim:\n      a\n    /   \ \n   b     c\n  / \   / \ \n d   e f   g\n\nO caminhamento " + str(texto) + " ficou assim:\n")


loop = True
while(loop):
    entrada = menu()
    if(entrada == 1):
        print("\n")
        mostrar(entrada)
        t.posfixesq()
        input("\nDigite qualquer coisa para voltar ao menu: ")
        

    elif(entrada == 2):
        print("\n")
        mostrar(entrada)
        t.posfixdir()
        input("\nDigite qualquer coisa para voltar ao menu: ")

    elif(entrada == 3):
        print("\n")
        mostrar(entrada)
        t.prefixesq()
        input("\nDigite qualquer coisa para voltar ao menu: ")

    elif(entrada == 4):
        print("\n")
        mostrar(entrada)
        t.prefixdir()
        input("\nDigite qualquer coisa para voltar ao menu: ")

    elif(entrada == 5):
        print("\n")
        mostrar(entrada)
        t.infixesq()
        input("\nDigite qualquer coisa para voltar ao menu: ")

    elif(entrada == 6):
        print("\n")
        mostrar(entrada)
        t.infixdir()
        input("\nDigite qualquer coisa para voltar ao menu: ")

    elif(entrada == 7):
        loop = False

    else:
        print("\nOpção invalida, tente novamente!\n")