import pyexcel_ods3
from pyexcel_ods3 import save_data
from collections import OrderedDict


def save_new_sheet(name_file, sheet_name, content):
    data = OrderedDict()
    
    first_line_sheet = ["Qual algoritmo", "Qual arquivo", "Qual instancia binaria",
                        "Qual instancia decimal",
                        "Quantos frascos", "Complexidade Teorica",
                        "Tempo de CPU (ms)", "Razao"]
    
    final_data = []
    final_data.append(first_line_sheet)
    
    for content_part in content:
        final_data.append(content_part)
    
    data.update({sheet_name: final_data})
    
    save_data(name_file, data)
