import random
import math
import cpuTimer
from conversor_poggi import Conversor_Arquivos
from frascos import Frascos32Melhorado, Frascos33
import teste_escritor_ods
from teste_escritor_ods import save_new_sheet

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
    criar_conjunto_de_instancias()
    criar_conjunto_de_frascos()
    
    posicao_bits = 0
    posicao_frascos = 0
    teste_de_n_frascos = None
    teste_de_infinitos_frascos = None
    timer = cpuTimer.CPUTimer(0)
    
    for i in range(len(lista_de_bits)):
        
        altura_bits = lista_de_bits[i]
        altura = pow(2,lista_de_bits[i])-1
        
        timer.reset()
        
        #print ("Teste de um frasco - " + str(altura_bits) + 
        #       " bits, quebra em 1, altura maxima = " + str(altura) + 
        #       ", frascos = " + str(valores_de_frascos[i*4]))
        #timer.start()
        #menor_valor_um_frasco = Frascos32Melhorado(1, altura,
        #                             valores_de_frascos[i*4], valores_de_bits[i*2])
        #menor_valor_um_frasco.iteracao_para_descobrir_onde_quebra()
        #timer.stop()
        #tempo_usado(timer)
        
        #print ("Teste de dois frascos - " + str(altura_bits) + 
        #       " bits, quebra em 1, altura maxima = " + str(altura) + 
        #       ", frascos = " + str(valores_de_frascos[i*4+1]))
        #timer.start()
        #menor_valor_dois_frascos = Frascos32Melhorado(1, altura,
        #                             valores_de_frascos[i*4+1], valores_de_bits[i*2])
        #menor_valor_dois_frascos.iteracao_para_descobrir_onde_quebra()
        #timer.stop()
        #tempo_usado(timer)
        
        print ("Teste de " + str(valores_de_frascos[i*4+2]) +
                 " frascos - " + str(altura_bits) + 
                 " bits, quebra em 1, altura maxima = " + str(altura) + 
                 ", frascos = " + str(valores_de_frascos[i*4+2]))
        timer.start()
        menor_valor_bits_frascos = Frascos32Melhorado(1, altura,
                                     valores_de_frascos[i*4+2], valores_de_bits[i*2])
        menor_valor_bits_frascos.iteracao_para_descobrir_onde_quebra()
        timer.stop()
        tempo_usado(timer)
        
        
        print ("Teste de infinitos frascos - " + str(altura_bits) + 
                 " bits, quebra em 1, altura maxima = " + str(altura))
        timer.start()
        menor_valor_infinitos_frascos = Frascos33(1, altura,
                                             valores_de_frascos[i*4+3], 0, 0, False)
        menor_valor_infinitos_frascos.iteracao_de_onde_quebra()
        timer.stop()
        tempo_usado(timer)

        #print ("Teste de um frasco - " + str(altura_bits) + 
        #       " bits, quebra em " + str(valores_de_bits[i*2+1]) +
        #       ", altura maxima = " + str(altura) + 
        #       ", frascos = " + str(valores_de_frascos[i*4]))
        #timer.start()
        #random_valor_um_frasco = Frascos32Melhorado(1, altura,
        #                             valores_de_frascos[i*4], valores_de_bits[i*2+1])
        #random_valor_um_frasco.iteracao_para_descobrir_onde_quebra()
        #timer.stop()
        #tempo_usado(timer)
        
        #print ("Teste de dois frascos - " + str(altura_bits) + 
        #       " bits, quebra em " + str(valores_de_bits[i*2+1]) +
        #       ", altura maxima = " + str(altura) + 
        #       ", frascos = " + str(valores_de_frascos[i*4]))
        #timer.start()
        #random_valor_dois_frascos = Frascos32Melhorado(1, altura,
        #                             valores_de_frascos[i*4+1], valores_de_bits[i*2+1])
        #random_valor_dois_frascos.iteracao_para_descobrir_onde_quebra()
        #timer.stop()
        #tempo_usado(timer)
        
        print ("Teste de " + str(valores_de_frascos[i*4+2]) +
                 " frascos - " + str(altura_bits) + 
                 " bits, quebra em " + str(valores_de_bits[i*2+1]) +
                 ", altura maxima = " + str(altura) + 
                 ", frascos = " + str(valores_de_frascos[i*4+2]))
        timer.start()
        random_valor_bits_frascos = Frascos32Melhorado(1, altura,
                                     valores_de_frascos[i*4+2], valores_de_bits[i*2+1])
        random_valor_bits_frascos.iteracao_para_descobrir_onde_quebra()        
        timer.stop()
        tempo_usado(timer)
        
        print ("Teste de infinitos frascos - " + str(altura_bits) + 
                 " bits, quebra em " + str(valores_de_bits[i*2+1]) +
                 ", altura maxima = " + str(altura))
        timer.start()
        random_valor_infinitos_frascos = Frascos33(1, altura,
                                             valores_de_bits[i*2+1], 0, 0, False)
        random_valor_infinitos_frascos.iteracao_de_onde_quebra()
        timer.stop()
        tempo_usado(timer)
        
