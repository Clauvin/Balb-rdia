import random
import math

conjunto_de_instancias = []
instancia = []

lista_de_bits = [2, 4, 8, 16, 32, 64, 128, 256]
valores_de_bits = []  

valores_de_frascos = []
    
def criar_conjunto_de_instancias():
    for bits in lista_de_bits:
        randomized_small = 1
        
        lower_limit = 2
        upper_limit = pow(2,bits) - 2
    
        randomized_any = random.randint(lower_limit, upper_limit)           
        valores_de_bits.append(randomized_small)
        valores_de_bits.append(randomized_any)

def criar_conjunto_de_frascos():
    for bits in lista_de_bits:
        um_frasco = 1
        dois_frascos = 2
        bits_frascos = None
        infinitos_frascos = -1
        
        valores_de_frascos.append(um_frasco)
        valores_de_frascos.append(dois_frascos)
        bits_frascos = bits
        valores_de_frascos.append(bits_frascos)
        valores_de_frascos.append(infinitos_frascos)
              
        
criar_conjunto_de_instancias()
criar_conjunto_de_frascos()

