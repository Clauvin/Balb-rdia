import leitura_de_dados
from leitura_de_dados import LeitorDeDadosDoPoggi

class Conversor_Arquivos:
    
    leitor_de_dados = None
    nome_do_arquivo = None
    conjunto_de_inteiros = []
    altura_maxima = None
    
    def __init__(self, nome_do_arquivo):
        self.set_nome_do_arquivo(nome_do_arquivo)

    def set_nome_do_arquivo(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        self.leitor_de_dados = LeitorDeDadosDoPoggi(nome_do_arquivo)
        
    def get_conjunto_de_inteiros(self):
        return self.conjunto_de_inteiros
    
    def get_altura_maxima(self):
        return self.altura_maxima
        
    def guardar_binarios(self):
        self.leitor_de_dados.open_file()
        self.leitor_de_dados.copy_text()
        self.leitor_de_dados.close_file()
        self.leitor_de_dados.adjust_file_characters()
        
        
        file_characters = self.leitor_de_dados.get_file_characters()
        divided_first_line = file_characters[0].split()
        self.altura_maxima = self.make_altura_maxima(int(divided_first_line[0]))
        quantity = int(divided_first_line[1])
        counter = 1
        
        self.conjunto_de_inteiros = []
        for counter in range(counter, quantity+1):
            self.conjunto_de_inteiros.append(
                self.string_binary_to_long(file_characters[counter]))
    
    def make_altura_maxima(self, quant_de_bits):
        
        altura_binaria = ""
        for i in range(0, quant_de_bits):
            altura_binaria += "1"
            
        return int(altura_binaria,2)
        
        
    
    def string_binary_to_long(self, string_binary):
        return int(string_binary, 2)
        
    
        