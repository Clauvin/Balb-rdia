import frascos

testar_conjunto = True

if testar_conjunto:
    
    for i in range(1,101):
        
        teste_1 = frascos.Frascos33NaoBinario(1, 100, i, 0, 0, False)
        if teste_1.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_1, altura " + str(i))
            
    for i in range(1,102):
        
        teste_2 = frascos.Frascos33NaoBinario(1, 101, i, 0, 0, False)
        if teste_2.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_2, altura " + str(i))
            
    for i in range(1, 54036):
        
        teste_3 = frascos.Frascos33NaoBinario(1, 54035, i, 0, 0, False)
        if teste_3.iteracao_de_onde_quebra() != i:
            print ("Erro em teste_3, altura " + str(i))
        