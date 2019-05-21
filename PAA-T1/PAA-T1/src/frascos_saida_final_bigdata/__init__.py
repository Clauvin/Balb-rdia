import random
import math
import cpuTimer
from frascos import Frascos32Melhorado, Frascos33

conjunto_de_instancias = []
instancia = []

lista_de_bits = [32, 64, 128, 256]
lista_extra_de_bits = [2, 4, 8, 16]
valores_de_bits = []  

valores_de_frascos = []
    
def criar_conjunto_de_instancias():
    for bits in lista_de_bits:
        randomized_small = 1
        
        lower_limit = 2
        upper_limit = pow(2,bits) - 2
    
        randomized_any = random.randint(math.floor(upper_limit/2), upper_limit)           
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
 
def testar_velocidade():
    posicao_bits = 0
    posicao_frascos = 0
    teste_de_n_frascos = None
    teste_de_infinitos_frascos = None
    timer = cpuTimer.CPUTimer(0)
    
    for i in range(len(lista_de_bits)):
        
        altura_bits = lista_de_bits[i]
        altura = pow(2,lista_de_bits[i])-1
        
        timer.reset()
        
        print ("Teste de um frasco - " + str(altura_bits) + 
               " bits, quebra em 1, altura maxima = " + str(altura) + 
               ", frascos = " + str(valores_de_frascos[i*4]))
        timer.start()
        menor_valor_um_frasco = Frascos32Melhorado(1, altura,
                                     valores_de_frascos[i*4], valores_de_bits[i*2])
        timer.stop()
        tempo_usado(timer)
        
        print ("Teste de dois frascos - " + str(altura_bits) + 
               " bits, quebra em 1, altura maxima = " + str(altura) + 
               ", frascos = " + str(valores_de_frascos[i*4+1]))
        timer.start()
        menor_valor_dois_frascos = Frascos32Melhorado(1, pow(2,lista_de_bits[i])-1,
                                     valores_de_frascos[i*4+1], valores_de_bits[i*2])
        timer.stop()
        tempo_usado(timer)
        
        print ("Teste de " + str(valores_de_frascos[i*4+2]) +
                 " frascos - " + str(altura_bits) + 
                 " bits, quebra em 1, altura maxima = " + str(altura) + 
                 ", frascos = " + str(valores_de_frascos[i*4+2]))
        timer.start()
        menor_valor_bits_frascos = Frascos32Melhorado(1, pow(2,lista_de_bits[i])-1,
                                     valores_de_frascos[i*4+2], valores_de_bits[i*2])
        timer.stop()
        tempo_usado(timer)
        
        
        print ("Teste de infinitos frascos - " + str(altura_bits) + 
                 " bits, quebra em 1, altura maxima = " + str(altura))
        timer.start()
        menor_valor_infinitos_frascos = Frascos33(1, pow(2,lista_de_bits[i])-1,
                                             valores_de_frascos[i*4+3], 0, 0, False)
        timer.stop()
        tempo_usado(timer)

        print ("Teste de um frasco - " + str(altura_bits) + 
               " bits, quebra em " + str(valores_de_bits[i*2+1]) +
               ", altura maxima = " + str(altura) + 
               ", frascos = " + str(valores_de_frascos[i*4]))
        timer.start()
        random_valor_um_frasco = Frascos32Melhorado(1, pow(2,lista_de_bits[i])-1,
                                     valores_de_frascos[i*4], valores_de_bits[i*2+1])
        timer.stop()
        tempo_usado(timer)
        
        print ("Teste de dois frascos - " + str(altura_bits) + 
               " bits, quebra em " + str(valores_de_bits[i*2+1]) +
               ", altura maxima = " + str(altura) + 
               ", frascos = " + str(valores_de_frascos[i*4]))
        timer.start()
        random_valor_dois_frascos = Frascos32Melhorado(1, pow(2,lista_de_bits[i])-1,
                                     valores_de_frascos[i*4+1], valores_de_bits[i*2+1])
        timer.stop()
        tempo_usado(timer)
        
        print ("Teste de " + str(valores_de_frascos[i*4+2]) +
                 " frascos - " + str(altura_bits) + 
                 " bits, quebra em " + str(valores_de_bits[i*2+1]) +
                 ", altura maxima = " + str(altura) + 
                 ", frascos = " + str(valores_de_frascos[i*4+2]))
        timer.start()
        random_valor_bits_frascos = Frascos32Melhorado(1, pow(2,lista_de_bits[i])-1,
                                     valores_de_frascos[i*4+2], valores_de_bits[i*2+1])
        timer.stop()
        tempo_usado(timer)
        
        print ("Teste de infinitos frascos - " + str(altura_bits) + 
                 " bits, quebra em " + str(valores_de_bits[i*2+1]) +
                 ", altura maxima = " + str(altura))
        timer.start()
        random_valor_infinitos_frascos = Frascos33(1, pow(2,lista_de_bits[i])-1,
                                             valores_de_bits[i*2+1], 0, 0, False)
        timer.stop()
        tempo_usado(timer)
        
def tempo_usado(timer):
    print ("Tempo usado em ms = " + str(timer.get_time("last", "ms")))       
        
criar_conjunto_de_instancias()
criar_conjunto_de_frascos()

testar_velocidade()