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



def fuzzy_operations(fuzzy_values):
    print(fuzzy_values)
    # 'resolucao' do grafico final
    step = 0.001
    # tamanho dos vetores gerados
    size = int(1/step)

    grafico_final = []



    '''
    Se o PRECO NAO for BARATO ou a VELOCIDADE do servico NAO for RAPIDA
    ou a QUALIDADE DA COMIDA NAO for BOA ou o GARCOM NAO for SIMPATICO
    entao a GORJETA eh RUIM
    '''
    preco = 1-fuzzy_values[0]
    vel_serv = 1-fuzzy_values[1]
    ql_comida = 1-fuzzy_values[2]
    simpatia = 1-fuzzy_values[3]
    f = max(preco, vel_serv, ql_comida, simpatia)
    final_gorjeta_ruim = generate_final_func(f, gorjeta_ruim, step)


    '''
    Se o PRECO for BARATO e o GARCOM for SIMPATICO e a QUALIDADE DA COMIDA nao for BOA 
    entao a GORJETA eh MEDIA
    '''
    preco = fuzzy_values[0]
    simpatia = fuzzy_values[3]
    ql_comida = 1-fuzzy_values[2]
    f = min(preco, simpatia, ql_comida)
    final_gorjeta_media = generate_final_func(f, gorjeta_media, step)


    '''
    Se a VELOCIDADE do servico for RAPIDA e a QUALIDADE DA COMIDA for BOA
    ou a QUALIDADE DA COMIDA for BOA e o GARCOM for SIMPATICO
    entao a GORJETA eh BOA
    '''
    vel_serv = fuzzy_values[1]
    ql_comida = fuzzy_values[2]
    simpatia = fuzzy_values[3]
    f = max(min(vel_serv, ql_comida), min(ql_comida, simpatia))
    final_gorjeta_boa = generate_final_func(f, gorjeta_boa, step)





    # pega o maximo entre os 3 graficos
    # (Agrega os graficos)
    for i in range(size):
        grafico_final.append(max(final_gorjeta_media[i], final_gorjeta_boa[i], final_gorjeta_ruim[i]))

    return grafico_final





'''

metodo mamdani:
https://www.mathworks.com/help/fuzzy/types-of-fuzzy-inference-systems.html
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
    return x/y/1000

'''
Metricas para avaliar o valor da gorjeta:
    - Preço (Quao barato) de 0.0 a 1.0
    - Velocidade do servico (Quao rapido) de 0.0 a 1.0
    - Qualidade da comida (Quao boa) de 0.0 a 1.0
    - Simpatia do garcom (Quao simpatico) de 0.0 a 1.0

Tipos de gorjeta (entre 0% e 25%):
    - Ruim (Funcao triangular com pico em 0.25)
    - Media (Funcao triangular com pico em 0.5)
    - Boa (Funcao triangular com pico em 0.75)
'''

def main():

    print("Programa para calcular o valor da gorjeta para um garcom utilizando logica fuzzy")

    user_inputs = []

    print("Digite de 0 a 1 o quanto achou barato o preco")
    user_inputs.append(float(input()))

    print("Digite de 0 a 1 o quanto achou rapido o servico")
    user_inputs.append(float(input()))

    print("Digite de 0 a 1 o quanto achou boa a qualidade da comida")
    user_inputs.append(float(input()))

    print("Digite de 0 a 1 o quanto achou simpatico o garcom")
    user_inputs.append(float(input()))


    # passa os valores do usuario para as funcoes de fuzzificação
    # retorna vetor com os valores difusos
    fuzzy_values = fuzzifier(user_inputs)

    # realiza as operacoes e implicações
    # retorna um vetor com o grafico difuso final
    funcao_final = fuzzy_operations(fuzzy_values)

    # recebe um grafico final e retorna o valor absoluto
    abs_value = defuzzifier(funcao_final)

    print(f"O valor da gorjeta eh: {(abs_value*25):.2f}%")

    return abs_value * 25



def test():
    assert fuzzifier([0.6, 0.75, 0.76, 0.64]) == [0.25, 0.95, 1, 0.28]
    assert defuzzifier([0.25, 0.95, 1, 0.28]) == 0.0015282258064516125


    assert metrica_preco_barato(0) == 0
    assert metrica_preco_barato(0.5) == 0.050000000000000044
    assert metrica_preco_barato(1) == 1


    assert metrica_qlserv_boa(0) == 0
    assert metrica_qlserv_boa(0.5) == 0
    assert metrica_qlserv_boa(1) == 1

    assert metrica_simp_boa(0) == 0
    assert metrica_simp_boa(0.5) == 0
    assert metrica_simp_boa(1) == 1

    assert metrica_velserv_boa(0) == 0 
    assert metrica_velserv_boa(0.5) == 0.19999999999999996
    assert metrica_velserv_boa(1) == 1

    assert gorjeta_ruim(0) == 0
    assert gorjeta_ruim(0.25) == 1.0 
    assert gorjeta_ruim(0.75) == 0

    assert gorjeta_media(0) == 0
    assert gorjeta_media(0.5) == 1.0 
    assert gorjeta_media(1) == 0

    assert gorjeta_boa(0) == 0
    assert gorjeta_boa(0.75) == 1.0 
    assert gorjeta_boa(1) == 0

if __name__ == "__main__":
    test()

    main()

