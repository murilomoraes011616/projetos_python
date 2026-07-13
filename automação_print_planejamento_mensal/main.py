import xlwings as xw
wb = xw.Book(r'C:\Users\murilo.oliveira\OneDrive - Greentech\planilhas1.xlsx')
abrir_planilha = wb.sheets('verde')
qual_valor_de_uma_celula = abrir_planilha.range('A1').value
print(qual_valor_de_uma_celula)
abrir_planilha.range('A1').value = 'Olá, Excel!'
qual_valor_de_uma_celula = abrir_planilha.range('A1').value
print(qual_valor_de_uma_celula)
breakpoint