import frascos

teste_correto = frascos.Frascos(100, 2, 53)
resultado_correto = teste_correto.descobrir_onde_quebra()
print("Resultado do teste_correto: " + str(resultado_correto))

teste_quebrado_em_altura = frascos.Frascos(-100, 2, 53)

teste_quebrado_em_garrafas = frascos.Frascos(100, -2, 53)

teste_quebrado_em_onde_quebra = frascos.Frascos(100, 2, -53)