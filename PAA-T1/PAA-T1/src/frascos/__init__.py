import math

class FrascosDoisPontoDois:
    
    altura = 0
    altura_corrigida = 0
    garrafas = 0
    quantidade_de_pedacos = 0
    quantidade_de_pedacos_corrigidos = 0
    tamanho_de_pedaco = 0
    altura_inicial = 1
    altura_final = 0
    onde_quebra = 0
    resto = 0
    
    def __init__(self, altura, garrafas, onde_quebra):
        if self.variaveis_tem_valores_corretos(altura, garrafas, onde_quebra):
            return
        
        self.altura = altura
        self.altura_final = altura
        self.garrafas = garrafas
        self.quantidade_de_pedacos = self.calcular_quantidade_de_pedacos()
        self.onde_quebra = onde_quebra
        
        self.calcular_resto()
        
    def calcular_quantidade_de_pedacos(self):
        quantidade_de_pedacos = math.pow(self.altura, 1/self.garrafas)
        print(quantidade_de_pedacos)
        return quantidade_de_pedacos
    
    def calcular_resto(self):
        self.quantidade_de_pedacos_corrigidos = math.floor(self.quantidade_de_pedacos)
        self.altura_corrigida = pow(self.quantidade_de_pedacos_corrigidos, self.garrafas)
        self.resto = self.altura - self.altura_corrigida
        self.tamanho_de_pedaco = self.altura_corrigida
        #print(self.resto)
        
    def variaveis_tem_valores_corretos(self, altura, garrafas, onde_quebra):
        if ((altura <= 0) or (garrafas <= 0) or (onde_quebra <= 0)):
            if (altura <= 0): print ("Ei, voce esta passando altura <= 0, ela precisa ser positiva.")
            if (garrafas <= 0): print ("Precisamos de uma garrafa no minimo pra testar...")
            if (onde_quebra <= 0): print ("Entao a garrafa nao aguenta existir...")
            return True
        return False
    
        
    def descobrir_onde_quebra(self):
        for i in range(self.garrafas):
            print ("Garrafa " + str(i + 1))
            self.tamanho_de_pedaco /= self.quantidade_de_pedacos_corrigidos
            print ("Tamanho do pedaco = " + str(self.tamanho_de_pedaco))
    
            quebrou = False
            
            print("tamanho de pedaco " + str(self.tamanho_de_pedaco))
            if (i == self.garrafas - 1) and (self.altura_inicial + self.quantidade_de_pedacos_corrigidos >= self.altura):
                self.quantidade_de_pedacos_corrigidos += self.resto
            elif (i == self.garrafas - 1):
                self.quantidade_de_pedacos_corrigidos += 1
            for qual_pedaco in range(self.quantidade_de_pedacos_corrigidos):
                altura_de_teste = round(self.altura_inicial) + round(self.tamanho_de_pedaco) * qual_pedaco
                #print("altura_de_teste " + str(altura_de_teste))
                if self.e_ai_quebrou(altura_de_teste):
                    
                    quebrou = True
                    
                    if (i == self.garrafas - 1) or (altura_de_teste == 1):
                        return self.o_resultado_e(qual_pedaco)
  
                    self.escolher_pedaco_como_conjunto_de_alturas_de_teste(qual_pedaco)
                    
                    break

                if (qual_pedaco == self.quantidade_de_pedacos_corrigidos - 1) and (quebrou == False):
                    self.escolher_pedaco_como_conjunto_de_alturas_de_teste(qual_pedaco + 1)
                    
    def e_ai_quebrou(self, onde_deixaram_cair):
        if (self.onde_quebra <= onde_deixaram_cair):
            return True
        else: return False
        
    def o_resultado_e(self, qual_pedaco):
        return self.altura_inicial + self.tamanho_de_pedaco * qual_pedaco
        
    def escolher_pedaco_como_conjunto_de_alturas_de_teste(self, qual_pedaco):
        self.altura_final = self.altura_inicial + self.tamanho_de_pedaco * (qual_pedaco)
        self.altura_inicial = self.altura_inicial + self.tamanho_de_pedaco * (qual_pedaco - 1)
        print("Qual pedaco = " + str(qual_pedaco))
        print("Proxima altura inicial = " + str(self.altura_inicial))
        print("Proxima altura final = " + str(self.altura_final))
        
