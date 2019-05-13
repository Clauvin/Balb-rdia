import frascos
from test.support import _1M

if False:

    teste_correto = frascos.FrascosDoisPontoDois(100, 2, 53)
    resultado_correto = teste_correto.descobrir_onde_quebra()
    print("Resultado do teste_correto: " + str(resultado_correto))
    
    teste_quebrado_em_altura = frascos.FrascosDoisPontoDois(-100, 2, 53)
    
    teste_quebrado_em_garrafas = frascos.FrascosDoisPontoDois(100, -2, 53)
    
    teste_quebrado_em_onde_quebra = frascos.FrascosDoisPontoDois(100, 2, -53)
    
    teste_correto_2 = frascos.FrascosDoisPontoDois(1000, 3, 245)
    resultado_correto_2 = teste_correto_2.descobrir_onde_quebra()
    print("Resultado do teste_correto_2: " + str(resultado_correto_2))
    
    teste_correto_3 = frascos.FrascosDoisPontoDois(1001, 3, 1001)
    resultado_correto_3 = teste_correto_3.descobrir_onde_quebra()
    print("Resultado do teste_correto_3: " + str(resultado_correto_3))
    
    teste_correto_4 = frascos.FrascosDoisPontoDois(1001, 15, 1)
    resultado_correto_4 = teste_correto_4.descobrir_onde_quebra()
    print("Resultado do teste_correto_4: " + str(resultado_correto_4))
    
    teste_errado_1 = frascos.FrascosDoisPontoDois(1001, 10, 2)
    resultado_errado_1 = teste_errado_1.descobrir_onde_quebra()
    print("Resultado do teste_errado_1: " + str(resultado_errado_1))
    print("Tudo bem, o algoritmo naturalmente nao funciona mesmo nesse caso.")
    
    teste_correto_6 = frascos.FrascosDoisPontoDois(1001, 8, 5)
    resultado_correto_6 = teste_correto_6.descobrir_onde_quebra()
    print("Resultado do teste_correto_6: " + str(resultado_correto_6))
    
    teste_correto_7 = frascos.FrascosDoisPontoDois(1001, 2, 1)
    resultado_correto_7 = teste_correto_7.descobrir_onde_quebra()
    print("Resultado do teste_correto_7: " + str(resultado_correto_7))
    
    teste_correto_8 = frascos.FrascosDoisPontoDois(1500, 3, 457)
    resultado_correto_8 = teste_correto_8.descobrir_onde_quebra()
    print("Resultado do teste_correto_8: " + str(resultado_correto_8))
    
    teste_correto_9 = frascos.FrascosDoisPontoDois(100567, 4, 100001)
    resultado_correto_9 = teste_correto_9.descobrir_onde_quebra()
    print("Resultado do teste_correto_9: " + str(resultado_correto_9))

if True:
    
    teste_vn_correto_1 = frascos.Frascos22Melhorado(1, 100, 2, 53)
    resultado_vn_correto_1 = teste_vn_correto_1.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_1: " + str(resultado_vn_correto_1))
    
    teste_vn_quebrado_em_altura = frascos.Frascos22Melhorado(-100, -50, 2, 53)
    
    teste_vn_quebrado_em_garrafas = frascos.Frascos22Melhorado(1, 100, -2, 53)
    
    teste_vn_quebrado_em_onde_quebra = frascos.Frascos22Melhorado(1, 100, 2, -53)
    
    teste_vn_correto_2 = frascos.Frascos22Melhorado(1, 1000, 3, 245)
    resultado_vn_correto_2 = teste_vn_correto_2.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_2: " + str(resultado_vn_correto_2))
    
    teste_vn_correto_3 = frascos.Frascos22Melhorado(1, 1001, 3, 1001)
    resultado_vn_correto_3 = teste_vn_correto_3.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_3: " + str(resultado_vn_correto_3))
    
    teste_vn_correto_4 = frascos.Frascos22Melhorado(1, 1001, 15, 1)
    resultado_vn_correto_4 = teste_vn_correto_4.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_vn_correto_4: " + str(resultado_vn_correto_4))
    
    teste_vn_correto_6 = frascos.Frascos22Melhorado(1, 1001, 8, 5)
    resultado_vn_correto_6 = teste_vn_correto_6.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_6: " + str(resultado_vn_correto_6))
    
    teste_vn_correto_7 = frascos.Frascos22Melhorado(1, 1001, 2, 1)
    resultado_vn_correto_7 = teste_vn_correto_7.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_7: " + str(resultado_vn_correto_7))
    
    teste_vn_correto_8 = frascos.Frascos22Melhorado(1, 1500, 3, 457)
    resultado_vn_correto_8 = teste_vn_correto_8.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_8: " + str(resultado_vn_correto_8))

    teste_vn_correto_9 = frascos.Frascos22Melhorado(1, 100567, 4, 100001)
    resultado_vn_correto_9 = teste_vn_correto_9.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_9: " + str(resultado_vn_correto_9))
    
    teste_vn_correto_9 = frascos.Frascos22Melhorado(1, 5000000, 40000, 442524)
    resultado_vn_correto_9 = teste_vn_correto_9.iteracao_para_descobrir_onde_quebra()
    print("Resultado do teste_correto_9: " + str(resultado_vn_correto_9))