import frascos

if False:

    teste_correto = frascos.FrascosTresPontoDois(100, 2, 53)
    resultado_correto = teste_correto.descobrir_onde_quebra()
    print("Resultado do teste_correto: " + str(resultado_correto))
    
    teste_quebrado_em_altura = frascos.FrascosTresPontoDois(-100, 2, 53)
    
    teste_quebrado_em_garrafas = frascos.FrascosTresPontoDois(100, -2, 53)
    
    teste_quebrado_em_onde_quebra = frascos.FrascosTresPontoDois(100, 2, -53)
    
    teste_correto_2 = frascos.FrascosTresPontoDois(1000, 3, 245)
    resultado_correto_2 = teste_correto_2.descobrir_onde_quebra()
    print("Resultado do teste_correto_2: " + str(resultado_correto_2))
    
    teste_correto_3 = frascos.FrascosTresPontoDois(1001, 3, 1001)
    resultado_correto_3 = teste_correto_3.descobrir_onde_quebra()
    print("Resultado do teste_correto_3: " + str(resultado_correto_3))
    
    teste_correto_4 = frascos.FrascosTresPontoDois(1001, 15, 1)
    resultado_correto_4 = teste_correto_4.descobrir_onde_quebra()
    print("Resultado do teste_correto_4: " + str(resultado_correto_4))
    
    teste_errado_1 = frascos.FrascosTresPontoDois(1001, 10, 2)
    resultado_errado_1 = teste_errado_1.descobrir_onde_quebra()
    print("Resultado do teste_errado_1: " + str(resultado_errado_1))
    print("Tudo bem, o algoritmo naturalmente nao funciona mesmo nesse caso.")
    
    teste_correto_6 = frascos.FrascosTresPontoDois(1001, 8, 5)
    resultado_correto_6 = teste_correto_6.descobrir_onde_quebra()
    print("Resultado do teste_correto_6: " + str(resultado_correto_6))
    
    teste_correto_7 = frascos.FrascosTresPontoDois(1001, 2, 1)
    resultado_correto_7 = teste_correto_7.descobrir_onde_quebra()
    print("Resultado do teste_correto_7: " + str(resultado_correto_7))
    
    teste_correto_8 = frascos.FrascosTresPontoDois(1500, 3, 457)
    resultado_correto_8 = teste_correto_8.descobrir_onde_quebra()
    print("Resultado do teste_correto_8: " + str(resultado_correto_8))
    
    teste_correto_9 = frascos.FrascosTresPontoDois(100567, 4, 100001)
    resultado_correto_9 = teste_correto_9.descobrir_onde_quebra()
    print("Resultado do teste_correto_9: " + str(resultado_correto_9))

if False:
    
    teste_vn_correto_1 = frascos.Frascos32Melhorado(1, 100, 2, 53)
    resultado_vn_correto_1 = teste_vn_correto_1.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_1: " + str(resultado_vn_correto_1))
    
    teste_vn_quebrado_em_altura = frascos.Frascos32Melhorado(-100, -50, 2, 53)
    
    teste_vn_quebrado_em_garrafas = frascos.Frascos32Melhorado(1, 100, -2, 53)
    
    teste_vn_quebrado_em_onde_quebra = frascos.Frascos32Melhorado(1, 100, 2, -53)
    
    teste_vn_correto_2 = frascos.Frascos32Melhorado(1, 1000, 3, 245)
    resultado_vn_correto_2 = teste_vn_correto_2.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_2: " + str(resultado_vn_correto_2))
    
    teste_vn_correto_3 = frascos.Frascos32Melhorado(1, 1001, 3, 1001)
    resultado_vn_correto_3 = teste_vn_correto_3.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_3: " + str(resultado_vn_correto_3))
    
    teste_vn_correto_4 = frascos.Frascos32Melhorado(1, 1001, 15, 1)
    resultado_vn_correto_4 = teste_vn_correto_4.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_4: " + str(resultado_vn_correto_4))
    
    teste_vn_correto_6 = frascos.Frascos32Melhorado(1, 1001, 8, 5)
    resultado_vn_correto_6 = teste_vn_correto_6.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_6: " + str(resultado_vn_correto_6))
    
    teste_vn_correto_7 = frascos.Frascos32Melhorado(1, 1001, 2, 1)
    resultado_vn_correto_7 = teste_vn_correto_7.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_7: " + str(resultado_vn_correto_7))
    
    teste_vn_correto_8 = frascos.Frascos32Melhorado(1, 1500, 3, 457)
    resultado_vn_correto_8 = teste_vn_correto_8.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_8: " + str(resultado_vn_correto_8))

    teste_vn_correto_9 = frascos.Frascos32Melhorado(1, 100567, 4, 100001)
    resultado_vn_correto_9 = teste_vn_correto_9.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_9: " + str(resultado_vn_correto_9))
 
if False:
    teste_vn_correto_9 = frascos.Frascos32Melhorado(1, 5000000, 40000, 442524)
    resultado_vn_correto_9 = teste_vn_correto_9.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_9: " + str(resultado_vn_correto_9))
    
for i in range(60000,62000):
    teste_final = frascos.Frascos32Melhorado(32768, 65536, 1, i)
    resultado_final = teste_final.iteracao_para_descobrir_onde_quebra()
    print("Resultado final = " + str(resultado_final))