
import random

def limit(x, l, h):
    
        return min(h, max(l, x))


def metrica_preco_barato(x):
    y = 2*x - 0.95
    return limit(y, 0, 1)

def metrica_velserv_boa(x):
    y = 3*x - 1.3
    return limit(y, 0, 1)

def metrica_qlserv_boa(x):
    y = 4*x - 2
    return limit(y, 0, 1)

def metrica_simp_boa(x):
    y = 2*x -1
    return limit(y, 0, 1)




def gorjeta_ruim(x):
    y1 = 4*x
    y2 = -4*x-1
    y = max(min(y1, y2, 1), 0)
    return limit(y, 0, 1)

def gorjeta_media(x):
    y1 = 4*x-1
    y2 = -4*x+3
    y = max(min(y1, y2, 1), 0)
    return limit(y, 0, 1)

def gorjeta_boa(x):
    y1 = 4*x-2
    y2 = -4*x+4
    y = max(min(y1, y2, 1), 0)
    return limit(y, 0, 1)






def fuzzifier(data):
    final = []

    final.append(metrica_preco_barato(data[0]/10))
    final.append(metrica_velserv_boa(data[1]/10))
    final.append(metrica_qlserv_boa(data[2]/10))
    final.append(metrica_simp_boa(data[3]/10))

    return final

# ???????
# talvez um peso para cada metrica
# se ql serv for boa, vel do serv for boa, ql da com for boa E simp do garcom for ruim, entao gorjeita ruim
# se ql serv for ruim, vel do serv for ruim, ql da com for ruim E simp do garcom for boa, entao gorjeita media
# baseado nas regras (if elses)
# trabalhar com as palavras (bom, medio, ruim) e nao com os valores absolutos (?)
# retornar palavra para o defusificador
# e o defus retorna valor absoluto baseado no range que a palavra representa
def fuzzy_operations(fuzzy_values):

    pass

# possivel distribuiçao normal
# considerando a palavra recebida
# onde comeca e acaba os valores de gorjeta possivel para cada palavra(ruim, medio, bom)
# bom = [0, 0.2]
# medio = [0.2, 0.5] 0.37  * 25 = 9.25
# ruim = [0.5, 1]

'''
metodo mamdani:
https://www.mathworks.com/help/fuzzy/types-of-fuzzy-inference-systems.html

wikipedia: fuzzy logic (mais coisa que na pagina br)
https://en.wikipedia.org/wiki/Fuzzy_logic

como deveria ser feito:
- ter um grafico especifico para cada qualidade de cada metrica
    por ex: um grafico para qualidade ruim de comida, media de comida
    e boa de comida, etc.
- seguindo as regras, monta-se um grafico final para cada regra
    por ex: se a comida for boa ou velocidade boa entao gorjeta eh media
    teriamos um valor X para colocar no grafico, que recebemos do usuario
    coloca-se esse x no grafico de comida boa e retornamos um Y, por ex: 0.4
    mesma coisa acontece para velocidade boa, por ex retorna 0.3
    como a operacao da regra eh or, fazemos o max entre eles, retorna entao 0.4
    com esse valor verificamos no grafico de gorjeta media, criamos um novo grafico
    onde o pegamos todo o valor do grafico ate o valor que tivemos, no caso 0.4
    nesse caso o graf fica 'cortado'.
- fazemos o passo anterior para todas as regras que temos, ao final agregamos todos os 
    graficos;
- apos conseguir o grafico final, fazemos a defusificação, nesse caso estamos utilizandoi
    o metodo de mamdani, entao seguimos nele, basta encontrar o centroide
    do grafico criado, ele retornara um valor absoluto

consideraçoes:
    nao acho que esteja necessariamente errado como esta snedo feito agora, retornando
    um valor escrito, porem eh melhor trocar pois dessa forma com o mesmo input
    temos o mesmo retorno
'''


def defuzzifier(fuzzy_final):

    pass


# trocar qual servico por algo mais condinzente com o problema
# custo, ou algo assim, que trabalhe no lado negativo
def main():
    # na forma de float entre 0 e 1
    user_inputs = [5, 6, 4, 9]
    metrics = ["Preço", "Vel. servico", "Qual. Comida", "Simp. Garcom"]
    
    fuzzy_values = fuzzifier(user_inputs)

    fuzzy_final = fuzzy_operations(fuzzy_values)

    abs_value = defuzzifier(fuzzy_final)

    return abs_value * 25





for i in range(10):
    print("preco", i, metrica_preco_barato(i/10))
print()

for i in range(10):
    print("vel serv", i, metrica_velserv_boa(i/10))
print()
    
for i in range(10):
    print("qual com", i, metrica_qlserv_boa(i/10))
print()

for i in range(10):
    print("simp", i, metrica_simp_boa(i/10))

print(fuzzifier([5, 6, 4, 9]))



