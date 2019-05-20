import frascos
import conversor_poggi
import leitura_de_dados
from leitura_de_dados import LeitorDeDadosDoPoggi
from conversor_poggi import Conversor_Arquivos

testar_conjunto_33NaoBinario = False

if testar_conjunto_33NaoBinario:
    
    for i in range(1,101):
        
        teste_1 = frascos.Frascos33(1, 100, i, 0, 0, False)
        if teste_1.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_1, altura " + str(i))
            
    for i in range(1,102):
        
        teste_2 = frascos.Frascos33(1, 101, i, 0, 0, False)
        if teste_2.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_2, altura " + str(i))
            
    for i in range(1, 54036):
        
        teste_3 = frascos.Frascos33(1, 54035, i, 0, 0, False)
        if teste_3.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_3, altura " + str(i))
            
    for i in range(1, 54036):
        
        teste_4 = frascos.Frascos33(1, 54035, i, 0, 0, True)
        if teste_4.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_3, altura " + str(i))
            
testar_leitura_de_dados = False

if testar_leitura_de_dados:
    
    leitor = LeitorDeDadosDoPoggi("../frascos_entradas_bigdata/bignum_128_01.dat")
    leitor.open_file()
    leitor.copy_text()
    leitor.close_file()
    leitor.adjust_file_characters()
    
    print(leitor.file_characters[0])
    print(leitor.file_characters[1])
    print(leitor.file_characters[2])
    
testar_conversao_de_dados = True

if testar_conversao_de_dados:
    
    conversor = Conversor_Arquivos("../frascos_entradas_bigdata/bignum_32_01.dat")
    
    conversor.guardar_binarios()
    
    inteiros = conversor.get_conjunto_de_inteiros()
    
    print(inteiros[0])
    print(conversor.get_altura_maxima())
        