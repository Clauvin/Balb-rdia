import frascos

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