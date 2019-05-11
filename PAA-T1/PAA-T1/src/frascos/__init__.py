import math

class Frascos:
    
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
        return math.pow(self.altura, 1/self.garrafas)
    
    def calcular_resto(self):
        self.quantidade_de_pedacos_corrigidos = math.floor(self.quantidade_de_pedacos)
        self.altura_corrigida = pow(self.quantidade_de_pedacos_corrigidos, self.garrafas)
        self.resto = self.altura - self.altura_corrigida
        self.tamanho_de_pedaco = self.altura_corrigida
        
    def variaveis_tem_valores_corretos(self, altura, garrafas, onde_quebra):
        if ((altura <= 0) or (garrafas <= 0) or (onde_quebra <= 0)):
            if (altura <= 0): print ("Ei, voce esta passando altura <= 0, ela precisa ser positiva.")
            if (garrafas <= 0): print ("Precisamos de uma garrafa no minimo pra testar...")
            if (onde_quebra <= 0): print ("Entao a garrafa nao aguenta existir...")
            return True
        return False
    
        
    def descobrir_onde_quebra(self):
        for i in range(self.garrafas):
            self.tamanho_de_pedaco /= self.quantidade_de_pedacos_corrigidos
    
            quebrou = False
            
            #print("tamanho de pedaco " + str(self.tamanho_de_pedaco))
            if (i == self.garrafas - 1) and (self.altura_inicial + self.quantidade_de_pedacos_corrigidos >= self.altura):
                self.quantidade_de_pedacos_corrigidos += self.resto
            for qual_pedaco in range(self.quantidade_de_pedacos_corrigidos):
                altura_de_teste = round(self.altura_inicial) + round(self.tamanho_de_pedaco) * qual_pedaco
                #print("altura_de_teste " + str(altura_de_teste))
                if self.e_ai_quebrou(altura_de_teste):
                    quebrou = True
                    if (i == self.garrafas - 1):
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
        print("Qual pedaco" + str(qual_pedaco))
        print("Altura inicial = " + str(self.altura_inicial))
        print("Altura final = " + str(self.altura_final))