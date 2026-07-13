import xlwings as xw
wb = xw.Book(r'C:\Users\murilo.oliveira\OneDrive - Greentech\planilhas1.xlsx') #criadno o wb, objeto da classe book 
abrir_planilha = wb.sheets('verde') #cri auma variavel, que dentro do objeto tem o metodo sheets, que abre a planilha que estiver em seu paramtro ()
qual_valor_de_uma_celula = abrir_planilha.range('A1').value #encontra o valor da celula A1
print(qual_valor_de_uma_celula) #printa esse valor 
abrir_planilha.range('A1').value = 'Olá, Excel!' #encontra esse valor da celula A1 e modifica ele 
qual_valor_ATUALIZADO_de_uma_celula = abrir_planilha.range('A1').value #variavel que equivale ao novo valor r 
print(qual_valor_ATUALIZADO_de_uma_celula)#printa esse novo valor 