class Frascos22Melhorado:
    
    altura_minima = 0
    altura_maxima = 0
    altura = 0
    garrafas = 0
    quantidade_de_pedacos = 0
    tamanho_de_pedaco = 0
    onde_quebra = 0
    resto = 0
    
    def __init__(self, altura_minima, altura_maxima, garrafas, onde_quebra):
        if self.variaveis_tem_valores_corretos(altura_minima, altura_maxima,
           garrafas, onde_quebra):
            return
        
        self.altura_minima = altura_minima
        self.altura_maxima = altura_maxima
        self.altura = altura_maxima - altura_minima + 1
        self.garrafas = garrafas
        self.quantidade_de_pedacos = self.calcular_quantidade_de_pedacos()
        self.onde_quebra = onde_quebra
        self.calcular_resto()
    
    def variaveis_tem_valores_corretos(self, altura_minima, altura_maxima,
                                        garrafas, onde_quebra):
        if ((altura_minima <= 0) or (altura_maxima <= 0) or
             (garrafas <= 0) or (onde_quebra <= 0)):
            if (altura_minima <= 0): print ("Ei, voce esta passando altura_minima <= 0, ela precisa ser positiva.")
            if (altura_maxima <= 0): print ("Ei, voce esta passando altura_maxima <= 0, ela precisa ser positiva.")
            if (garrafas <= 0): print ("Precisamos de uma garrafa no minimo pra testar...")
            if (onde_quebra <= 0): print ("Entao a garrafa nao aguenta existir...")
            return True
        if (altura_maxima - altura_minima < 0):
            print ("Ei, a sua regua aponta para baixo.")
            return True
        return False
        
    def calcular_quantidade_de_pedacos(self):
        quantidade_de_pedacos = math.pow(self.altura, 1/self.garrafas)
        return quantidade_de_pedacos
    
    def calcular_resto(self):
        self.quantidade_de_pedacos = math.floor(self.quantidade_de_pedacos)
        self.altura_corrigida = pow(self.quantidade_de_pedacos, self.garrafas)
        self.resto = self.altura - self.altura_corrigida
        self.tamanho_de_pedaco = self.altura_corrigida
            
    def iteracao_para_descobrir_onde_quebra(self):
        self.tamanho_de_pedaco /= self.quantidade_de_pedacos
    
        quebrou = False
        quantidade_real_de_pedacos = self.quantidade_de_pedacos

        if (self.resto > 0):
            quantidade_real_de_pedacos += 1
            
        altura_de_teste = 0
        qual_pedaco = 0
        
        for qual_pedaco in range(quantidade_real_de_pedacos):
            altura_de_teste = round(self.altura_minima) + round(self.tamanho_de_pedaco) * qual_pedaco
                   
            if self.e_ai_quebrou(altura_de_teste):
                    
                quebrou = True
                    
                if (self.garrafas == 1) or (altura_de_teste == 1):
                    result = self.o_resultado_e(qual_pedaco)
                    return result
            
                break
        
        if (self.garrafas == 1):
            return "Garrafa aguentou todas as quedas"
    
        else:
            if (quebrou == True):
                nova_altura_minima = altura_de_teste - round(self.tamanho_de_pedaco)
                nova_altura_maxima = altura_de_teste
                novas_garrafas = self.garrafas - 1
                
            else:
                nova_altura_minima = altura_de_teste
                nova_altura_maxima = self.altura_maxima
                novas_garrafas = self.garrafas - 1
            
            return self.criar_novo_teste(nova_altura_minima, nova_altura_maxima, 
                             novas_garrafas, self.onde_quebra)
                    
    def e_ai_quebrou(self, onde_deixaram_cair):
        if (self.onde_quebra <= onde_deixaram_cair):
            return True
        else: return False

    def o_resultado_e(self, qual_pedaco):
        result = self.altura_minima + self.tamanho_de_pedaco * qual_pedaco
        return result

    def criar_novo_teste(self, nova_altura_minima, nova_altura_maxima, 
                             novas_garrafas, onde_quebra):
        novo_teste = Frascos22Melhorado(nova_altura_minima, nova_altura_maxima,
                                         novas_garrafas, onde_quebra)
        if (novo_teste != None):
            return novo_teste.iteracao_para_descobrir_onde_quebra()

