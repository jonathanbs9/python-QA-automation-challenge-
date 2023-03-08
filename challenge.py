from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# URL
URL = 'https://www.espn.com.ar/futbol/posiciones/_/liga/arg.1'

# Chrome Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Instancia de Selenium Web Driver
driver = webdriver.Chrome(
    options=options,
)

driver.maximize_window()
driver.get(URL)

page = BeautifulSoup(driver.page_source, 'html.parser')


#Equipos
equipos = list()
for equipo in page.find_all('span', attrs={'class':'hide-mobile'}):
    #Nombre equipo 
    nombre_equipo = equipo.find('a', attrs={'class': 'AnchorLink'})
    equipos.append(nombre_equipo.text)
print(equipos)


# Posiciones
posiciones = list()
for pos in page.find_all('span', attrs={'class':'team-position ml2 pr3'}):
    posiciones.append(pos.text)
print(posiciones)


# Tabla de datos (PJ -  PG - PE - PP - GF -  GC - DIF - PTS)
todos_puntajes = list()
for data in page.find_all('span', attrs={'class':'stat-cell'}):
    todos_puntajes.append(data.text)
print(todos_puntajes)

# Partidos Jugados (PJ)
i = 0
partidos_jugados = list()
while i < len(todos_puntajes):
    partidos_jugados.append(todos_puntajes[i])
    i+=8
#print(partidos_jugados)


# Partidos Ganados (PG)
i= 1 
partidos_ganados = list()
while i < len(todos_puntajes):
    partidos_ganados.append(todos_puntajes[i])
    i+=8
#print(partidos_ganados)


# Partidos Empatados (PE)
i= 2 
partidos_empatados = list()
while i < len(todos_puntajes):
    partidos_empatados.append(todos_puntajes[i])
    i+=8
#print(partidos_empatados)

# Partidos Perdidos (PP)
i= 3 
partidos_perdidos = list()
while i < len(todos_puntajes):
    partidos_perdidos.append(todos_puntajes[i])
    i+=8
#print(partidos_perdidos)


# Goles a favor (GF)
i = 4
goles_favor = list()
while i < len(todos_puntajes):
    goles_favor.append(todos_puntajes[i])
    i+=8
#print(goles_favor)

# Goles en contra (GC)
i = 5
goles_contra = list()
while i < len(todos_puntajes):
    goles_contra.append(todos_puntajes[i])
    i+=8
#print(goles_contra)

# Diferencia de gol (DIF)
i = 6
diferencia_goles = list()
while i < len(todos_puntajes):
    diferencia_goles.append(todos_puntajes[i])
    i+=8
#print(diferencia_goles)


# Puntos (Pts)
i = 7
puntos = list()
while i < len(todos_puntajes):
    puntos.append(todos_puntajes[i])
    i+=8
#print(puntos)

# Data Frame
df = pd.DataFrame({
    'Posición': posiciones, 
    'Equipos':equipos, 
    'PJ': partidos_jugados, 
    'PG': partidos_ganados, 
    'PE': partidos_empatados, 
    'PP': partidos_perdidos, 
    'GF': goles_favor, 
    'GC':goles_contra, 
    'DIF':diferencia_goles, 
    'PTS':puntos 
})
#print(df)

# Excel file
writer = pd.ExcelWriter('challenge_tabla_posiciones.xlsx')
df.to_excel(writer, 'Torneo futbol argentino', index=False)

# If you want a CSV file
#df.to_csv('challenge_equipos.csv', index = False)

# Save xlsx file
writer.save()

print('Datos exportados!')
driver.quit()
    