from tabelatad import *

tabela = Tabela(5)
"""
tabela.inserir(1,"oi")
tabela.inserir(2,"tchau")
tabela.inserir(2,"adeus")
tabela.excluir(1)
tabela.inserir(4,"ola")
tabela.inserir(3,"opa")
tabela.inserir(5,"eae")
print(tabela.consultar(1))
print(tabela.consultar(2))
print(tabela.consultar(3))
print(tabela.consultar(4))
print(tabela.consultar(5))
"""
"""
tabela.destruir()
print(tabela.consultar(1))
print(tabela.consultar(2))
print(tabela.consultar(3))
print(tabela.consultar(4))
print(tabela.consultar(5))
"""
tabela.inserirord(1,"oi")
tabela.inserirord(4,"tchau")
tabela.inserirord(2,"ola")
tabela.inserirord(3,"eae")
tabela.inserirord(5,"opa")
print(tabela.buscarbin(1))
print(tabela.buscarbin(4))
print(tabela.buscarbin(2))
print(tabela.buscarbin(3))
print(tabela.buscarbin(5))
print(tabela.buscarbin(8))