"""
3.3:

FrascosDoisPontoDois foi feita para inicialmente resolver a 3.1 e então a 3.2...
...mas ao ver que a forma que eu escolhi para lidar com o problema do resto
não funcionou bem, fiz o Frascos 2 2 Melhorado.

O código dessa classe funciona muito bem para o problema... exceto quando
são tantas garrafas que o algoritmo tenta checar TODAS as alturas, em ordem
crescente.

Não resolvi esse problema porquê ele faz ponte para o problema da 3.3

Percebe-se na 3.2 que com o teto da complexidade igual a k * n ^ (1/k),
quanto maior o k, mais rápido é o algoritmo...

...até que  n ^ (1/k) (que representa a quantidade de testes a se fazer em
cada iteração do código seja igual ou menor que um.

Ou seja, chega um ponto em que a quantidade de garrafas é mais um empecilho que uma
vantagem. Tendo isso em mente, qual a menor complexidade assintótica?

Bom, temos duas situações que limitam o algoritmo.

1 - Uma onde temos uma garrafa apenas, então precisamos testar todas as alturas
em ordem crescente, ou seja, k = 1 e O(n)

2 - Uma onde temos tantas garrafas que n ^ (1/k) = 1 (porquê não temos como
fazer menos que um teste de cada vez) e O(k).

Então se queremos um algoritmo mais rápido, precisamos que ele seja mais rápido
que um algoritmo linear.

Em O(k * n ^ (1/k)), k é uma constante, então temos O(n^(1/k)). Como reduzir
ao máximo O(n^(1/k)) sem cair em algo linear?

Se n^(1/k) não pode ser igual a 1, e se ele for igual a 2? Notar que nesse caso
k terá que ser grande o suficiente para que a raiz k-ésima reduza n para um valor
o mais próximo possível de 2...

...ou melhor. 2 aqui quer dizer temos dois testes por iteração, ou seja, o
equivalente a uma busca binária: dado um conjunto linear de alturas, fazemos 
um teste com uma garrafa no começo desse conjunto.

Se a garrafa quebrar, ótimo, se não, quebramos a garrafa no meio do conjunto.
Se a garrafa quebrar, pegamos o subconjunto da metade menor do conjunto e
fazemos o teste acima nesse subconjunto. Caso contrário, pegamos o subconjunto da
metade maior do conjunto.

Repetimos o processo até acharmos um conjunto de duas alturas, onde uma das duas
quebrará a garrafa e com isso teremos o limite procurado.

Esse processo tem a complexidade de O(log n), n sendo o número de alturas, e com
log2 n sendo o número de garrafas.

Ou seja, com digamos, n = 100, log2 n = 6.64 (arredondaremos para 7):

Teste 1 = Conjunto de 100 garrafas.
Teste 2 = Conjunto de 50 garrafas.
Teste 3 = Conjunto de 25 garrafas.
Teste 4 = Conjunto de 12 garrafas.
Teste 5 = Conjunto de 6 garrafas.
Teste 6 = Conjunto de 3 garrafas.
Teste 7 = Conjunto de 2 garrafas. <- Nesse caso, talvez não precisemos
                                    do sétimo teste MAS considerando o pior
                                    dos casos, vamos ficar com o sétimo teste.

Fica a pergunta: existem testes melhores que a busca binária eles podem ser
aplicados a esse problema?

Busca exponencial - começa testando valores iguais a potências crescentes de 2 até
achar um valor menor que o valor buscado, então passa para busca binária.
    - Esse é bom só se o número procurado (no nosso caso a altura) estiver perto
        do começo dos números a serem testados.
    - Isso leva a um bom fator de comparação: um algoritmo melhor que o de busca
        binária precisa ser capaz de cortar mais que a metade do conjunto de teste
        a cada iteração.
        
O problema é: sem NADA que dê uma direção melhor para cortes fora da metade, temos
como nos aproveitar de testes iniciais fora da metade do conjunto para sermos mais
rápidos que O(log2 n)?



"""