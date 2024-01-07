import matplotlib.pyplot as plt
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
    y2 = -4*x +2
    y = max(min(y1, y2, 1), 0)
    return y

def gorjeta_media(x):
    y1 = 4*x -1
    y2 = -4*x +3
    y = max(min(y1, y2, 1), 0)
    return y

def gorjeta_boa(x):
    y1 = 4*x -2
    y2 = -4*x +4
    y = max(min(y1, y2, 1), 0)
    return y






def fuzzifier(data):
    final = []

    final.append(metrica_preco_barato(data[0]))
    final.append(metrica_velserv_boa(data[1]))
    final.append(metrica_qlserv_boa(data[2]))
    final.append(metrica_simp_boa(data[3]))

    return final


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

'''
x -> valor do eixo x
fuzz_max_val -> valor maximo que o fuzzificador pode retornar
final_func -> funcao que representa o grafico final ou seja a gorjeta(boa, media ou ruim)
'''
def get_func_to_val(x, fuzz_max_val, final_func):
    return min(final_func(x), fuzz_max_val)

def generate_final_func(fuzz_max_val, final_func, step):
    final_map = []

    for i in range(0, int(1/step), 1):
        final_map.append(get_func_to_val(i*step, fuzz_max_val, final_func))

    return final_map


# para cada regra, calcula as variaveis e gera o grafico final, que dps sera
# todos agregados juntos(max entre todos) e enviados ao defuzifier
# provavelmente precisara de um jeito de fazer varias sem guardar em variavel
# os valores chegando ja passaram pela fuzificação
def fuzzy_operations(fuzzy_values):
    print(fuzzy_values)
    step = 0.001
    size = int(1/step)
    grafico_final = []

    # se preco for barato ou simpatia do garcom for boa entao gorjeta eh media
    preco = fuzzy_values[0]
    simpatia = fuzzy_values[3]
    f = max(preco, simpatia)
    final_gorjeta_media = generate_final_func(f, gorjeta_media, step)

    ########
    plt.plot(final_gorjeta_media)
    plt.show()
    ########

    # se velocidade do servico for boa e qualidade da comida for boa entao gorjeta eh boa
    vel_serv = fuzzy_values[1]
    ql_comida = fuzzy_values[2]
    f = min(vel_serv, ql_comida)
    final_gorjeta_boa = generate_final_func(f, gorjeta_boa, step)


    ########
    plt.plot(final_gorjeta_boa)
    plt.show()
    ########

    # se o preco nao for barato ou a velocidade do servico nao for boa
    # ou a qualidade da comida nao for boa ou a simpatia do garcom nao for boa
    # entao gorjeta eh ruim
    preco = 1-fuzzy_values[0]
    vel_serv = 1-fuzzy_values[1]
    ql_comida = 1-fuzzy_values[2]
    simpatia = 1-fuzzy_values[3]
    f = max(preco, vel_serv, ql_comida, simpatia)
    final_gorjeta_ruim = generate_final_func(f, gorjeta_ruim, step)

    ########
    plt.plot(final_gorjeta_ruim)
    plt.show()
    ########

    # junta todos os graficos
    for i in range(size):
        grafico_final.append(max(final_gorjeta_media[i], final_gorjeta_boa[i], final_gorjeta_ruim[i]))

    ########
    plt.plot(grafico_final)
    plt.show()
    ########

    return grafico_final





'''
centroid = sum( u{xi} * xi ) / ^sum( u{xi} )
'''
# recebe um array de X valores, representando a funcao final
# a funcao calcula o centroid e retorna o valor encontrado
def defuzzifier(func_final):
    x = 0
    y = 0
    for i in range(len(func_final)):
        x += func_final[i] * i
        y += func_final[i]
    print(x, y)
    return x/y/1000



# trocar qual servico por algo mais condinzente com o problema
# custo, ou algo assim, que trabalhe no lado negativo
def main():
    #user_inputs = [0.5, 0.6, 0.4, 0.9]
    user_inputs = [0.6, 0.5, 0.6, 0.8]

    metrics = ["Preço", "Vel. servico", "Qual. Comida", "Simp. Garcom"]
    metrics_tip = ["Ruim", "Media", "Boa"]

    metrics_func = [metrica_preco_barato, metrica_velserv_boa, metrica_qlserv_boa, metrica_simp_boa]
    metrrics_tip_func = [gorjeta_ruim, gorjeta_media, gorjeta_boa]

    # passa os valores do usuario para as funcoes de fuzzificação
    # retorna vetor com os valores difusos
    fuzzy_values = fuzzifier(user_inputs)

    # realiza as operacoes e implicações
    # retorna um vetor com o grafico difuso final
    funcao_final = fuzzy_operations(fuzzy_values)

    ########
    plt.plot(funcao_final)
    plt.show()
    ########



    # recebe um grafico final e retorna o valor absoluto
    abs_value = defuzzifier(funcao_final)

    #talvez o resultado do defuzzifier seja o index da funcao final??

    return abs_value





#print(fuzzifier([5, 6, 4, 9]))

#print(metrica_preco_barato(0.5))

#print(generate_final_func(0.5, gorjeta_ruim))

#print(fuzzy_operations([5, 6, 4, 9]))

print(main())