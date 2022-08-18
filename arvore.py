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
        print("\n --" + str(self) + " = " + str(valor) + " -- \n")
        if(self.info == valor):
            return self
        if self.esq:
            return self.esq.localiza(valor)
        
        if self.dir:
            return self.dir.localiza(valor)
        
        
 
t = nodo("a")
t.esq = nodo("b")
t.dir = nodo("c")
t.esq.dir = nodo("e")
t.esq.esq = nodo("d")
t.dir.esq = nodo("f")
t.dir.dir = nodo("g")
t.infixesq()
print("\n")
t.infixdir()
print("\n\n" +str(t.localiza("e")) + "\n")