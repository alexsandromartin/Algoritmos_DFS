''' 
Allan Feitosa Wariss Maia - 541564
Rogério de Jesus Machado Pio - 540140
Alexsandro Martins Alves - 541581
Mahatma Gandhi Pereira Leite - 542480
'''


def imprime(d, f, N):
    # "N" é o numero de vertices
    for i in range(N):
        print("Vértice ", i+1, ":", d[i], f[i]) 
        
#testa para ver se os vertices são numeros ou letras
# def is_numeric(v):
#     try:
#         int(v)
#         return True
#     except ValueError:
#         return False

def loadlista():
    arquivo = open('GD.txt','r')
    lista = arquivo.readlines()
    
    for i in range(len(lista)):
        linha= lista[i].split()
        if i == 0:
            N = int(linha[0])
            lista_adj = [[]for _ in range (N)]
        else:
            lista_adj[int(linha[0])-1].append(int(linha[1])-1)
            print( lista_adj)
            
    arquivo.close()
    return lista_adj, N

# Tentamos kk
# def loadlistaLetras():
#     arquivo = open('grafo_letras.txt','r')
#     lista = arquivo.readlines()
    
#     for i in range(len(lista)):
#         linha= lista[i].split()
#         if i == 0:
#             N = int(linha[0])
#             lista_adj = [[]for _ in range (N)]
#         else:
#             lista_adj[0].append(linha[1])
            
#     arquivo.close()
#     return lista_adj, N


def DFS_visit(u):
    global mark
    cor[u] = "Cinza"
    mark = mark +1
    d[u] = mark
    for v in lista_adj[u]:
        if cor [v] == "Branco":
            print("Aresta (", u+1,v+1,") : Árvore")
            DFS_visit(v)
        elif cor[v]=="Cinza":
            print("Aresta (",u+1,v+1,") : Retorno")
        elif d[u] < f[v]:
            print("Aresta (",u+1,v+1,") : Avanço")
        else:
            print("Aresta (",u+1,v+1,") : Cruzamento")
    cor[u] = "Preto"
    mark = mark +1
    f[u] = mark

def Dfs():
    for u in V:
        cor[u]="Branco"
    for u in V:
        if cor[u]=="Branco":
            DFS_visit(u)

[lista_adj, N] = loadlista()

V = [3,0,1,2,4,5,6]
cor = [0]*N
d = [0]*N
f = [0]*N
mark = 0
Dfs()
imprime(d,f,N)