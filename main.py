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
def to_fuzzy(d, m):
    pass

def fuzzifier(data, metrics):
    r = []
    for i in range(len(len(data))):
        r.append(to_fuzzy(data[i], metrics[i]))

    return r

# ???????
# talvez um peso para cada metrica
# se ql serv for boa, vel do serv for boa, ql da com for boa E simp do garcom for ruim, entao gorjeita ruim
# se ql serv for ruim, vel do serv for ruim, ql da com for ruim E simp do garcom for boa, entao gorjeita media
# baseado nas regras (if elses)
def fuzzy_operations(fuzzy_values):
    pass

# possivel distribuiçao normal
# considerando a palavra recebida
# onde comeca e acaba os valores de gorjeta possivel para cada palavra(ruim, medio, bom)
# bom = [0, 0.2]
# medio = [0.2, 0.5] 0.37  * 25 = 9.25
# ruim = [0.5, 1]
def defuzzifier(fuzzy_final):
    pass



def main():
    # na forma de float entre 0 e 1
    user_inputs = [0.5, 0.6, 0.4, 0.9]
    metrics = ["Qual. servico", "Vel. servico", "Qual. Comida", "Simp. Garcom"]
    
    fuzzy_values = fuzzifier(user_inputs, metrics)

    fuzzy_final = fuzzy_operations(fuzzy_values)

    abs_value = defuzzifier(fuzzy_final)

    return abs_value * 25
























