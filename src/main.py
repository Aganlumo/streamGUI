from openpyxl import load_workbook
import xlrd
import pandas as pd
from Video import Movie, Serie


fname='D:\Argo&Eon\Streaming GUI\streamGUI\DataB\BasePelículas.xlsx'
workbook = xlrd.open_workbook(fname, on_demand=True)        #Determina el numero de filas
sheet=workbook.sheet_by_name('BasePelículas')
row_count=sheet.nrows
DB=pd.read_excel(fname)
moviesL=[]
seriesL=[]
for i in range(row_count-2):
    linea = DB.values[i]
    if type(linea[6])!=str:
        element=Movie(linea[1],linea[3],linea[4],linea[2],linea[5])
        moviesL.append(element)
    else:
        element=Serie(linea[1],linea[3],linea[4],linea[7],linea[5],linea[2],linea[8],linea[6])
        seriesL.append(element)

# for i in seriesL:
#     print(i.name,'  ',i.nameS)
        
    
