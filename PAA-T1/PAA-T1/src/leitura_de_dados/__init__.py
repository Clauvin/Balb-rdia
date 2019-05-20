class LeitorDeDadosDoPoggi:
    
    quantidade_de_bits = None
    quantidade_de_entradas = None
    entradas = None
    file_name = None
    file = None
    file_characters = None
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_file_characters(self):
        return self.file_characters
    
    def open_file(self):
        self.file = open(self.file_name,"r")
    
    def copy_text(self):
        self.file_characters = self.file.readlines() 
        
    def close_file(self):
        self.file.close()
        
    def adjust_file_characters(self):
        new_file_characters = []
        
        for line in self.file_characters:
            new_file_characters.append(line.strip())
        
        self.file_characters = new_file_characters