import math

class Frascos:
    
    altura = 0
    garrafas = 0
    quantidade_de_pedacos = 0
    tamanho_de_pedaco = 0
    altura_inicial = 1
    altura_final = 0
    onde_quebra = 0
    
    def __init__(self, altura, garrafas, onde_quebra):
        if ((altura <= 0) or (garrafas <= 0) or (onde_quebra <= 0)):
            if (altura <= 0): print ("Ei, voce esta passando altura <= 0, ela precisa ser positiva.")
            if (garrafas <= 0): print ("Precisamos de uma garrafa no minimo pra testar...")
            if (onde_quebra <= 0): print ("Entao a garrafa nao aguenta existir...")
            return
        self.altura = altura
        self.altura_final = altura
        self.garrafas = garrafas
        self.quantidade_de_pedacos = math.pow(altura, 1/garrafas)
        self.tamanho_de_pedaco = altura
        self.onde_quebra = onde_quebra
        
    def descobrir_onde_quebra(self):
        for i in range(self.garrafas):
            self.tamanho_de_pedaco /= self.quantidade_de_pedacos
            quebrou = False
            self.quantidade_de_pedacos = round(self.quantidade_de_pedacos)
            for qual_pedaco in range(self.quantidade_de_pedacos):
                print (qual_pedaco)
                altura_de_teste = self.altura_inicial + self.tamanho_de_pedaco * qual_pedaco
                if self.e_ai_quebrou(altura_de_teste):
                    quebrou = True
                    if (i == self.garrafas - 1):
                        return self.altura_inicial + self.tamanho_de_pedaco * qual_pedaco
                    escolher_pedaco_como_conjunto_de_alturas_de_teste(self, qual_pedaco)
                    break

                if (qual_pedaco == self.quantidade_de_pedacos - 1) and (quebrou == False):
                    escolher_pedaco_como_conjunto_de_alturas_de_teste(self, qual_pedaco)
                    
    def e_ai_quebrou(self, onde_deixaram_cair):
        print("onde_quebra " + str(self.onde_quebra))
        print("onde_deixaram_cair " + str(onde_deixaram_cair))
        if (self.onde_quebra <= onde_deixaram_cair):
            return True
        else: return False
        
    def escolher_pedaco_como_conjunto_de_alturas_de_teste(self, qual_pedaco):
        self.altura_inicial = self.altura_inicial + self.tamanho_de_pedaco * (qual_pedaco - 1)
        self.altura_final = self.altura_inicial + self.tamanho_de_pedaco * qual_pedaco
        