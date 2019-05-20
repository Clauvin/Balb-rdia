from conversor_poggi import Conversor_Arquivos
import frascos
from frascos import Frascos33

bignum_32_01 = True
bignum_32_02 = True
bignum_64_01 = True
bignum_64_02 = True
bignum_128_01 = True
bignum_128_02 = True
bignum_192_01 = True
bignum_192_02 = True
bignum_256_01 = True
bignum_256_02 = True

conversor_arquivos = None
teste_garrafas = None 

def roda_teste_sob_arquivo(entrada):
    conversor_arquivos = None
    conversor_arquivos = Conversor_Arquivos(entrada)
    conversor_arquivos.guardar_binarios()
    teste_garrafas = None
    for altura_quebra in conversor_arquivos.get_conjunto_de_inteiros():
        teste_garrafas = Frascos33(1, conversor_arquivos.altura_maxima,
                                    altura_quebra, 0, 0, False)
        result = teste_garrafas.iteracao_de_onde_quebra() 
        if (result == altura_quebra):
            print (str(result) + " certo")
        else:
            print ("erro em " + str(altura_quebra) +
                    ", resultado foi " + str(altura_maxima))

if bignum_32_01:
    print("bignum_32_01")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_32_01.dat")
    print("-------------------")
    
if bignum_32_02:
    print("bignum_32_02")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_32_02.dat")
    print("-------------------")

if bignum_64_01:
    print("bignum_64_01")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_64_01.dat")
    print("-------------------")
    
if bignum_64_02:
    print("bignum_64_02")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_64_02.dat")
    print("-------------------")
    
if bignum_128_01:
    print("bignum_128_01")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_128_01.dat")
    print("-------------------")
    
if bignum_128_02:
    print("bignum_128_02")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_128_02.dat")
    print("-------------------")
    
if bignum_192_01:
    print("bignum_192_01")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_192_01.dat")
    print("-------------------")
    
if bignum_192_02:
    print("bignum_192_02")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_192_02.dat")
    print("-------------------")
    
if bignum_256_01:
    print("bignum_256_01")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_256_01.dat")
    print("-------------------")
    
if bignum_256_02:
    print("bignum_256_02")
    roda_teste_sob_arquivo("../frascos_entradas_bigdata/bignum_256_02.dat")
    print("-------------------")