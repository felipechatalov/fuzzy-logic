'''
possivel problema: Problema da gorjeta

-> Considerando que o valor da gorjeta pode ser de 0 ate 25%.
    Para sabermos quanto dar de gorjeta temos que avaliar a
    qualidade do servico, qualidade da comida, velocidade 
    do servico e simpatia do garcom. (Ainda da pra adicionar/trocar
    valor total da conta). Eh necessario 4 variaveis para avaliar
 
    
->  Exemplos de valores arbitrarios para cada variavel:
      Qualidade do servico: 
        Absoluto: 0 a 10
        Fuzzy: ruim, aceitavel, otimo

      Qualidade da comida: 
        Absoluto: 0 a 10
        Fuzzy: ruim, aceitavel, otimo

      Velocidade do servico:
        Absoluto: 0 a 10
        Fuzzy: ruim, aceitavel, otimo

      Simpatia do garcom:
        Absoluto: 0 a 10
        Fuzzy: ruim, aceitavel, otimo

        
->  Baseado nos valores das variaveis, o programa deve retornar
    um valor para a gorjeta.
    Absoluto: 0 a 25


->  Regras:
    - Deve ter regras baseadas em cada variavel, onde as 4 trabalham
    juntas na mesma regra

    -ex: 
      -> Se a qualidade do servico for boa e a qualidade da comida for boa
      e a velocidade do servico for mediana e a simpatia do garcom for ok
      entao a gorjeta deve ser boa, ou em absoluto, 15% 


->  O programa deve funcionar baseado no input de (?) valores abosultos
      para cada variavel(?) ou valores (?)arbitrarios(?) e retonar a 
      porcentagem de gorjeta em porcentagem (ex: 20%)


->  1 Passo: Transformar os valores de entrada entre 0 e 1, para valores difusos,
      como bom, medio e ruim, para todas as variaveis. Este passo usa as funcoes de
      transformacao.
->  2 Passo: Aplicar operadores difusos(And e or), para definir o grau maximo e minimo de
      pertinencia do conjunto.
->  3 Passo: Aplicar operador de implicacao. Ex: Comida excelente ou atentimento excelente 
      entao gorjeta E alta
->  4 Passo: Combinar todas as saidas em um unico conjunto difuso, uniao e interseccao
->  5 Passo: Difusificacao, retornar um numero baseado na faixa estipulada pela logica difusa

    
->  Ficar atento no 'passo-a-passo' dado no pdf e fazer questao de seguir cada passo
'''




'''
aqui, baseado no grafico, retorna se um valor float d é
bom, medio ou ruim por exemplo
bom = x=y-0.3
medio x=y-0.5
ruim x=y-1
mt ruim = asdasda

0.5   0.5     0.0     0.0
bom + medio + ruim + mtruim= 

0.37 -> bom

0.6 -> medio
'''

import random

def qlserv(x):

    r = -3*x + 1.6 
    r = min(1, max(0, r))

    m1 = 3* x - 0.6
    m2 = -6*x + 4.6
    m = max(min(m1, m2, 1), 0)

    b = 6*x-3.6
    b = min(1, max(0, b))

    return [r, m, b]


def velserv(x):
    r = -3*x +1.2
    r = min(1, max(0, r))

    m1 = 3 * x - 0.2
    m2 = 2 - 2 * x
    m = max(min(m1, m2, 1), 0)

    b = 2 * x - 1
    b = min(1, max(0, b))

    return [r, m, b]


def qlcomida(x):
    r = -8 * x + 2.6
    r = min(1, max(0, r))

    m1 = 8 * x - 1.6
    m2 = -8 * x + 7
    m = max(min(m1, m2, 1), 0)

    b = 8 * x - 6
    b = min(1, max(0, b))

    return [r, m, b]


def simp(x):
    r = -8 * x + 1.8
    r = min(1, max(0, r))

    m1 = 8 * x - 0.8
    m2 = -6 * x + 5
    m = max(min(m1, m2, 1), 0)

    b = 6 * x - 4
    b = min(1, max(0, b))

    return [r, m, b]

def to_fuzzy(x, nome):
    r,m,b = qlserv(x)

    if nome == "Preço":
        r,m,b = qlserv(x)
    elif nome == "Vel. servico":
        r,m,b = velserv(x)
    elif nome == "Qual. Comida":
        r,m,b = qlcomida(x)
    elif nome == "Simp. Garcom":
        r,m,b = simp(x)
    else:
        print("ERROR: metrica nao encontrada")
        return

    number = random.random()
    print(f"rng:{float(number):.2} r:{float(r):.2} m:{float(m):.2} b:{float(b):.2}", end=" ")
    if number < r:
        return "Ruim"
    elif number < (m+r):
        return "Medio"
    else:
        return "Bom"

def fuzzifier(data, metrics):
    r = []
    for i in range(len(len(metrics))):
        r.append(to_fuzzy(data[i], metrics[i]))

    return r

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
    user_inputs = [0.5, 0.6, 0.4, 0.9]
    metrics = ["Preço", "Vel. servico", "Qual. Comida", "Simp. Garcom"]
    
    fuzzy_values = fuzzifier(user_inputs, metrics)

    fuzzy_final = fuzzy_operations(fuzzy_values)

    abs_value = defuzzifier(fuzzy_final)

    return abs_value * 25






for i in range(10):
    print("vel serv", i, to_fuzzy(i/10, "Vel. servico"))
print()

for i in range(10):
    print("ql serv", i, to_fuzzy(i/10, "Qual. servico"))
print()
    
for i in range(10):
    print("qual com", i, to_fuzzy(i/10, "Qual. Comida"))
print()

for i in range(10):
    print("simp", i, to_fuzzy(i/10, "Simp. Garcom"))





