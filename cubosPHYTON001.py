
def cubos():
        nome = input("digite o nome do cubo")
        pecas = int(input("Quantas peças tem o cubo?"))
        quantidade_de_pecas_mv = int(input("Quantas peças você terá quie mover para chegar até a posição desejada"))
        deformidade = int(input("Quantas arestas diferentes entre si tem o cubo?"))
        distancia = int(input("Qual a distancia, em unidades de peça, até a posição desejada?"))


complexidade = quantidade_de_pecas_mv*deformidade
entropia = complexidade*distancia*quantidade_de_pecas_mv

print(complexidade)
print("A complexidade do cubo{} é {}".format (nome,complexidade))
