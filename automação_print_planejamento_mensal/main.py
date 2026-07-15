import xlwings as xw # importa a biblioteca para manipular o excel .
from datetime import date # importa sobemente a função date da biblioteca datetime de pega a data, biblioteca do python ja.
import time # importa biblioteca para poder dar o comando de esperar 10 segundos 


wb = xw.Book(r'C:\Users\murilo.oliveira\OneDrive - Greentech\planilhas1.xlsx') #criando o wb, objeto da classe book.
abrir_planilha = wb.sheets('verde') #cria uma variavel, que dentro do objeto tem o metodo sheets, que abre a planilha que estiver em seu paramtro ().
qual_valor_de_uma_celula = abrir_planilha.range('A1').value #encontra o valor da celula A1.
print(qual_valor_de_uma_celula) #printa esse valor.

data_de_hoje = date.today()   # pega a função de hoje da biblioteca datetime e guarda esse valor me um variavel.
abrir_planilha.range('A1').value = data_de_hoje #encontra esse valor da celula A1 e modifica ele.
qual_valor_ATUALIZADO_de_uma_celula = abrir_planilha.range('A1').value #variavel que equivale ao novo valorr.
print(qual_valor_ATUALIZADO_de_uma_celula) #printa esse novo valor.
wb.api.RefreshAll()  ## 
time.sleep(10) #espera 10 segundos no codigo apenas para poder para garantir a atualização dos dados

##ETAPA DE TIRAR O PRINT DA IMAGEM DA TABELA 

aba = wb.sheets('tabela dinamica')   # 1. trasforma

aba.api.PageSetup.PrintArea = 'A3:F5'            # 2. só CONFIGURA, não gera nada ainda
aba.api.PageSetup.Orientation = 2                 # 3. só CONFIGURA, não gera nada ainda
aba.api.PageSetup.Zoom = False                    # 4. só CONFIGURA, não gera nada ainda
aba.api.PageSetup.FitToPagesWide = 1              # 5. só CONFIGURA, não gera nada ainda
aba.api.PageSetup.FitToPagesTall = 1              # 6. só CONFIGURA, não gera nada ainda

aba.api.ExportAsFixedFormat(0, r'C:\Users\murilo.oliveira\OneDrive - Greentech\Perfil\Desktop\lugar dos pdf para autoamação\tabela.pdf')  # 7. ESSA é a linha que EXECUTA e cria o arquivo