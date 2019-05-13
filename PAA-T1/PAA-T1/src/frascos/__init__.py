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
        print(quantidade_de_pedacos)
        return quantidade_de_pedacos
    
    def calcular_resto(self):
        self.quantidade_de_pedacos = math.floor(self.quantidade_de_pedacos)
        self.altura_corrigida = pow(self.quantidade_de_pedacos, self.garrafas)
        self.resto = self.altura - self.altura_corrigida
        self.tamanho_de_pedaco = self.altura_corrigida
            
    def iteracao_para_descobrir_onde_quebra(self):
        print ("Testando uma de " + str(self.garrafas) + " garrafas.")
        self.tamanho_de_pedaco /= self.quantidade_de_pedacos
    
        quebrou = False
        quantidade_real_de_pedacos = self.quantidade_de_pedacos

        if (self.resto > 0):
            quantidade_real_de_pedacos += 1

        altura_de_teste = 0
        qual_pedaco = 0
        
        for qual_pedaco in range(quantidade_real_de_pedacos):
            print("For " + str(qual_pedaco))
            altura_de_teste = round(self.altura_minima) + round(self.tamanho_de_pedaco) * qual_pedaco
            
            print("alt_de_teste = " + str(altura_de_teste))
            
            if self.e_ai_quebrou(altura_de_teste):
                    
                quebrou = True
                    
                if (self.garrafas == 1) or (altura_de_teste == 1):
                    result = self.o_resultado_e(qual_pedaco)
                    return result
            
                break
            
        if (self.garrafas == 1):
            return "Garrafa aguentou todas as quedas"
    
        else:
            nova_altura_minima = altura_de_teste - round(self.tamanho_de_pedaco)
            nova_altura_maxima = altura_de_teste
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