def tempo_usado(timer):
    print ("Tempo usado em ms = " + str(timer.get_time("last", "ms")))       
        
bignum_32_01 = False
bignum_32_02 = False
bignum_64_01 = False
bignum_64_02 = False
bignum_128_01 = False
bignum_128_02 = False
bignum_192_01 = False
bignum_192_02 = False
bignum_256_01 = False
bignum_256_02 = False

conversor_arquivos = None
teste_garrafas = None 

def roda_teste_sob_arquivo_32(entrada, garrafas):
    timer = cpuTimer.CPUTimer(0)
    conversor_arquivos = None
    conversor_arquivos = Conversor_Arquivos(entrada)
    conversor_arquivos.guardar_binarios()
    teste_garrafas = None
    
    tempo_total = 0
    iteracoes = 0
    while tempo_total < 5000:
        timer.start()
        for altura_quebra in conversor_arquivos.get_conjunto_de_inteiros():
            teste_garrafas = Frascos32Melhorado(1,
                           conversor_arquivos.altura_maxima, garrafas, altura_quebra)
            result = teste_garrafas.iteracao_para_descobrir_onde_quebra()
        timer.stop()
        tempo_total += timer.get_time("last", "ms")
        iteracoes += 1
    print ("Media = " + str(tempo_total/iteracoes)) 

def roda_teste_sob_arquivo_33(entrada, nome_do_arquivo_para_tabela):
    conversor_arquivos = None
    conversor_arquivos = Conversor_Arquivos(entrada)
    conversor_arquivos.guardar_binarios()
    teste_garrafas = None
    
    timer = cpuTimer.CPUTimer(0)
    
    qual_algoritmo = "Frascos33"
    qual_arquivo = nome_do_arquivo_para_tabela
    qual_instancia_em_decimal = None
    qual_instancia_em_binario = None
    quantos_frascos = "infinitos"
    complexidade_teorica = 0
    tempo_de_cpu = 0
    razao = 0
    
    content = []
    
    for altura_quebra in conversor_arquivos.get_conjunto_de_inteiros():
        print("Indo")
        tempo_total = 0
        iteracoes = 0
        qual_instancia_em_decimal = bin(altura_quebra)
        qual_instancia_em_binario = altura_quebra

        
        iteracoes = 0
        
        while (tempo_total < 5000):
            timer.start()
            teste_garrafas = Frascos33(1, conversor_arquivos.altura_maxima,
                                        altura_quebra, 0, 0, False)
            result = teste_garrafas.iteracao_de_onde_quebra()
            timer.stop()
            tempo_total += timer.get_time("last", "ms")
            iteracoes += 1
        
        tempo_de_cpu = tempo_total / iteracoes
        
        content.append([qual_algoritmo, qual_arquivo, qual_instancia_em_decimal,
                        qual_instancia_em_binario, quantos_frascos, 
                        complexidade_teorica, tempo_de_cpu, razao])
        
    save_new_sheet(nome_do_arquivo_para_tabela, "Teste 1", content)
         
            
roda_teste_sob_arquivo_33("../frascos_entradas_bigdata/bignum_32_01.dat",
                          "Teste.ods")

if bignum_32_01:
    print("bignum_32_01")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_32_01.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_32_01.dat", 32)
    print("-------------------")
    
if bignum_32_02:
    print("bignum_32_02")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_32_02.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_32_02.dat", 32)
    print("-------------------")

if bignum_64_01:
    print("bignum_64_01")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_64_01.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_64_01.dat", 32)
    print("-------------------")
    
if bignum_64_02:
    print("bignum_64_02")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_64_02.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_64_02.dat", 32)
    print("-------------------")
    
if bignum_128_01:
    print("bignum_128_01")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_128_01.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_128_01.dat", 32)
    print("-------------------")
    
if bignum_128_02:
    print("bignum_128_02")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_128_02.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_128_02.dat", 32)
    print("-------------------")
    
if bignum_192_01:
    print("bignum_192_01")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_192_01.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_192_01.dat", 32)
    print("-------------------")
    
if bignum_192_02:
    print("bignum_192_02")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_192_02.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_192_02.dat", 32)
    print("-------------------")
    
if bignum_256_01:
    print("bignum_256_01")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_256_01.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_256_01.dat", 32)
    print("-------------------")
    
if bignum_256_02:
    print("bignum_256_02")
    roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_256_02.dat", 2)
    #roda_teste_sob_arquivo_32("../frascos_entradas_bigdata/bignum_256_02.dat", 32)
    print("-------------------")
    