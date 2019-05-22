import pyexcel_ods3
from pyexcel_ods3 import save_data
from collections import OrderedDict


def save_new_sheet(name_file, sheet_name, content):
    data = OrderedDict()
    
    first_line_sheet = ["Qual algoritmo", "Qual arquivo", "Qual instancia decimal",
                        "Qual instancia binaria",
                        "Quantos frascos", "Complexidade Teorica",
                        "Tempo de CPU (ms)", "Razao"]
    
    final_data = []
    final_data.append(first_line_sheet)
    
    for content_part in content:
        final_data.append(content_part)
    
    data.update({sheet_name: final_data})
    
    save_data(name_file, data)

save_new_sheet("test.ods", "Sheet 1", [[1, 2, 3], [4, 5, 6]])
