class Tabela:
    def __init__(self,max):
        self.chave = [None]*(max)
        self.valor = [None]*(max)
        self.li = 1
        self.ls = max
        self.ini = self.li - 1
        self.fim = self.ls + 1
    def vazia(self):
        if self.ini < self.li:
            return(True)
        return(False)
    def cheia(self):
        if self.fim == self.ls:
            return(True)
        return(False)
    def tamanho(self):
        if not self.vazia(): 
            return(self.fim)
        return(0)
    def buscarbin(self,chave):
        if not self.vazia():
            meio = ((self.ini + self.fim)//2) - 1
            inicio = self.ini - 1
            final = self.fim - 1
            while inicio != final:
                if self.chave[meio] < chave:
                    if meio == inicio:
                        if self.chave[final] == chave:
                            return(final+1)
                        else:
                            return(0)
                    inicio = meio
                    meio = (inicio+ final)//2
                else:
                    if meio == inicio:
                        if self.chave[inicio] == chave:
                            return(inicio+1)
                        else:
                            return(0)
                    final = meio
                    meio = (inicio+final)//2
            if self.chave[inicio] == chave:
                return[inicio+1]
        return(0)
    def buscar(self,chave):
        if not self.vazia():
            for i in range(self.ini-1,self.fim):
                if self.chave[i] == chave:
                    return(i+1)
        return(0)
    def inserirord(self,chave,valor):
        pos = self.buscar(chave)
        if pos > 0:
            self.valor[pos-1] = valor
            return(True)
        elif not self.cheia():
            if self.vazia():
                self.ini = self.li
                self.fim = self.li
                self.chave[self.fim-1] = chave
                self.valor[self.fim-1] = valor
                return(True)
            else:
                for i in range(self.ini-1,self.fim):
                    if chave < self.chave[i]:
                        self.fim += 1
                        cont = self.fim-1
                        while cont > i:
                            self.chave[cont] = self.chave[cont-1]
                            self.valor[cont] = self.valor[cont-1]
                            cont -= 1
                        self.chave[cont] = chave
                        self.valor[cont] = valor
                        return(True)
                self.fim += 1
                self.chave[self.fim-1] = chave
                self.valor[self.fim-1] = valor
        else:
            return(False)
    def inserir(self,chave,valor):
        pos = self.buscar(chave)
        if pos > 0:
            self.valor[pos-1] = valor
            return(True)
        elif not self.cheia():
            if self.vazia():
                self.ini = self.li
                self.fim = self.li
            else:
                self.fim += 1
            self.chave[self.fim-1] = chave
            self.valor[self.fim-1] = valor
            return(True)
        else:
            return(False)
    def consultar(self,chave):
        pos = self.buscar(chave)
        if pos > 0:
            return(self.valor[pos-1])
        return(False)
    def excluir(self,chave):
        pos = self.buscar(chave)
        if pos > 0:
            for i in range(pos-1,self.fim-1):
                self.chave[i] = self.chave[i+1]
                self.valor[i] = self.valor[i+1]
            self.fim -= 1
            return(True)
        return(False)
    def destruir(self):
        self.ini = self.li - 1
        self.fim = self.ls + 1