class LeitorDeDadosDoPoggi:
    
    quantidade_de_bits = None
    quantidade_de_entradas = None
    entradas = None
    file_name = None
    file = None
    file_characters = None
    
    def __init__(self, file_name):
        self.file_name = file_name
        
    def open_file(self):
        self.file = open(self.file_name,"r")
    
    def copy_text(self):
        self.file_characters = self.file.readlines() 
        
    def close_file(self):
        self.file.close()
        
    